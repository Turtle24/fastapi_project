from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password: str):
        """The encryption used to hash the user's password.

        Args:
            password (str): The users passowrd.

        Returns:
            str: Returns a hashed password.
        """
        return pwd_cxt.hash(password)

    def verify(hashed_password,plain_password):
        """Checks that the hashed password matches the plain inputed password.

        Args:
            hashed_password (str): The hashed password in the database.
            plain_password (str): The plain password submitted during login.

        Returns:
            bool: True if the password matched the hash, otherwise False
        """
        return pwd_cxt.verify(plain_password,hashed_password)