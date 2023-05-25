from datetime import datetime

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.tables.base_class import Base, IdMixin


class CreatedRecipe(Base, IdMixin):
    __tablename__ = "created_recipes"

    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"))
    recipe_id: Mapped[int] = mapped_column(ForeignKey("recipes.id"))

    quantity: Mapped[float] = mapped_column(
        default=1,
    )

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
