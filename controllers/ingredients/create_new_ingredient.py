from fastapi import HTTPException

from models import Ingredient

from .get_all_ingredients import INGREDIENTS


async def create_new_ingredient(ingredient: Ingredient) -> Ingredient:
    """
    Create a new ingredient and add it to the list of ingredients.

    Args:
        ingredient (Ingredient): The ingredient object containing name, amount, and nutritional_info.

    Returns:
        new_ingredient: The newly created ingredient object.
    """

    try:
        # check if all fields are not empty
        if not ingredient.name or not ingredient.amount or not ingredient.nutritional_info:
            raise HTTPException(
                status_code=400,
                detail="All fields are required",
            )

        # check if the ingredient is already in the list
        for existing_ingredient in INGREDIENTS:
            if existing_ingredient["name"].lower() == ingredient.name.lower():
                raise HTTPException(
                    status_code=400,
                    detail="Ingredient already exists",
                )

        # Create a new ingredient dictionary
        new_ingredient: Ingredient = {
            "name": ingredient.name,
            "amount": ingredient.amount,
            "nutritional_info": ingredient.nutritional_info,
        }

        # Append the new ingredient to the list
        INGREDIENTS.append(new_ingredient)

        return new_ingredient

    except HTTPException as error:
        raise error
