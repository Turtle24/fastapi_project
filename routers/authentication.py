from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from database import get_db
from schemas import schemas
from models.models_repo import User
from security import token, hashing
from sqlalchemy.orm import Session


router = APIRouter(tags=['Authentication'])

@router.post('/login')
async def login_request(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    check = ("SELECT email, password FROM test.users WHERE email=%s")
    check_user = await db.execute(check, (request.username))
    user = await db.fetchall()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")

    if not hashing.Hash.verify(user[0]['password'], request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")

    access_token = token.create_access_token(data={"sub": user[0]['email']})
    return {"access_token": access_token, "token_type": "bearer"}