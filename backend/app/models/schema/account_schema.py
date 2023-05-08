from typing import List, Optional

from app.models.domain.account_domain import AccountDomain
from app.models.schema.base_schema import BaseSchema


class AccountInLogin(BaseSchema):
    username: str
    password: str


class AccountInCreate(AccountInLogin):
    email: str


# AccountUpdate


class AccountWithToken(AccountDomain):
    token: str


class AccountInResponse(BaseSchema):
    account: AccountDomain


class AccountInResponseWithToken(BaseSchema):
    account: AccountWithToken
