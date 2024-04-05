from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from controllers import (
    create_new_ingredient,
    get_all_ingredients,
    update_an_ingredient,
)
from models import Ingredient, UpdateIngredient

ingredients = APIRouter(prefix="/ingredients", tags=["ingredients"])


@ingredients.get("/", response_model=list[Ingredient], status_code=200)
async def get_ingredients():
    """
    Retrieve all ingredients.

    Returns:
    - `List[Ingredient]`: A list containing all ingredients.

    Raises:
    - `HTTPException 404`: If no ingredients are found.
    - `HTTPException 500`: If an error occurs while retrieving ingredients (unexpected error).
    """

    data = await get_all_ingredients()

    if not data:
        raise HTTPException(status_code=404, detail="Data not found")

    response: dict[str, any] = {
        "message": "success",
        "data": jsonable_encoder(data),
    }

    return JSONResponse(status_code=200, content=response)


@ingredients.post("/new", response_model=Ingredient, status_code=201)
async def create_ingredient(ingredient: Ingredient):
    """
    Create a new ingredient and add it to the list of ingredients.

    Parameters:
    - `ingredient`: An instance of Ingredient class containing information about the new ingredient.

    Returns:
    - `created_ingredient`: The newly created ingredient object.

    Raises:
    - `HTTPException 400`: If all fields (name, amount, nutritional_info) are not provided.
    - `HTTPException 404`: If the ingredient data is not found (unexpected error).
    - `HTTPException 500`: If an error occurs while creating the new ingredient (unexpected error).
    """

    data = await create_new_ingredient(ingredient)

    if not data:
        raise HTTPException(status_code=404, detail="Data not found")

    response: dict[str, any] = {
        "message": "success",
        "data": jsonable_encoder(data),
    }

    return JSONResponse(status_code=201, content=response)


@ingredients.patch("/{ingredient_name}", response_model=Ingredient, status_code=200)
async def update_ingredient(
    ingredient_name: str,
    ingredient_update: UpdateIngredient,
):
    """
    Update an existing ingredient.

    Args:
    - `ingredient_name (str)`: The name of the ingredient to update.
    - `ingredient_update (UpdateIngredient)`: An instance of UpdateIngredient class containing updated information.

    Returns:
    - `Ingredient`: The updated ingredient object.

    Raises:
    - `HTTPException 404`: If the ingredient data is not found.
    - `HTTPException 500`: If an error occurs while updating the ingredient (unexpected error).
    """

    data = await update_an_ingredient(ingredient_name, ingredient_update)

    if not data:
        raise HTTPException(status_code=404, detail="Data not found")

    response: dict[str, any] = {
        "message": "success",
        "data": jsonable_encoder(data),
    }

    return JSONResponse(status_code=200, content=response)
