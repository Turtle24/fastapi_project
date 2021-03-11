from typing import List, Optional
from pydantic import BaseModel
import datetime

class User(BaseModel):
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
    rain: str
    datetime: Optional[datetime.datetime]

class Login(BaseModel):
    username: str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None