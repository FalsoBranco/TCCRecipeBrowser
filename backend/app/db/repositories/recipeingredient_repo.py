from app.db.repositories.base import BaseRepository
from app.db.tables.recipeingredient_table import RecipeIngredient
from app.models.schema.recipeingredient_schema import RecipeIngredientInCreate


class RecipeIngredientRepository(BaseRepository):
    async def add_ingredient_to_recipe(
        self,
        *,
        ingredient_id: int,
        recipe_id: int,
        recipe_extra: RecipeIngredientInCreate
    ):
        recipe_ingredient = RecipeIngredient(
            ingredient_id=ingredient_id,
            recipe_id=recipe_id,
            quantity=recipe_extra.quantity,
        )
        self.session.add(recipe_ingredient)
        await self.session.commit()
        return None
