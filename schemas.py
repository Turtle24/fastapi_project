from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    location: str
