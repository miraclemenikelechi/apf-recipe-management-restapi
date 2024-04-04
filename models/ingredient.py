from pydantic import BaseModel, PositiveFloat

from .nutritional_info import NutritionalInfo


class Ingredient(BaseModel):
    name: str
    amount: PositiveFloat
    nutritional_info: NutritionalInfo
