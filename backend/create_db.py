from sqlalchemy import create_engine
from app.db.base import Base
from app.models.user import User
from app.models.guesstimate import Guesstimate

# Create database connection
engine = create_engine(
    "sqlite:///./sql_app.db",
    connect_args={"check_same_thread": False}
)

def init_db():
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")

if __name__ == "__main__":
    init_db() 