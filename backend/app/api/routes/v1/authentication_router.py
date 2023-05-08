from dataclasses import asdict

from fastapi import APIRouter, Body, Depends, HTTPException, status

from app.config import AppSettings, get_app_settings
from app.constant import string
from app.db.errors import EntityDoesNotExist
from app.db.repositories.account_repo import AccountRepository
from app.db.tables.account_table import Account
from app.dependencies.database import get_repository
from app.models.domain.account_domain import AccountDomain, AccountDomainInDb
from app.models.schema.account_schema import (
    AccountInCreate,
    AccountInLogin,
    AccountInResponse,
    AccountWithToken,
)
from app.models.schema.jwt_schema import JWTInResponse
from app.services import commons, jwt
from app.services.authentication import (
    check_email_is_taken,
    check_username_is_taken,
)

router = APIRouter()


@router.post(
    "/login",
    status_code=status.HTTP_200_OK,
    response_model=JWTInResponse,
    name="auth:login",
)
async def login(
    account_login: AccountInLogin = Body(...),
    account_repo: AccountRepository = Depends(get_repository(AccountRepository)),
    settings: AppSettings = Depends(get_app_settings),
) -> JWTInResponse:

    wrong_login_error = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=string.INCORRECT_LOGIN_INPUT,
        headers={"WWW-Authenticate": "Token"},
    )

    try:
        account_result: Account = await account_repo.get_account_by_username(
            username=account_login.username
        )
        account = AccountDomainInDb(**asdict(account_result))

    except EntityDoesNotExist as existence_error:
        raise wrong_login_error from existence_error

    # Check password
    if not account.check_password(account_login.password):
        raise wrong_login_error

    token = jwt.create_access_token_for_user(account, str(settings.SECRET_KEY))

    data = JWTInResponse(
        access_token=token,
        token_type="Token",
        user=AccountDomain(
            **account.dict(),
        ),
    )
    return data


@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    response_model=JWTInResponse,
    name="auth:register",
)
async def register(
    account_create: AccountInCreate = Body(..., embed=True, alias="account"),
    account_repo: AccountRepository = Depends(get_repository(AccountRepository)),
    settings: AppSettings = Depends(get_app_settings),
) -> JWTInResponse:
    if await check_username_is_taken(account_repo, account_create.username):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=string.USERNAME_TAKEN,
            headers={"WWW-Authenticate": "Token"},
        )

    if await check_email_is_taken(account_repo, account_create.email):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=string.EMAIL_TAKEN,
            headers={"WWW-Authenticate": "Token"},
        )

    account_slug: str = commons.get_slug_from_title(account_create.username)

    account_row: Account = await account_repo.create_account(
        **account_create.dict(), slug=account_slug
    )
    account = AccountDomain(**asdict(account_row))

    token: str = jwt.create_access_token_for_user(account, str(settings.SECRET_KEY))
    data = JWTInResponse(
        access_token=token,
        token_type="Token",
        user=AccountDomain(
            **account.dict(),
        ),
    )
    return data
