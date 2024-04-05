from fastapi import HTTPException

from models import Ingredient, UpdateIngredient

from .get_all_ingredients import INGREDIENTS


async def update_an_ingredient(
    ingredient_name: str,
    ingredient_update: UpdateIngredient,
) -> Ingredient | None:
    try:
        # check if the ingredient exists
        for existing_ingredient in INGREDIENTS:
            if existing_ingredient["name"].lower() == ingredient_name.lower():
                # update the ingredient
                if ingredient_update.name is not None:
                    existing_ingredient["name"] = ingredient_update.name

                if ingredient_update.amount is not None:
                    existing_ingredient["amount"] = ingredient_update.amount

                if ingredient_update.nutritional_info is not None:
                    existing_ingredient["nutritional_info"] = (
                        ingredient_update.nutritional_info
                    )

                return existing_ingredient
        
    except HTTPException as error:
        raise error
