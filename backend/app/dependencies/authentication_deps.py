from typing import Callable, Optional

from fastapi import Depends, HTTPException, Security
from fastapi.security import APIKeyHeader
from jose import ExpiredSignatureError
from starlette import requests, status
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.config import AppSettings, get_app_settings
from app.constant import string
from app.db.errors import EntityDoesNotExist
from app.db.repositories.account_repo import AccountRepository
from app.db.tables.account_table import Account
from app.dependencies.database import get_repository
from app.services import jwt

HEADER_KEY = "Authorization"


class ApiKeyHeader(APIKeyHeader):
    async def __call__(  # noqa: WPS610
        self,
        request: requests.Request,
    ) -> Optional[str]:
        try:
            return await super().__call__(request)
        except StarletteHTTPException as original_auth_exc:
            raise HTTPException(
                status_code=original_auth_exc.status_code,
                detail=string.AUTHENTICATION_REQUIRED,
            )


def get_current_user_authorizer(*, required: bool = True) -> Callable:  # type: ignore
    return _get_current_user if required else _get_current_user_optional


def _get_authorization_header_retriever(
    *,
    required: bool = True,
) -> Callable:  # type: ignore
    return _get_authorization_header if required else _get_authorization_header_optional


def _get_authorization_header(
    api_key: str = Security(ApiKeyHeader(name=HEADER_KEY)),
    settings: AppSettings = Depends(get_app_settings),
) -> str:
    try:
        token_prefix, token = api_key.split(" ")
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=string.WRONG_TOKEN_PREFIX,
        )
    if token_prefix != settings.JWT_TOKEN_PREFIX:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=string.WRONG_TOKEN_PREFIX,
        )

    return token


def _get_authorization_header_optional(
    authorization: Optional[str] = Security(
        ApiKeyHeader(name=HEADER_KEY, auto_error=False),
    ),
    settings: AppSettings = Depends(get_app_settings),
) -> str:
    if authorization:
        return _get_authorization_header(authorization, settings)

    return ""


async def _get_current_user(
    users_repo: AccountRepository = Depends(get_repository(AccountRepository)),
    token: str = Depends(_get_authorization_header_retriever()),
    settings: AppSettings = Depends(get_app_settings),
) -> Account:
    try:
        username: str = jwt.get_username_from_token(
            token,
            str(settings.SECRET_KEY),
        )

    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=string.MALFORMED_PAYLOAD,
        )

    try:
        return await users_repo.get_account_by_username(username=username)
    except EntityDoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=string.MALFORMED_PAYLOAD,
        )


async def _get_current_user_optional(
    repo: AccountRepository = Depends(get_repository(AccountRepository)),
    token: str = Depends(_get_authorization_header_retriever(required=False)),
    settings: AppSettings = Depends(get_app_settings),
) -> Optional[Account]:
    if token:
        return await _get_current_user(repo, token, settings)

    return None
