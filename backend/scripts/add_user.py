from app.db.session import SessionLocal
from app.models.user import User
from app.core.security import get_password_hash

def add_user():
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
    add_user() 