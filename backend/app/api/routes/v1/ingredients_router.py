import string
from datetime import datetime

from fastapi import APIRouter, Depends, Path
from pydantic import BaseModel, Field

from app.db.repositories.Ingredient_repo import IngredientRepository
from app.db.tables.account_table import Account
from app.dependencies.authentication_deps import get_current_user_authorizer
from app.dependencies.database import get_repository

router = APIRouter()


class UnitType(BaseModel):
    unit: str
    slug: str

    class Config:
        orm_mode = True


class IngredientInResponse(BaseModel):
    title: str
    summary: str
    slug: str
    quantity: float
    unit: UnitType

    class Config:
        orm_mode = True


# Listar ingredient
@router.get("/")
async def list_ingredients(
    account: Account = Depends(get_current_user_authorizer()),
    ingredient_repo: IngredientRepository = Depends(
        get_repository(IngredientRepository)
    ),
):
    results = await ingredient_repo.list_all_ingredients(account_id=account.id)

    return [IngredientInResponse.from_orm(result) for result in results]


# Excluir ingredient
@router.delete("/{id}")
async def delete_ingredient(
    id: int = Path(...),
    account: Account = Depends(get_current_user_authorizer()),
    ingredient_repo: IngredientRepository = Depends(
        get_repository(IngredientRepository)
    ),
):
    await ingredient_repo.delete_ingredient(account_id=account.id, ingredient_id=id)

    # TODO Validar se deletou com sucesso
    return {"message": "Deleted"}


# Escolher ingredient pelo slug ou id
@router.get("/{slug_or_id}")
async def get_ingredient(
    slug_or_id: int | str = Path(...),
    account: Account = Depends(get_current_user_authorizer()),
    ingredient_repo: IngredientRepository = Depends(
        get_repository(IngredientRepository)
    ),
) -> None:
    if isinstance(slug_or_id, int):
        ingredient = await ingredient_repo.get_ingredient_by_id(
            account_id=account.id, id=slug_or_id
        )
    else:
        ingredient = await ingredient_repo.get_ingredient_by_slug(
            account_id=account.id, slug=slug_or_id
        )
    print(ingredient)
    return IngredientInResponse.from_orm(ingredient)


# Adicionar ingredient
# Atualizar ingredient
