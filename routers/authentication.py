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
    """The authentication process used to access the third party weather api. The user's email is check to see if they have
       valid credentials. Then the hashed passwords are compared to grant a token to the user.

    Args:
        request (OAuth2PasswordRequestForm, optional): Form that hands username and password. Defaults to Depends().
        db (Session, optional): Database Session. Defaults to Depends(get_db).

    Raises:
        HTTPException: Raises a 404 if the user's username or email in this case isn't found.
        HTTPException: Raises a 404 if the passwords don't match.

    Returns:
        Dict: Returns a dictionary with the access token.
    """
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