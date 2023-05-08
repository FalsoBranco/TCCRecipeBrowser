from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.tables.base_class import Base, IdMixin
from app.db.tables.unittype_table import UnitType


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
    unittype_id: Mapped[int] = mapped_column(ForeignKey("unit_types.id"))

    unit: Mapped[UnitType] = relationship(lazy="joined")
