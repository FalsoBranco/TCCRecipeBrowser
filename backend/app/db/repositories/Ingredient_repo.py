from datetime import date

from fastapi import HTTPException
from sqlalchemy import delete, exc, select
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.db.errors import EntityDoesNotExist
from app.db.repositories.base import BaseRepository
from app.db.repositories.unittype_repo import UnitTypeRepository
from app.db.tables.ingredient_table import Ingredient
from app.db.tables.unittype_table import UnitType
from app.services.commons import get_slug_from_title
from app.services.unittype_service import check_if_unitytype_exists


class IngredientRepository(BaseRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.unittype_repo = UnitTypeRepository(session)
        super().__init__(session)

    async def list_all_ingredients(self, *, account_id: int):
        query = select(Ingredient).where(Ingredient.account_id == account_id)

        result_rows = await self.session.execute(query)

        ingredients = result_rows.scalars().all()
        return ingredients

    async def delete_ingredient(self, *, account_id: int, ingredient_id: int) -> None:
        query = (
            delete(Ingredient)
            .where(Ingredient.account_id == account_id)
            .where(Ingredient.id == ingredient_id)
        )
        await self.session.execute(query)

        await self.session.commit()

        return None

    async def get_ingredient_by_id(self, *, account_id: int, id: int):
        query = (
            select(Ingredient)
            .where(Ingredient.account_id == account_id)
            .where(Ingredient.id == id)
        )

        result_row = await self.session.execute(query)

        ingredient = result_row.scalar_one_or_none()

        if ingredient:
            return ingredient

        raise EntityDoesNotExist(f"Ingredient with id {id} does not exist")

    async def get_ingredient_by_slug(self, *, account_id: int, slug: str):
        query = (
            select(Ingredient)
            .where(Ingredient.account_id == account_id)
            .where(Ingredient.slug == slug)
        )

        result_row = await self.session.execute(query)

        ingredient = result_row.scalar_one_or_none()

        if ingredient:
            return ingredient

        raise EntityDoesNotExist(f"Ingredient with slug {id} does not exist")

    async def create_new_ingredient(
        self,
        *,
        title: str,
        slug: str,
        summary: str | None,
        quantity: int,
        account_id: int,
        expired_date: date,
        unit: str,
    ) -> Ingredient:
        new_unit = await check_if_unitytype_exists(
            unittype_repo=self.unittype_repo,
            slug=get_slug_from_title(unit),
        )
        if not new_unit:
            new_unit = UnitType(unit=unit, slug=get_slug_from_title(unit))

        new_ingredient: Ingredient = Ingredient(
            title=title,
            slug=slug,
            summary=summary,
            quantity=quantity,
            account_id=account_id,
            expired_date=expired_date,
            unit=new_unit,
        )

        try:
            self.session.add(instance=new_ingredient)
            await self.session.commit()
            await self.session.refresh(new_ingredient)

        except exc.IntegrityError:
            await self.session.rollback()

            raise HTTPException(
                status_code=409,
                detail="Resource already exists",
            )
        return new_ingredient
