from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field

class FirebaseBase(BaseModel):
    """Base class for Firebase models"""
    id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class FirebaseUser(FirebaseBase):
    """Firebase User model"""
    email: str
    hashed_password: str
    full_name: Optional[str] = None
    is_active: bool = True
    is_superuser: bool = False
    
    class Config:
        orm_mode = True

class FirebaseTodo(FirebaseBase):
    """Firebase Todo model"""
    title: str
    description: Optional[str] = None
    is_completed: bool = False
    user_id: str
    
    class Config:
        orm_mode = True

class FirebaseCaseStudy(FirebaseBase):
    """Firebase Case Study model"""
    question: str
    solution: str
    user_id: str
    
    class Config:
        orm_mode = True

class FirebaseGuesstimate(FirebaseBase):
    """Firebase Guesstimate model"""
    question: str
    solution: str
    user_id: str
    
    class Config:
        orm_mode = True 