import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()  # reads the .env file

DATABASE_URL = os.getenv("DATABASE_URL")

# The engine is the actual connection to PostgreSQL.
engine = create_engine(DATABASE_URL)

# A session is a short "conversation" with the database.
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# All our future table classes will inherit from Base.
Base = declarative_base()


# FastAPI will use this to give each request its own session,
# then close it when the request finishes.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()