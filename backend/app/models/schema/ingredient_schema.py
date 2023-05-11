from datetime import date
from typing import List, Optional

from app.db.tables.unittype_table import UnitType
from app.models.domain.ingredient_domain import IngredientDomain
from app.models.schema.base_schema import BaseSchema


class IngredientInCreate(BaseSchema):
    title: str
    summary: Optional[str]
    quantity: int
    unit: str
    expired_date: date


class IngredientInUpdate(BaseSchema):
    title: Optional[str]
    summary: Optional[str]
    quantity: Optional[int]
    unit: Optional[str]


class IngredientForResponse(BaseSchema, IngredientDomain):
    """Ingredient Schema"""

    unit: UnitType


class IngredientInResponse(BaseSchema):
    """Response Detail"""

    ingredient: IngredientForResponse


class ListOfIngredientInResponse(BaseSchema):
    """Response List"""

    ingredients: List[IngredientForResponse]
    ingredients_count: int
