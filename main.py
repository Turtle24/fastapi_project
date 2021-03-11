from fastapi import FastAPI
from models import models_repo
from database import engine, get_db
from routers import home, user, weather_api, authentication

app = FastAPI()

models_repo.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(home.router)
app.include_router(user.router)
app.include_router(weather_api.router)


# if __name__ == "__main__":
#     uvicorn.run(app)