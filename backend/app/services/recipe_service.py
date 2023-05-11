from app.db.errors import EntityDoesNotExist
from app.db.repositories.recipe_repo import RecipeRepository


async def check_if_recipes_exists(
    *, recipes_repo: RecipeRepository, slug: str, user_id: int
) -> bool:
    try:
        await recipes_repo.get_recipe_by_slug(slug=slug, account_id=user_id)
    except EntityDoesNotExist:
        return False

    return True
