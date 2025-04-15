from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.user import User
from app.models.guesstimate import Guesstimate
from app.core.security import get_password_hash
from app.core.config import settings

# Create database connection
engine = create_engine(
    "sqlite:///./sql_app.db",
    connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_user():
    db = SessionLocal()
    try:
        # Check if user already exists
        existing_user = db.query(User).filter(User.email == "mihirnarula@gmail.com").first()
        if existing_user:
            print("User already exists!")
            return

        # Create new user
        user = User(
            email="mihirnarula@gmail.com",
            hashed_password=get_password_hash("Password"),
            full_name="Mihir Narula",
            is_active=True,
            is_superuser=False
        )
        db.add(user)
        db.commit()
        print("User created successfully!")
    except Exception as e:
        print(f"Error creating user: {str(e)}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    create_user() 