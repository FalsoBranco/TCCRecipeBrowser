from pydantic import EmailStr, Field

from app.models.domain.base_domain import BaseDomain
from app.services import security


class AccountDomain(BaseDomain):
    username: str
    email: str
    slug: str


class AccountDomainInDb(AccountDomain):
    _id: int = Field(0, alias="id")
    hashed_password: str = ""
    salt: str = ""

    def check_password(self, password: str) -> bool:
        return security.verify_password(self.salt + password, self.hashed_password)

    def change_password(self, password: str) -> None:
        self.salt = security.generate_salt()
        self.hashed_password = security.get_password_hash(self.salt + password)
