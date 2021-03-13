from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from security import token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(data: str = Depends(oauth2_scheme)):
    """Recieves a token as a str from the sub-dependency oauth2_scheme.

    Args:
        data (str): A token str. Defaults to Depends(oauth2_scheme).

    Returns:
        bool: Returns True if the user's credentials are validated else False
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return token.verify_token(data, credentials_exception)