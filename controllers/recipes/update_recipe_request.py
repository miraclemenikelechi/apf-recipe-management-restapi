from uuid import UUID

from fastapi import HTTPException

from models import Recipe, UpdateRecipe

from .create_new_recipe import RECIPES


async def update_recipe_request(
    recipe_id: UUID,
    recipe_update: UpdateRecipe,
) -> Recipe | None:
    """
    Update an existing recipe with the given ID using the provided update data.

    Args:
    - recipe_id (UUID): The UUID of the recipe to update.
    - recipe_update (UpdateRecipe): An instance of UpdateRecipe class containing updated information.

    Returns:
    - Optional[Recipe]: The updated recipe object if found, otherwise None.

    Raises:
    - HTTPException 404: If the recipe is not found for the given ID.
    """

    for existing_recipe in RECIPES:
        if existing_recipe["test_id"] == recipe_id:
            # Update recipe fields if the corresponding update data is provided
            if recipe_update.title is not None:
                existing_recipe["title"] = recipe_update.title

            if recipe_update.description is not None:
                existing_recipe["description"] = recipe_update.description

            if recipe_update.ingredients is not None:
                existing_recipe["ingredients"] = recipe_update.ingredients

            return existing_recipe

    raise HTTPException(
        status_code=404,
        detail="Recipe not found for the given ID: {}".format(recipe_id),
    )
