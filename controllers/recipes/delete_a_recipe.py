from uuid import UUID

from fastapi import HTTPException

from models import Recipe

from .create_new_recipe import RECIPES


async def delete_a_recipe(recipe_id: UUID) -> Recipe | None:
    """
    A function to delete a recipe.
    """

    try:
        # check if the recipe exists
        for existing_recipe in RECIPES:
            if existing_recipe["test_id"] == recipe_id:
                RECIPES.remove(existing_recipe)
                return existing_recipe

    except HTTPException as error:
        raise error
