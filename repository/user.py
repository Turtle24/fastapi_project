from sqlalchemy.orm import Session
from schemas import schemas
from models import models_repo
from fastapi import HTTPException, status
import json
from security import hashing

async def create(request: schemas.User, db:Session):
    statement = ("INSERT INTO test.users (name, email, password, city, country)" 
                "VALUES (%s, %s, %s, %s, %s)")
    new_user = await db.execute(statement, (request.name, request.email, hashing.Hash.bcrypt(request.password), request.city, request.country))
    if not new_user:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED,
                            detail=f"The user could not be created")
    user = schemas.User(name=request.name, email=request.email, password=hashing.Hash.bcrypt(request.password),city=request.city, country=request.country)
    return user
    
async def show(id:int, db:Session):
    query = await db.execute(f"SELECT * FROM users WHERE id = {id};")   
    results = await db.fetchall()
    if not results:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} can not be found")
    return results[0]