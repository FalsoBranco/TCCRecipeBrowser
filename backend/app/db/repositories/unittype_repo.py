from sqlalchemy import select

from app.db.errors import EntityDoesNotExist
from app.db.repositories.base import BaseRepository
from app.db.tables.unittype_table import UnitType


class UnitTypeRepository(BaseRepository):
    async def get_unit_by_slug(self, *, slug: str):
        query = select(UnitType).where(UnitType.slug == slug)

        result = await self.session.execute(query)

        unit = result.scalar_one_or_none()

        if unit:
            return unit

        raise EntityDoesNotExist("Could not find unit")
