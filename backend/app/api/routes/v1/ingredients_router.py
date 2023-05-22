from fastapi import APIRouter, Body, Depends, HTTPException, Path, status

from app.db.repositories.ingredient_repo import IngredientRepository
from app.db.tables.account_table import Account
from app.dependencies.authentication_deps import get_current_user_authorizer
from app.dependencies.database import get_repository
from app.models.schema.ingredient_schema import (
    IngredientForResponse,
    IngredientInCreate,
    IngredientInResponse,
    ListOfIngredientInResponse,
)
from app.services.commons import get_slug_from_title
from app.services.ingredient_service import check_if_ingredients_exists

router = APIRouter()


# Listar ingredient
@router.get(
    "/",
    name="ingredients:list-ingredients",
    response_model=ListOfIngredientInResponse,
    status_code=status.HTTP_200_OK,
)
async def list_ingredients(
    account: Account = Depends(get_current_user_authorizer()),
    ingredient_repo: IngredientRepository = Depends(
        get_repository(IngredientRepository)
    ),
) -> ListOfIngredientInResponse:
    results = await ingredient_repo.list_all_ingredients(account_id=account.id)

    ingredients = [IngredientForResponse.from_orm(result) for result in results]

    return ListOfIngredientInResponse(
        ingredients=ingredients, ingredients_count=len(ingredients)
    )


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    name="ingredients:delete-ingredients",
)
async def delete_ingredient(
    id: int = Path(...),
    account: Account = Depends(get_current_user_authorizer()),
    ingredient_repo: IngredientRepository = Depends(
        get_repository(IngredientRepository)
    ),
) -> None:
    await ingredient_repo.delete_ingredient(account_id=account.id, ingredient_id=id)


# Escolher ingredient pelo slug ou id
@router.get(
    "/{slug_or_id}",
    status_code=status.HTTP_200_OK,
    name="ingredients:get-ingredient",
    response_model=IngredientInResponse,
)
async def get_ingredient(
    slug_or_id: int | str = Path(...),
    account: Account = Depends(get_current_user_authorizer()),
    ingredient_repo: IngredientRepository = Depends(
        get_repository(IngredientRepository)
    ),
) -> IngredientInResponse:
    if isinstance(slug_or_id, int):
        ingredient = await ingredient_repo.get_ingredient_by_id(
            account_id=account.id, id=slug_or_id
        )
    else:
        ingredient = await ingredient_repo.get_ingredient_by_slug(
            account_id=account.id, slug=slug_or_id
        )
    print(ingredient)
    return IngredientInResponse(ingredient=IngredientForResponse.from_orm(ingredient))


# Adicionar ingredient
@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=IngredientInResponse,
    name="ingredients:create-ingredient",
)
async def create_ingredient(
    ingredient_repo: IngredientRepository = Depends(
        get_repository(IngredientRepository)
    ),
    account: Account = Depends(get_current_user_authorizer()),
    new_ingredient: IngredientInCreate = Body(..., embed=True, alias="ingredient"),
) -> IngredientInResponse:
    # Create slug from title
    ingredient_slug: str = get_slug_from_title(title=new_ingredient.title)

    # Check if ingredient already exists in database
    if await check_if_ingredients_exists(
        ingredients_repo=ingredient_repo, slug=ingredient_slug, user_id=account.id
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Ingredient already exists"
        )

    # Create new ingredient
    ingredient_row = await ingredient_repo.create_new_ingredient(
        title=new_ingredient.title,
        slug=ingredient_slug,
        summary=new_ingredient.summary,
        quantity=new_ingredient.quantity,
        account_id=account.id,
        expired_date=new_ingredient.expired_date,
        unit=new_ingredient.unit,
    )
    ingredient = IngredientForResponse.from_orm(ingredient_row)
    return IngredientInResponse(ingredient=ingredient)


# Atualizar ingredient
