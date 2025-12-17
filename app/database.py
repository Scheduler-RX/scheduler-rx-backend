import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

# Use the same URL you used for Alembic
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# This is the "Base" your models.py already uses (or should use)
# If your models.py defines its own Base, we might need to unify them, 
# but usually, we define Base here and import it in models.
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# Dependency: This gives each request a fresh DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()