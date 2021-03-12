from fastapi import APIRouter
import database, models
from schemas import schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from repository import user
from typing import List
from security.oauth2 import get_current_user

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db


@router.post('/sign-up', response_model=schemas.User, status_code=status.HTTP_201_CREATED)
async def create_user(request: schemas.User, db: Session = Depends(get_db)):
    query = await user.create(request,db)
    return query

@router.get('/{id}', response_model=schemas.ShowUser, status_code=status.HTTP_200_OK)
async def get_user(id:int, db: Session = Depends(get_db)):
    query = await user.show(id, db)
    return query

@router.delete('/delete/{id}', response_model=schemas.ShowUser, status_code=status.HTTP_202_ACCEPTED)
async def delete_user(id: int, db: Session = Depends(get_db)):
    delete = await user.delete_user(id, db)
    return delete
    
@router.put('/update/{id}', response_model=schemas.User, status_code=status.HTTP_202_ACCEPTED)
async def update_user(id: int, request: schemas.User, db: Session = Depends(get_db)):
    update = await user.update_user(id, request, db)
    return update