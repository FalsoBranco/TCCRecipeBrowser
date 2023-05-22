from fastapi import APIRouter, Body, Depends, HTTPException, Path, status

from app.db.repositories.recipe_repo import RecipeRepository
from app.db.tables.account_table import Account
from app.dependencies.authentication_deps import get_current_user_authorizer
from app.dependencies.database import get_repository
from app.models.schema.recipe_schema import (
    ListOfRecipeInResponse,
    RecipeForResponse,
    RecipeInCreate,
    RecipeInResponse,
)
from app.services.commons import get_slug_from_title
from app.services.recipe_service import check_if_recipes_exists

router = APIRouter()


# Listar recipes
@router.get(
    "/",
    name="recipes:list-recipes",
    response_model=ListOfRecipeInResponse,
    status_code=status.HTTP_200_OK,
)
async def list_recipes(
    account: Account = Depends(get_current_user_authorizer()),
    recipe_repo: RecipeRepository = Depends(get_repository(RecipeRepository)),
) -> ListOfRecipeInResponse:
    results = await recipe_repo.list_all_recipes(account_id=account.id)

    recipes = [RecipeForResponse.from_orm(result) for result in results]

    return ListOfRecipeInResponse(recipes=recipes, recipes_count=len(recipes))


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    name="recipes:delete-recipes",
)
async def delete_recipe(
    id: int = Path(...),
    account: Account = Depends(get_current_user_authorizer()),
    recipe_repo: RecipeRepository = Depends(get_repository(RecipeRepository)),
) -> None:
    await recipe_repo.delete_recipe(account_id=account.id, recipe_id=id)


# Escolher recipe pelo slug ou id
@router.get(
    "/{slug_or_id}",
    status_code=status.HTTP_200_OK,
    name="recipes:get-recipe",
    response_model=RecipeInResponse,
)
async def get_recipe(
    slug_or_id: int | str = Path(...),
    account: Account = Depends(get_current_user_authorizer()),
    recipe_repo: RecipeRepository = Depends(get_repository(RecipeRepository)),
) -> RecipeInResponse:
    if isinstance(slug_or_id, int):
        recipe = await recipe_repo.get_recipe_by_id(
            account_id=account.id, id=slug_or_id
        )
    else:
        recipe = await recipe_repo.get_recipe_by_slug(
            account_id=account.id, slug=slug_or_id
        )
    print(recipe)
    return RecipeInResponse(recipe=RecipeForResponse.from_orm(recipe))


# Adicionar recipe
@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=RecipeInResponse,
    name="recipes:create-recipe",
)
async def create_recipe(
    recipe_repo: RecipeRepository = Depends(get_repository(RecipeRepository)),
    account: Account = Depends(get_current_user_authorizer()),
    new_recipe: RecipeInCreate = Body(..., embed=True, alias="recipe"),
) -> RecipeInResponse:
    # Create slug from title
    recipe_slug: str = get_slug_from_title(title=new_recipe.title)

    # Check if recipe already exists in database
    if await check_if_recipes_exists(
        recipes_repo=recipe_repo, slug=recipe_slug, user_id=account.id
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Recipe already exists"
        )
    print("passow")
    # Create new recipe
    recipe_row = await recipe_repo.create_new_recipe(
        amounts=new_recipe.amounts,
        account_id=account.id,
        instructions=new_recipe.instructions,
        slug=recipe_slug,
        summary=new_recipe.summary,
        title=new_recipe.title,
        unit=new_recipe.unit,
    )

    return RecipeInResponse(recipe=RecipeForResponse.from_orm(recipe_row))


@router.get("/{recipe_id}/ingredients")
async def get_recipe_with_ingredients(
    recipe_id: int = Path(...),
    account: Account = Depends(get_current_user_authorizer()),
    recipe_repo: RecipeRepository = Depends(get_repository(RecipeRepository)),
):
    await recipe_repo.get_recipe_instructions(
        recipe_id=recipe_id, account_id=account.id
    )

    # ingredient_instructions: list[RecipeIngredientForResponse] = [
    #     RecipeIngredientForResponse.from_orm(step) for step in recipe.ingredients
    # ]

    # recipe_for_response: RecipeWithInstructionsForResponse = (
    #     RecipeWithInstructionsForResponse.from_orm(recipe)
    # )
    # recipe_for_response.ingredients = ingredient_instructions
    # return RecipeWithInstructionInResponse(recipe=recipe_for_response)
