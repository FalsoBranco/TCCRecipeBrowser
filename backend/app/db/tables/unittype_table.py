from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.tables.base_class import Base, IdMixin


class UnitType(Base, IdMixin):
    __tablename__ = "unit_types"

    unit: Mapped[str] = mapped_column(
        String(75),
        nullable=False,
        index=True,
    )
    slug: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )
