from fastapi import APIRouter
import database, schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from fastapi.responses import HTMLResponse
from starlette.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import fastapi
from repository.home import get_home

router = APIRouter(
    prefix="/home",
    tags=['Home']
)

router.mount("/static", StaticFiles(directory="static"), name="static")

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    home = await get_home(request)
    return home