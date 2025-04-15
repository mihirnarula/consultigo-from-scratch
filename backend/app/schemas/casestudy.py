from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class CaseStudyBase(BaseModel):
    """Base schema for Case Study"""
    title: str
    description: Optional[str] = None
    content: str
    category: Optional[str] = None
    difficulty: Optional[str] = None

class CaseStudyCreate(CaseStudyBase):
    """Schema used for case study creation"""
    pass

class CaseStudyUpdate(CaseStudyBase):
    """Schema used for case study update"""
    title: Optional[str] = None
    content: Optional[str] = None

class CaseStudyInDBBase(CaseStudyBase):
    """Base schema for case studies retrieved from the database"""
    id: str
    user_id: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class CaseStudy(CaseStudyInDBBase):
    """Schema used for returning case study information to client"""
    pass 