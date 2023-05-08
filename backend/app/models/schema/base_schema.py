from typing import Literal

from app.models.domain.base_domain import BaseDomain


class BaseSchema(BaseDomain):
    class Config(BaseDomain.Config):
        orm_mode: Literal[True] = True
