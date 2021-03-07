from fastapi import APIRouter
import database, schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from repository import user

router = APIRouter(
    prefix="/home",
    tags=['Home']
)

get_db = database.get_db


@router.get('/')
def home():
    return 'Running!'