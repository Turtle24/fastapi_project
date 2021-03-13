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
from typing import Optional

load_dotenv() 
API_KEY = os.environ.get("API_KEY")


async def get_weather(city:str, country:str, db: Session, user_id:Optional[int] = None):
    """Calls the weather api and checks if the endpoint is live, if a user is passed into the function,
       then their id is added to the query to be commited to the database. Normal weather queries and user
       queries use this function.

    Args:
        city (str): The city the user inputs
        country (str): The country the user inputs.
        db (Session): The database session that the query is commited to.
        user_id (Optional[int], optional): Optional user id. Defaults to None.

    Raises:
        HTTPException: If there is no response then a 404 error is raised

    Returns:
        Dict: Returns a dictionary.
    """
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&units=metric&appid={API_KEY}"
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(url)
            resp.raise_for_status()
        except httpx.HTTPError as exc:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Error response, while requesting city :{city}, Country: {country}.")
        data = resp.json()
    
    weather = data['weather']
    conditions = weather[0]['main']
    forecast = data['main']
    tempreture = forecast['temp']
    date_time = datetime.datetime.now()

    if user_id is None:
        statement = ("INSERT INTO test.weather (city, country, tempreture, conditions, datetime)" 
                    "VALUES (%s, %s, %s, %s, %s)")
        new_weather = await db.execute(statement, (city, country, tempreture, conditions, date_time))
    else:
        statement = ("INSERT INTO test.weather (city, country, tempreture, conditions, datetime, user_id)" 
                    "VALUES (%s, %s, %s, %s, %s, %s)")
        new_weather = await db.execute(statement, (city, country, tempreture, conditions, date_time, user_id))
    weather = schemas.Weather(city=city, country=country ,tempreture=tempreture, conditions=conditions, datetime=date_time, user_id=user_id)
    return weather

async def get_all_weather(db: Session):
    """Gets all the weather data in the weather table in the database.

    Args:
        db (Session): The database session that is queried.

    Raises:
        HTTPException: If there are no results then a 204 error is raised.

    Returns:
        List: Returns a list of all the weather entries in the weather table.
    """
    statement = ("SELECT * FROM test.weather")
    query = await db.execute(statement)
    results = await db.fetchall()
    if not results:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,
                            detail=f"The database didn't return anything")
    return results