from models.models_repo import Weather
from fastapi import APIRouter
import database, schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from repository import user, weather_api
from typing import List

router = APIRouter(
    prefix="/weather",
    tags=['Weather']
)

get_db = database.get_db
@router.post("/api/umbrella", response_model= schemas.Weather)
async def weather(request: schemas.Weather, db: Session = Depends(get_db)):
    request = await weather_api.get_weather(request)
    print("off")
    return request