from datetime import datetime

from app.models.domain.account_domain import AccountDomain
from app.models.schema.base_schema import BaseSchema


class JWTMeta(BaseSchema):
    exp: datetime
    sub: str
    type: str


class JWTUser(BaseSchema):
    username: str


class JWTInResponse(BaseSchema):
    access_token: str
    token_type: str
    user: AccountDomain
