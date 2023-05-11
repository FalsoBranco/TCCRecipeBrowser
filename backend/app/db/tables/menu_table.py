from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.tables.account_table import Account
from app.db.tables.base_class import Base, IdMixin


class Menu(Base, IdMixin):
    __tablename__ = "menus"

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
    content: Mapped[str] = mapped_column(
        default=None,
    )

    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"))
