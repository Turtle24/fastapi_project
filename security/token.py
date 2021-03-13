from datetime import datetime, timedelta
from jose import JWTError, jwt
from schemas import schemas
from settings import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM

def create_access_token(data: dict):
    """Creates an access token that expires after 30 minutes.

    Args:
        data (dict): A dictionary containing the user's email.

    Returns:
        str: The string representation of the header, claims, and signature.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token:str, credentials_exception):
    """Verifys the token and raises exceptions if the user's email isn't in the database or if there's a JWTError.

    Args:
        token (str): The created token from create_access_token.
        credentials_exception (HTTPException): A HTTPException if the credntials couldn't be validated.

    Raises:
        credentials_exception: If there isn't an email in the payload.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except JWTError:
        raise credentials_exception