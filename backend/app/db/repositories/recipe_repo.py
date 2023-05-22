from fastapi import HTTPException
from sqlalchemy import delete, exc, select
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import joinedload

from app.db.errors import EntityDoesNotExist
from app.db.repositories.base import BaseRepository
from app.db.repositories.unittype_repo import UnitTypeRepository
from app.db.tables.recipe_table import Recipe
from app.db.tables.recipeingredient_table import RecipeIngredient
from app.db.tables.unittype_table import UnitType
from app.services.commons import get_slug_from_title
from app.services.unittype_service import check_if_unitytype_exists


class RecipeRepository(BaseRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.unittype_repo = UnitTypeRepository(session)
        super().__init__(session)

    async def list_all_recipes(self, *, account_id: int):
        query = select(Recipe).where(Recipe.account_id == account_id)

        result_rows = await self.session.execute(query)

        recipes = result_rows.scalars().all()
        return recipes

    async def delete_recipe(self, *, account_id: int, recipe_id: int) -> None:
        query = (
            delete(Recipe)
            .where(Recipe.account_id == account_id)
            .where(Recipe.id == recipe_id)
        )
        await self.session.execute(query)

        await self.session.commit()

        return None

    async def get_recipe_by_id(self, *, account_id: int, id: int):
        query = (
            select(Recipe).where(Recipe.account_id == account_id).where(Recipe.id == id)
        )

        result_row = await self.session.execute(query)

        recipe = result_row.scalar_one_or_none()

        if recipe:
            return recipe

        raise EntityDoesNotExist(f"Recipe with id {id} does not exist")

    async def get_recipe_by_slug(self, *, account_id: int, slug: str):
        query = (
            select(Recipe)
            .where(Recipe.account_id == account_id)
            .where(Recipe.slug == slug)
        )

        result_row = await self.session.execute(query)

        recipe = result_row.scalar_one_or_none()

        if recipe:
            return recipe

        raise EntityDoesNotExist(f"Recipe with slug {id} does not exist")

    async def create_new_recipe(
        self,
        *,
        slug: str,
        account_id: int,
        title: str,
        summary: str,
        amounts: int,
        instructions: str,
        unit: str,
    ):
        new_unit = await check_if_unitytype_exists(
            unittype_repo=self.unittype_repo,
            slug=get_slug_from_title(unit),
        )
        print(new_unit)
        if not new_unit:
            new_unit = UnitType(unit=unit, slug=get_slug_from_title(unit))

        new_recipe: Recipe = Recipe(
            title=title,
            slug=slug,
            summary=summary,
            amounts=amounts,
            account_id=account_id,
            instructions=instructions,
            unittype_id=None,
            unit=new_unit,
        )

        try:
            self.session.add(instance=new_recipe)
            await self.session.commit()
            await self.session.refresh(new_recipe)

        except exc.IntegrityError:
            await self.session.rollback()

            raise HTTPException(
                status_code=409,
                detail="Resource already exists",
            )
        return new_recipe

    async def get_recipe_instructions(
        self, *, account_id: int, recipe_id: int
    ) -> Recipe:
        query = (
            select(Recipe).where(Recipe.id == recipe_id)
            # .where(Recipe.account_id == account_id)
            .options(
                joinedload(
                    Recipe.ingredients,
                    innerjoin=True,
                ).joinedload(
                    RecipeIngredient.ingredient,
                    innerjoin=True,
                )
            )
        )
        recipe_row = await self.session.execute(query)

        result: Recipe | None = recipe_row.unique().scalar_one_or_none()
        print(result.ingredients)
        if not result:
            raise EntityDoesNotExist

        return result
