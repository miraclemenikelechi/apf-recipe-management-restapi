from uuid import UUID, uuid4

from fastapi import HTTPException
from pydantic import (
    BaseModel,
    Field,
    PositiveFloat,
    PositiveInt,
    field_validator,
)

from .ingredient import Ingredient


class Instruction(BaseModel):
    id: PositiveInt = Field(
        default=1,
        gt=1,
        description="id of the instruction",
    )

    description: str = Field(
        min_length=3,
        max_length=500,
        description="the instruction",
    )


class Recipe(BaseModel):
    test_id: UUID = Field(default_factory=uuid4)

    title: str = Field(
        min_length=3,
        max_length=120,
        description="the title of the recipe",
    )

    description: str = Field(
        min_length=3,
        max_length=500,
        description="the description of the recipe",
    )

    cooking_instructions: list[Instruction]

    @field_validator("coking_instructions", check_fields=False)
    @classmethod
    def validate_cooking_instructions(cls, value: any) -> any:
        if len(value) < 1:
            raise HTTPException(
                status_code=400,
                detail="Instructions cannot be empty",
            )

        return value

    ingredients: list[Ingredient]

    @field_validator("ingredients", check_fields=False)
    @classmethod
    def validate_cooking_ingredients(cls, value: any) -> any:
        if len(value) < 1:
            raise HTTPException(
                status_code=400,
                detail="Instructions cannot be empty",
            )

        return value

    time_to_prepare: PositiveFloat = Field(
        description="the time to prepare in minutes",
        gt=0,
    )

    servings: PositiveFloat = Field(
        gt=0,
        description="the number of servings",
    )
