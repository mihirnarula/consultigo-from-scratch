from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    is_completed: bool = False

class TodoCreate(TodoBase):
    pass

class TodoUpdate(TodoBase):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None

class TodoInDBBase(TodoBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class Todo(TodoInDBBase):
    pass 