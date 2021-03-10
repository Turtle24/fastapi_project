from models.models_repo import Weather
from fastapi import APIRouter
import database
from schemas import schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from repository import user, weather_api
from typing import List

router = APIRouter(
    prefix="/weather",
    tags=['Weather']
)

get_db = database.get_db
@router.post("/api/weather", response_model= schemas.Weather)
async def weather(city: str, country: str, db: Session = Depends(get_db)):
    request = await weather_api.get_weather(city, country, db)
    print("off")
    return request