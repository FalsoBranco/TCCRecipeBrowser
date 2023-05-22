from fastapi import APIRouter, Body, Depends, Path

from app.db.repositories.recipeingredient_repo import RecipeIngredientRepository
from app.dependencies.database import get_repository
from app.models.schema.recipeingredient_schema import RecipeIngredientInCreate

router = APIRouter()


@router.post("/{recipe_id}/ingredient/{ingredient_id}")
async def add_ingredient_to_recipe(
    ingredient_id: int = Path(...),
    recipe_id: int = Path(...),
    recipe_ingredient_repo: RecipeIngredientRepository = Depends(
        get_repository(RecipeIngredientRepository)
    ),
    recipe_extra: RecipeIngredientInCreate = Body(..., embed=True, alias="extra"),
) -> None:
    await recipe_ingredient_repo.add_ingredient_to_recipe(
        recipe_id=recipe_id, ingredient_id=ingredient_id, recipe_extra=recipe_extra
    )
    return None
