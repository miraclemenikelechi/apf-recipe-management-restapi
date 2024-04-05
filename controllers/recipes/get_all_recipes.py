from fastapi import HTTPException

from models import Recipe

from .create_new_recipe import RECIPES


async def get_all_recipes() -> list[Recipe]:
    """
    A function to get all recipes.
    """

    try:
        return RECIPES

    except HTTPException as error:
        raise error
