from sqlalchemy import create_engine
from app.db.base import Base
from app.models.user import User
from app.models.guesstimate import Guesstimate
from app.core.security import get_password_hash

# Create database connection
engine = create_engine(
    "sqlite:///./sql_app.db",
    connect_args={"check_same_thread": False}
)

def init_db():
    # Drop all tables
    Base.metadata.drop_all(bind=engine)
    # Create all tables
    Base.metadata.create_all(bind=engine)
    
    # Create a session
    from sqlalchemy.orm import sessionmaker
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    
    try:
        # Create user
        user = User(
            email="mihirnarula@gmail.com",
            hashed_password=get_password_hash("Password"),
            full_name="Mihir Narula",
            is_active=True,
            is_superuser=False
        )
        db.add(user)
        db.commit()
        print("Database initialized and user created successfully!")
    except Exception as e:
        print(f"Error: {str(e)}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    init_db() 