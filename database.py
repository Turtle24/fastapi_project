from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings import USERNAME, DATABASE_PASSWORD
from fastapi import HTTPException, status
from check_calls import calltracker
import asyncio
import aiomysql

SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://{USERNAME}:{DATABASE_PASSWORD}@127.0.0.1:3306/test'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

async def get_db():
    loop = asyncio.get_event_loop()
    async with aiomysql.connect(host='127.0.0.1', port=3306,
                                user=f'{USERNAME}', password=f'{DATABASE_PASSWORD}',
                                db='test', loop=loop, autocommit=False) as conn:
        cursor = await conn.cursor(aiomysql.DictCursor) 

        if not cursor:
            raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                            detail=f"Could not connect to the database")
        yield cursor
        await conn.commit()
        conn.close()
        
if __name__ == "__main__":
    loop.run_until_complete(get_db(loop))