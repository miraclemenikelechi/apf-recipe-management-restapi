from uuid import UUID

from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from controllers import (
    create_new_recipe,
    get_all_recipes,
    update_recipe_request,
    delete_a_recipe,
)
from models import Recipe, UpdateRecipe

recipes = APIRouter(prefix="/recipes", tags=["recipes"])


@recipes.post("/new", response_model=Recipe, status_code=201)
async def create_recipe(recipe: Recipe):
    """
    Create a new recipe and add it to the list of recipes.

    Parameters:
    - `recipe`: An instance of Recipe class containing information about the new recipe.

    Returns:
    - `created_recipe`: The newly created recipe object.

    Raises:
    - `HTTPException 400`: If all fields (name, ingredients, instructions) are not provided.
    - `HTTPException 404`: If the recipe data is not found (unexpected error).
    - `HTTPException 500`: If an error occurs while creating the new recipe (unexpected error).
    """

    data = await create_new_recipe(recipe)

    if not data:
        raise HTTPException(status_code=404, detail="Data not found")

    response: dict[str, any] = {
        "message": "success",
        "data": jsonable_encoder(data),
    }

    return JSONResponse(status_code=201, content=response)


@recipes.get("/", response_model=list[Recipe], status_code=200)
async def get_recipes():
    """
    Retrieve all recipes.

    Returns:
    - `List[Recipe]`: A list containing all recipes.

    Raises:
    - `HTTPException 404`: If no recipes are found.
    - `HTTPException 500`: If an error occurs while retrieving recipes (unexpected error).
    """

    data = await get_all_recipes()

    if not data:
        raise HTTPException(status_code=404, detail="Data not found")

    response: dict[str, any] = {
        "message": "success",
        "data": jsonable_encoder(data),
    }

    return JSONResponse(status_code=200, content=response)


@recipes.patch("/{recipe_id}", response_model=Recipe, status_code=200)
async def update_recipe(
    recipe_id: UUID,
    recipe_update: UpdateRecipe,
):
    """
    Update an existing recipe.

    Args:
    - `recipe_id (UUID)`: The ID of the recipe to update.
    - `recipe_update (UpdateRecipe)`: An instance of UpdateRecipe class containing updated information.

    Returns:
    - `Recipe`: The updated recipe object.

    Raises:
    - `HTTPException 404`: If the recipe data is not found.
    - `HTTPException 500`: If an error occurs while updating the recipe (unexpected error).
    """

    data = await update_recipe_request(recipe_id, recipe_update)

    if not data:
        raise HTTPException(status_code=404, detail="Data not found")

    response: dict[str, any] = {
        "message": f"updated recipe with the id of {recipe_id}",
        "data": jsonable_encoder(data),
    }

    return JSONResponse(status_code=200, content=response)


@recipes.delete("/{recipe_id}", status_code=200)
async def delete_recipe(recipe_id: UUID):
    """
    Delete an existing recipe.

    Args:
    - `recipe_id (UUID)`: The ID of the recipe to delete.

    Raises:
    - `HTTPException 404`: If the recipe data is not found.
    - `HTTPException 500`: If an error occurs while deleting the recipe (unexpected error).
    """

    data = await delete_a_recipe(recipe_id)

    if not data:
        raise HTTPException(status_code=404, detail="Data not found")

    response: dict[str, any] = {
        "message": f"deleted recipe with the id of {recipe_id}",
        "data": jsonable_encoder(data),
    }

    return JSONResponse(status_code=200, content=response)
