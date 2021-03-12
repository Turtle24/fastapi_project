from typing import List, Optional
from pydantic import BaseModel
import datetime

class User(BaseModel):
    id: int
    name: str
    email: str
    password: str
    city: str
    country: str

class ShowUser(BaseModel):
    name: str
    email: str

class Weather(BaseModel):
    city: str
    country: str
    tempreture: int
    conditions: str
    datetime: Optional[datetime.datetime] 
    user_id: Optional[int] = None

class GetUserWeather(BaseModel):
    city: str
    country: str

class Login(BaseModel):
    username: str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None