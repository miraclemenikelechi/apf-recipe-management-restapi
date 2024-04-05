from datetime import datetime
from uuid import uuid4

from fastapi import HTTPException

from models import Recipe
from utils import generate_id

RECIPES: list[Recipe] = []


async def create_new_recipe(recipe: Recipe) -> Recipe:
    """
    Create a new recipe and add it to the list of recipes.

    Args:
    - recipe (Recipe): An instance of Recipe class containing information about the new recipe.

    Returns:
    - Recipe: The newly created recipe object.

    Raises:
    - ValueError: If any required field in the recipe object is empty or invalid.
    - Exception: If an error occurs while creating the new recipe (unexpected error).
    """

    if not recipe.title or not recipe.description:
        raise HTTPException(
            status_code=400,
            detail="Title and description are required fields",
        )

    created_recipe: Recipe = {
        "id": generate_id(),
        "test_id": uuid4(),
        "createdAt": datetime.now(),
        "title": recipe.title,
        "description": recipe.description,
        "cooking_instructions": recipe.cooking_instructions,
        "ingredients": recipe.ingredients,
        "time_to_prepare": recipe.time_to_prepare,
        "servings": recipe.servings,
    }

    RECIPES.append(created_recipe)

    return created_recipe
