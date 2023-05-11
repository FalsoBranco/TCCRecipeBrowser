from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.tables.account_table import Account
from app.db.tables.base_class import Base, IdMixin
from app.db.tables.ingredient_table import Ingredient
from app.db.tables.unittype_table import UnitType


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
