from datetime import datetime
from typing import TYPE_CHECKING, List

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.tables.base_class import Base, IdMixin
from app.db.tables.unittype_table import UnitType

if TYPE_CHECKING:
    from app.db.tables.recipeingredient_table import RecipeIngredient


class Ingredient(Base, IdMixin):
    __tablename__ = "ingredients"

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
    quantity: Mapped[float] = mapped_column(
        default=0,
    )
    expired_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=None
    )

    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"))
    unittype_id: Mapped[int] = mapped_column(ForeignKey("unit_types.id"), default=None)

    unit: Mapped[UnitType] = relationship(lazy="joined")
    recipes: Mapped[List["RecipeIngredient"]] = relationship(
        back_populates="ingredient", default_factory=list, init=False, repr=False
    )
