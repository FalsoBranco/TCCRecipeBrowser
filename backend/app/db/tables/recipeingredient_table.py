from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.tables.base_class import Base, IdMixin
from app.db.tables.ingredient_table import Ingredient
from app.db.tables.recipe_table import Recipe
from app.db.tables.unittype_table import UnitType


class RecipeIngredient(Base, IdMixin):
    __tablename__ = "recipe_ingredients"

    quantity: Mapped[float] = mapped_column(default=1)

    unittype_id: Mapped[int] = mapped_column(ForeignKey("unit_types.id"))
    unit: Mapped[UnitType] = relationship(lazy="joined")

    recipe_id: Mapped[int] = mapped_column(ForeignKey("recipes.id"))
    ingredient_id: Mapped[int] = mapped_column(ForeignKey("ingredients.id"))
