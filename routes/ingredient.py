from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

ingredients = APIRouter(prefix="/ingredients", tags=["ingredients"])


@ingredients.get("/")
async def get_all_ingredients():
    pass
