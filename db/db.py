import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASE = "postgresql"
USER = os.environ.get("POSTGRES_USER")
PASSWORD = os.environ.get("POSTGRES_PASSWORD")
NAME = os.environ.get("POSTGRES_DB")
HOST = os.environ.get("POSTGRES_HOST")

SQLALCHEMY_DATABASE_URL = "{}://{}:{}@{}/{}".format(
    DATABASE, USER, PASSWORD, HOST, NAME
)
print(SQLALCHEMY_DATABASE_URL)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Session:
    try:
        db = sessionLocal()
        yield db
    finally:
        db.close()