from sqlalchemy.orm import Session
from fastapi import HTTPException, status

@app.get('/')
def home():
    return 'Running!'