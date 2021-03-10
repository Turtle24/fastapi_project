from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    city: str
    country: str

class Weather(BaseModel):
    city: str
    country: str
    tempreture: int
    rain: str