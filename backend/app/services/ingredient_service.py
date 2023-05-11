from app.db.errors import EntityDoesNotExist
from app.db.repositories.ingredient_repo import IngredientRepository


async def check_if_ingredients_exists(
    *, ingredients_repo: IngredientRepository, slug: str, user_id: int
) -> bool:
    try:
        await ingredients_repo.get_ingredient_by_slug(slug=slug, account_id=user_id)
    except EntityDoesNotExist:
        return False

    return True
