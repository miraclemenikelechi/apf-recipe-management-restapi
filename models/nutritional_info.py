from pydantic import BaseModel, Field, PositiveFloat


class NutritionalInfo(BaseModel):
    calories: PositiveFloat = Field(
        gt=0,
        description="Calories per serving",
        precision=2,
    )

    protein: PositiveFloat = Field(
        gt=0,
        description="Protein per serving",
        precision=2,
    )

    fat: PositiveFloat = Field(
        gt=0,
        description="Fat per serving",
        precision=2,
    )
