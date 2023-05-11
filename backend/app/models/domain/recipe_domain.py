from pydantic import Field

from app.models.domain.base_domain import BaseDomain


class RecipeDomain(BaseDomain):
    id_: int = Field(0, alias="id")
    title: str
    summary: str
    slug: str
    amounts: float
    instructions: str
