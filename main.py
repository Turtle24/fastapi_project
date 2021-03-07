from fastapi import FastAPI
import models
from database import engine, get_db
from routers import home, user

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(home.router)
app.include_router(user.router)