from sqlalchemy.orm import Session
from schemas import schemas
from models import models_repo
from fastapi import HTTPException, status
import json

# from ..hashing import Hash


async def create(request: schemas.User, db:Session):
    # new_user = await db.execute(f"INSERT INTO test.users (name, email, location) VALUES ({str(request.name)}, {str(request.email)}, {str(request.location)})")
    # new_user = models.User(name=request.name, email=request.email, location=request.location)
    data = {'name': request.name, 'email': request.email, 'city': request.city, 'country': request.country}
    # print(data.values())  
    statement = ("INSERT INTO test.users (name, email, city, country)" 
                "VALUES (%s, %s, %s, %s)")
    new_user = await db.execute(statement, (request.name, request.email, request.city, request.country))

    return data
    

async def show(id:int, db:Session):
    query = await db.execute(f"SELECT * FROM users WHERE id = {id};")   
    results = await db.fetchall()
    if not results:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} can not be found")
    return results[0]