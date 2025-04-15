from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class GuesstimateBase(BaseModel):
    """Base schema for Guesstimate"""
    title: str
    description: Optional[str] = None
    content: str
    category: Optional[str] = None
    difficulty: Optional[str] = None

class GuesstimateCreate(GuesstimateBase):
    """Schema used for guesstimate creation"""
    pass

class GuesstimateUpdate(GuesstimateBase):
    """Schema used for guesstimate update"""
    title: Optional[str] = None
    content: Optional[str] = None

class GuesstimateInDBBase(GuesstimateBase):
    """Base schema for guesstimate retrieved from the database"""
    id: str
    user_id: Optional[str] = None

    class Config:
        orm_mode = True

class Guesstimate(GuesstimateInDBBase):
    """Schema used for returning guesstimate information to client"""
    pass 