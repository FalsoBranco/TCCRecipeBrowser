from app.db.errors import EntityDoesNotExist
from app.db.repositories.unittype_repo import UnitTypeRepository
from app.db.tables.unittype_table import UnitType


async def check_if_unitytype_exists(
    *, unittype_repo: UnitTypeRepository, slug: str
) -> UnitType | None:
    try:
        return await unittype_repo.get_unit_by_slug(slug=slug)
    except EntityDoesNotExist:
        return None
