from typing import Optional, Dict, Any, List, Union
from pydantic import EmailStr

from app.core.security import get_password_hash, verify_password
from app.db.firebase_repository import UserFirebaseRepository
from app.models.firebase_models import FirebaseUser
from app.schemas.user import UserCreate, UserUpdate

class CRUDFirebaseUser:
    def __init__(self):
        self.repository = UserFirebaseRepository(FirebaseUser)
    
    def get(self, id: str) -> Optional[FirebaseUser]:
        """Get user by ID"""
        return self.repository.get(id)
    
    def get_by_email(self, email: str) -> Optional[FirebaseUser]:
        """Get user by email"""
        return self.repository.get_by_email(email)
    
    def get_multi(self, skip: int = 0, limit: int = 100) -> List[FirebaseUser]:
        """Get multiple users with pagination"""
        return self.repository.get_multi(skip, limit)
    
    def create(self, obj_in: UserCreate) -> FirebaseUser:
        """Create a new user"""
        data = obj_in.dict()
        hashed_password = get_password_hash(data.pop("password"))
        
        user_data = {
            "email": data["email"],
            "hashed_password": hashed_password,
            "full_name": data.get("full_name", ""),
            "is_active": data.get("is_active", True),
            "is_superuser": data.get("is_superuser", False),
        }
        
        return self.repository.create(user_data)
    
    def update(self, id: str, obj_in: Union[UserUpdate, Dict[str, Any]]) -> Optional[FirebaseUser]:
        """Update a user"""
        if isinstance(obj_in, UserUpdate):
            update_data = obj_in.dict(exclude_unset=True)
        else:
            update_data = obj_in
        
        if "password" in update_data:
            hashed_password = get_password_hash(update_data.pop("password"))
            update_data["hashed_password"] = hashed_password
        
        return self.repository.update(id, update_data)
    
    def authenticate(self, email: str, password: str) -> Optional[FirebaseUser]:
        """Authenticate a user with email and password"""
        user = self.get_by_email(email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user
    
    def is_active(self, user: FirebaseUser) -> bool:
        """Check if user is active"""
        return user.is_active
    
    def is_superuser(self, user: FirebaseUser) -> bool:
        """Check if user is superuser"""
        return user.is_superuser

firebase_user = CRUDFirebaseUser() 