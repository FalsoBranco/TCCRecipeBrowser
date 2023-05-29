from app.models.schema.base_schema import BaseSchema
from app.models.schema.ingredient_schema import IngredientForResponse


class RecipeIngredientForResponse(BaseSchema):
    id: int
    quantity: int
    ingredient: IngredientForResponse


class RecipeIngredientInCreate(BaseSchema):
    quantity: int
    unittype_id: int
    unittype_id: int
