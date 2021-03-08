from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status
import json
# from ..hashing import Hash

async def create(request: schemas.User, db:Session):
    # new_user = await db.execute(f"INSERT INTO test.users (name, email, location) VALUES ({str(request.name)}, {str(request.email)}, {str(request.location)})")
    # new_user = models.User(name=request.name, email=request.email, location=request.location)
    data = [
        (f'({request.name})'), (f'({request.email})'), (f'({request.location})')
        ]
        
    statement = "INSERT INTO test.users (name, email, location) VALUES ('%s', '%s', %s)"
    await db.executemany(statement, data)
    return new_user[0]
    

async def show(id:int, db:Session):
    query = await db.execute(f"SELECT * FROM users WHERE id = {id};")   
    results = await db.fetchall()
    if not results:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} can not be found")
    return results[0]