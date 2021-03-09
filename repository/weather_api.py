from sqlalchemy.orm import Session
import schemas
from models.models_repo import User
from fastapi import HTTPException, status, Depends
import json
import httpx
import os 
from dotenv import load_dotenv
from repository import user

load_dotenv() 
API_KEY = os.environ.get("API_KEY")


async def get_weather(request: schemas.Weather, db: Session):
    print("off")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={request.city},{request.country}&units=metric&appid={API_KEY}"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()
        data = resp.json()

    return data
        
    # weather = data['weather']
    # category = weather[0]['main']

    # forecast = data['main']
    # temp = forecast['temp']

    # weather = Weather(tempreture=temp, rain=category)

    # return weather