import os
from dotenv import load_dotenv
from sqlmodel import create_engine, Session
from models import User
from sqlmodel import SQLModel, Field

load_dotenv()  # reads variables from .env into the environment

DATABASE_URL = os.getenv("DATABASE_URL")

# echo=True prints every SQL query to your terminal — useful while learning,
# turn it off (False) later once you trust what's happening
engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    """Yields a database session, one per request. FastAPI will call this
    via Depends() so every route gets a fresh session automatically."""
    with Session(engine) as session:
        yield session