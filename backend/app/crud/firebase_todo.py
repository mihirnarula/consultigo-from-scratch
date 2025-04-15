from typing import Optional, Dict, Any, List, Union
from datetime import datetime

from app.db.firebase_repository import TodoFirebaseRepository
from app.models.firebase_models import FirebaseTodo
from app.schemas.todo import TodoCreate, TodoUpdate

class CRUDFirebaseTodo:
    def __init__(self):
        self.repository = TodoFirebaseRepository(FirebaseTodo)
    
    def get(self, id: str) -> Optional[FirebaseTodo]:
        """Get todo by ID"""
        return self.repository.get(id)
    
    def get_multi(self, skip: int = 0, limit: int = 100) -> List[FirebaseTodo]:
        """Get multiple todos with pagination"""
        return self.repository.get_multi(skip, limit)
    
    def get_multi_by_user(self, user_id: str, skip: int = 0, limit: int = 100) -> List[FirebaseTodo]:
        """Get todos for a specific user"""
        return self.repository.get_multi_by_user(user_id, skip, limit)
    
    def get_by_user(self, user_id: str, todo_id: str) -> Optional[FirebaseTodo]:
        """Get a todo for a specific user"""
        return self.repository.get_by_user(user_id, todo_id)
    
    def create(self, obj_in: TodoCreate) -> FirebaseTodo:
        """Create a new todo"""
        data = obj_in.dict()
        return self.repository.create(data)
    
    def create_with_user(self, obj_in: TodoCreate, user_id: str) -> FirebaseTodo:
        """Create a new todo with user_id"""
        data = obj_in.dict()
        data["user_id"] = user_id
        return self.repository.create(data)
    
    def update(self, id: str, obj_in: Union[TodoUpdate, Dict[str, Any]]) -> Optional[FirebaseTodo]:
        """Update a todo"""
        if isinstance(obj_in, TodoUpdate):
            update_data = obj_in.dict(exclude_unset=True)
        else:
            update_data = obj_in
        
        return self.repository.update(id, update_data)
    
    def remove(self, id: str) -> bool:
        """Delete a todo"""
        return self.repository.delete(id)

firebase_todo = CRUDFirebaseTodo() 