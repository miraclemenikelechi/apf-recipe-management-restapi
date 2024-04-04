from pydantic import BaseModel, PositiveFloat

from .nutritional_info import NutritionalInfo


class UpdateIngredient(BaseModel):
    name: str
    amount: PositiveFloat
    nutritional_info: NutritionalInfo


class UpdateRecipe(BaseModel):
    title: str
    description: str
    ingredients: list[UpdateIngredient]
