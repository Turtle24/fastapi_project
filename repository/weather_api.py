from sqlalchemy.orm import Session
from schemas import schemas
from fastapi import HTTPException, status, Depends
import json
import httpx
import os 
from dotenv import load_dotenv
from repository import user


load_dotenv() 
API_KEY = os.environ.get("API_KEY")


async def get_weather(city: str, country: str, db: Session):
    print("off")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&units=metric&appid={API_KEY}"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()
        data = resp.json()
    
    weather = data['weather']
    rain = weather[0]['main']

    forecast = data['main']
    tempreture = forecast['temp']

    statement = ("INSERT INTO test.weather (city, country, tempreture, rain)" 
                "VALUES (%s, %s, %s, %s)")
    new_user = await db.execute(statement, (city, country, tempreture, rain))

    weather = schemas.Weather(city=city, country=country ,tempreture=tempreture, rain=rain)
    return weather