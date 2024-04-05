from models import Ingredient
from utils import load_data

INGREDIENTS: list[Ingredient] = load_data("assets/ingredients.json")


async def get_all_ingredients() -> list[Ingredient]:
    """
    A function to get all ingredients.
    """

    return INGREDIENTS
