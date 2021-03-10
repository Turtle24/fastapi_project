from fastapi import APIRouter
import database, schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from fastapi.responses import HTMLResponse
from starlette.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import fastapi

templates = Jinja2Templates(directory="templates")

def get_home(request: Request):
    data = {
        "page": "Home page"
    }
    return templates.TemplateResponse("index.html", {"request": request, "data": data})