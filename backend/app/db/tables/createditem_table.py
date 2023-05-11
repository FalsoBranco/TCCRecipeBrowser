from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.tables.account_table import Account
from app.db.tables.base_class import Base, IdMixin
from app.db.tables.ingredient_table import Ingredient
from app.db.tables.unittype_table import UnitType


class CreatedRecipe(Base, IdMixin):
    __tablename__ = "created_recipes"

    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"))
    recipe_id: Mapped[int] = mapped_column(ForeignKey("recipes.id"))

    quantity: Mapped[float] = mapped_column(
        default=1,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), insert_default="now()"
    )
