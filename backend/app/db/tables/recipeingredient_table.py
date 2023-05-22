from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.tables.base_class import Base, IdMixin

if TYPE_CHECKING:
    from app.db.tables.ingredient_table import Ingredient
    from app.db.tables.recipe_table import Recipe


class RecipeIngredient(Base, IdMixin):
    __tablename__ = "recipe_ingredients"

    quantity: Mapped[float] = mapped_column(default=1)

    # account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"))

    recipe_id: Mapped[int] = mapped_column(ForeignKey("recipes.id"), default=None)

    ingredient_id: Mapped[int] = mapped_column(
        ForeignKey("ingredients.id"), default=None
    )

    ingredient: Mapped["Ingredient"] = relationship(
        back_populates="recipes", default=None, init=False
    )
    recipe: Mapped["Recipe"] = relationship(
        back_populates="ingredients", default=None, init=False
    )
