from fastapi import APIRouter

from app.api.routes.v1 import (
    accounts_router,
    authentication_router,
    ingredients_router,
    recipeingredient_router,
    recipes_router,
)

api_router: APIRouter = APIRouter()

api_router.include_router(
    authentication_router.router,
    prefix="/auth",
    tags=["Authentication"],
)
api_router.include_router(
    ingredients_router.router,
    prefix="/ingredients",
    tags=["Ingredient"],
)
api_router.include_router(
    accounts_router.router,
    prefix="/users",
    tags=["User"],
)
api_router.include_router(
    recipes_router.router,
    prefix="/recipes",
    tags=["Recipe"],
)
api_router.include_router(
    recipeingredient_router.router,
    prefix="/recipe-ingredient",
    tags=["Recipe Ingredient"],
)
