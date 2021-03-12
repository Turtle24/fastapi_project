from sqlalchemy.orm import Session
from schemas import schemas
from fastapi import HTTPException, status, Depends
import json
import httpx
import os 
from dotenv import load_dotenv
from repository import user
import datetime
from models import models_repo

load_dotenv() 
API_KEY = os.environ.get("API_KEY")


async def get_weather(city:str, country:str, db: Session):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&units=metric&appid={API_KEY}"
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(url)
            resp.raise_for_status()
        except httpx.HTTPError as exc:
            raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY,
                            detail=f"Error response, while requesting city :{city}, Country: {country}.")
        data = resp.json()
    weather = data['weather']
    conditions = weather[0]['main']

    forecast = data['main']
    tempreture = forecast['temp']
    date_time = datetime.datetime.now()
    statement = ("INSERT INTO test.weather (city, country, tempreture, conditions, datetime)" 
                "VALUES (%s, %s, %s, %s, %s)")
    new_weather = await db.execute(statement, (city, country, tempreture, conditions, date_time))
    weather = schemas.Weather(city=city, country=country ,tempreture=tempreture, conditions=conditions, datetime=date_time)
    return weather

async def get_all_weather(db: Session):
    statement = ("SELECT * FROM test.weather")
    query = await db.execute(statement)
    results = await db.fetchall()
    if not results:
        raise HTTPException(status_code=status.HTTP_504_GATEWAY_TIMEOUT,
                            detail=f"The database didn't return anything")
    return results