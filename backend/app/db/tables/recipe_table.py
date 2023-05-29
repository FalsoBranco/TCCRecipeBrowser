from typing import TYPE_CHECKING, List

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.tables.base_class import Base, IdMixin
from app.db.tables.unittype_table import UnitType

if TYPE_CHECKING:
    from app.db.tables.recipeingredient_table import RecipeIngredient


class Recipe(Base, IdMixin):
    __tablename__ = "recipes"

    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"))

    title: Mapped[str] = mapped_column(
        String(75),
        nullable=False,
        index=True,
    )
    summary: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )
    slug: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )
    amounts: Mapped[float] = mapped_column(
        default=0,
    )
    unittype_id: Mapped[int] = mapped_column(ForeignKey("unit_types.id"))
    unit: Mapped[UnitType] = relationship(lazy="joined")

    instructions: Mapped[str] = mapped_column(
        default=None,
    )
    ingredients: Mapped[List["RecipeIngredient"]] = relationship(
        back_populates="recipe",
        default_factory=list,
        init=False,
    )
