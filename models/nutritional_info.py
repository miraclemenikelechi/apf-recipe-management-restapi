from pydantic import BaseModel, Field, PositiveFloat


class NutritionalInfo(BaseModel):
    calories: PositiveFloat = Field(
        gt=0,
        description="Calories per serving",
    )

    protein: PositiveFloat = Field(
        gt=0,
        description="Protein per serving",
    )

    fat: PositiveFloat = Field(
        gt=0,
        description="Fat per serving",
    )
