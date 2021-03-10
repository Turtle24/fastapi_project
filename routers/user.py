from fastapi import APIRouter
import database, models
from schemas import schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from repository import user
from typing import List

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db


@router.post('/', response_model=schemas.User)
async def create_user(request: schemas.User, db: Session = Depends(get_db)):
    query = await user.create(request,db)
    return query

@router.get('/{id}', response_model=schemas.User)
async def get_user(id:int, db: Session = Depends(get_db)):
    query = await user.show(id, db)
    return query