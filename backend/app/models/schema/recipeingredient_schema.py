from app.models.schema.base_schema import BaseSchema


class RecipeIngredientInCreate(BaseSchema):
    quantity: int
    unittype_id: int
