from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Use DATABASE_URL if available, otherwise use SQLALCHEMY_DATABASE_URI
database_url = settings.DATABASE_URL or settings.SQLALCHEMY_DATABASE_URI

engine = create_engine(
    database_url,
    connect_args={"check_same_thread": False}  # Only needed for SQLite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 