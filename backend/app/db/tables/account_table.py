from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.tables.base_class import Base, IdMixin


class Account(Base, IdMixin):
    __tablename__ = "accounts"
    username: Mapped[str] = mapped_column(
        String(75),
        nullable=False,
        index=True,
    )
    email: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )
    slug: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )
    hashed_password: Mapped[str] = mapped_column(
        default=None,
    )
    salt: Mapped[str] = mapped_column(
        default=None,
    )
