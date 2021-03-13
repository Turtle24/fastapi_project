from dotenv import load_dotenv
import os
from pathlib import Path 

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

USERNAME = os.getenv("db_user_name")
DATABASE_PASSWORD = os.getenv("db_password")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
