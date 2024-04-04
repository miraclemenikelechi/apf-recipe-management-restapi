from fastapi import APIRouter


recipes = APIRouter(prefix="/recipes", tags=["recipes"])
