from typing import Tuple

from fastapi import HTTPException
from pydantic import EmailStr
from sqlalchemy import Result, Select, exc, select

from app.db.errors import EntityDoesNotExist
from app.db.repositories.base import BaseRepository
from app.db.tables.account_table import Account
from app.models.domain.account_domain import AccountDomainInDb


class AccountRepository(BaseRepository):
    async def get_account_by_email(self, *, email: EmailStr) -> Account:
        query: Select[Tuple[Account]] = (
            select(Account).where(Account.email == email).limit(1)
        )

        account_result: Result[Tuple[Account]] = await self.session.execute(query)

        account: Account | None = account_result.scalar_one_or_none()

        if account:
            return account

        raise EntityDoesNotExist(f"user with email {email} does not exist")

    async def get_account_by_username(self, *, username: str) -> Account:

        query: Select[Tuple[Account]] = (
            select(Account).where(Account.username == username).limit(1)
        )

        account_result: Result[Tuple[Account]] = await self.session.execute(query)

        account: Account | None = account_result.scalar_one_or_none()

        if account:
            return account

        raise EntityDoesNotExist(f"user with username {username} does not exist")

    async def create_account(
        self, *, username: str, email: EmailStr, slug: str, password: str
    ):
        account = AccountDomainInDb(username=username, email=email, slug=slug)

        account.change_password(password)

        account_row = Account(**account.dict())
        try:
            
            self.session.add(account_row)
            
            await self.session.commit()
            await self.session.refresh(account_row)

        except exc.IntegrityError:
            await self.session.rollback()

            raise HTTPException(
                status_code=409,
                detail="Resource already exists",
            )

        return account_row
