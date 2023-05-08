from dataclasses import asdict

from fastapi import APIRouter, Depends

from app.config import AppSettings, get_app_settings
from app.db.tables.account_table import Account
from app.dependencies.authentication_deps import get_current_user_authorizer
from app.models.domain.account_domain import AccountDomain
from app.models.schema.account_schema import AccountInResponse, AccountWithToken
from app.services import jwt

router = APIRouter()


@router.get("/me", response_model=AccountInResponse, name="accounts:get-current-user")
async def retrieve_current_user(
    account: Account = Depends(get_current_user_authorizer(required=True)),
) -> AccountInResponse:

    account_domain = AccountDomain(**asdict(account))

    return AccountInResponse(account=account_domain)
