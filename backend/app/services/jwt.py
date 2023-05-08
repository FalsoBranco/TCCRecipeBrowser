from datetime import datetime, timedelta
from typing import Dict

from jose import JWTError, jwt
from pydantic import ValidationError

from app.models.domain.account_domain import AccountDomain
from app.models.schema.jwt_schema import JWTMeta, JWTUser

JWT_TYPE = "access"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # one week


def _create_access_token(
    *,
    subject: str,
    jwt_content: Dict[str, str],
    secret_key: str,
    expires_delta: timedelta
) -> str:
    to_encode = jwt_content.copy()

    expire = datetime.utcnow() + expires_delta

    to_encode.update(JWTMeta(exp=expire, sub=subject, type=JWT_TYPE).dict())

    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=ALGORITHM)
    return encoded_jwt


def create_access_token_for_user(account: AccountDomain, secret_key: str) -> str:
    return _create_access_token(
        jwt_content=JWTUser(username=account.username).dict(),
        subject=account.email,
        secret_key=secret_key,
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    )


def get_username_from_token(token: str, secret_key: str) -> str:
    try:
        return JWTUser(**jwt.decode(token, secret_key, algorithms=[ALGORITHM])).username
    except JWTError as decode_error:
        raise ValueError("unable to decode JWT token") from decode_error
    except ValidationError as validation_error:
        raise ValueError("malformed payload in token") from validation_error
