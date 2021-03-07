from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings import USERNAME, DATABASE_PASSWORD

SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://{USERNAME}:{DATABASE_PASSWORD}@127.0.0.1:3306/test'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

# async def get_db():
#     db = await SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
import asyncio
import aiomysql

loop = asyncio.get_event_loop()

async def get_db():
    db = await SessionLocal()
    