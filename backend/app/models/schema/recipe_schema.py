from typing import List, Optional

from app.db.tables.unittype_table import UnitType
from app.models.domain.recipe_domain import RecipeDomain
from app.models.schema.base_schema import BaseSchema


class RecipeInCreate(BaseSchema):
    title: str
    summary: str
    amounts: int
    instructions: str
    unit: str


class RecipeForResponse(BaseSchema, RecipeDomain):
    """Recipe Schema"""

    unit: UnitType


class RecipeInResponse(BaseSchema):
    """Response Detail"""

    recipe: RecipeForResponse


class ListOfRecipeInResponse(BaseSchema):
    """Response List"""

    recipes: List[RecipeForResponse]
    recipes_count: int
