from datetime import datetime

from sqlalchemy import Integer, func
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    MappedAsDataclass,
    mapped_column,
)


class Base(DeclarativeBase):
    pass


class DatetimeMixin(MappedAsDataclass):
    created_at: Mapped[datetime] = mapped_column(
        insert_default=func.utc_timestamp(), init=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        insert_default=func.utc_timestamp(), init=False
    )


class IdMixin(MappedAsDataclass, kw_only=True):
    id: Mapped[int] = mapped_column(
        Integer(),
        # init=False,
        default=None,
        primary_key=True,
        index=True,
        nullable=False,
    )
