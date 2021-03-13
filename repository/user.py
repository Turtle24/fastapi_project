from sqlalchemy.orm import Session
from schemas import schemas
from models import models_repo
from fastapi import HTTPException, status
import json
from security import hashing
from repository import weather_api 

async def create(request: schemas.SignUpUser, db:Session):
    """Creates a new user and inserts their information into the database.

    Args:
        request (schemas.User): The request schema used for creating a new user.
        db (Session): The database session used for the new user instertion.

    Raises:
        HTTPException: If the new_user execute fails the exception will be raised.

    Returns:
        Dict: Returns a dictionary of the new user's details.
    """
    statement = ("INSERT INTO test.users (name, email, password, city, country)" 
                "VALUES (%s, %s, %s, %s, %s)")
    new_user = await db.execute(statement, (request.name, request.email, hashing.Hash.bcrypt(request.password), request.city, request.country))
    if not new_user:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED,
                            detail=f"The user could not be created")
    user = schemas.SignUpUser(name=request.name, email=request.email, password=hashing.Hash.bcrypt(request.password),city=request.city, country=request.country)
    return user
    
async def show(id:int, db:Session):
    """Retrieves a user from the database.

    Args:
        id (int): The user's id being queried
        db (Session): The database session used for the query.

    Raises:
        HTTPException: If the query fails and no user is found, the exception will raise.

    Returns:
        Dict: Returns a dictionary of the users details.
    """
    query = await db.execute(f"SELECT * FROM users WHERE id = {id};")   
    results = await db.fetchall()
    if not results:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} can not be found")
    return results[0]

async def delete_user(id: int, db: Session):
    """Deletes a user from the database

    Args:
        id (int): User's id
        db (Session): The database session used for the query.

    Raises:
        HTTPException: If the query fails and no user is found, the exception will raise.

    Returns:
        Dict: Returns a dictionary of the deleted user.
    """
    check = await show(id, db)
    query = await db.execute(f"DELETE FROM test.users WHERE id = {id};")
    deleted = await db.fetchall()
    if not check:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} can not be found")
    return check

async def update_user(id: int, request: schemas.SignUpUser, db: Session):
    """Updates a user's details in the database.

    Args:
        id (int): The user's id.
        request (schemas.User): The schema used to update the users details.
        db (Session): The database session used.

    Returns:
        Dict: New details served in a dictionary.
    """
    statement = (f"UPDATE test.users SET name=%s, email=%s, password=%s, city=%s, country=%s WHERE id = {id}")
    data = (request.name, request.email, hashing.Hash.bcrypt(request.password), request.city, request.country)
    await db.execute(statement, data)
    updated = await show(id, db)
    return updated

async def create_weather(id: int, db = Session):
    """Creates weather entries based on user id's

    Args:
        id (int): The users id
        db (Session): The database session. Defaults to Session.

    Returns:
        Weather Schema: Returns Weather Schema but displays as a dictionary in the Swagger UI.
    """
    query_user = await show(id, db)
    query_weather = await weather_api.get_weather(query_user['city'], query_user['country'], db, query_user['id'])
    return query_weather

async def get_weather(id: int, db = Session):
    """Retrieves all the user weather requests.

    Args:
        id (int): The user's id.
        db (Session): The database session. Defaults to Session.

    Raises:
        HTTPException: If the user's id isn't found then the 404 exception is raised.

    Returns:
        List: Returns a list of all the user's weather requests in the database.
    """
    query = await db.execute(f"SELECT * FROM weather WHERE user_id = {id};")   
    results = await db.fetchall()
    if not results:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} can not be found")
    return results