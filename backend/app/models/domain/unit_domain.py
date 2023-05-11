from pydantic import Field

from app.models.domain.base_domain import BaseDomain


class UnitDomain(BaseDomain):
    id_: int = Field(0, alias="id")
    unit: str
    slug: str
