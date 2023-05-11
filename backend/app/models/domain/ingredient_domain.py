from datetime import datetime

from pydantic import Field

from app.models.domain.base_domain import BaseDomain
from app.models.domain.unit_domain import UnitDomain


class IngredientDomain(BaseDomain):
    id_: int = Field(0, alias="id")
    title: str
    slug: str
    summary: str
    quantity: int
    expired_date: datetime
