from typing import Dict, List, Optional, Any, TypeVar, Generic, Type
from datetime import datetime
import json
from uuid import uuid4
from pydantic import BaseModel

from app.db.firebase import get_ref, get_users_ref, get_todos_ref

T = TypeVar('T')

class FirebaseRepository(Generic[T]):
    """Generic repository for Firebase Realtime Database operations"""
    
    def __init__(self, model_class: Type[T], base_ref_path: str):
        self.model_class = model_class
        self.base_ref = get_ref(base_ref_path)
    
    def get(self, id: str) -> Optional[T]:
        """Get a single item by ID"""
        data = self.base_ref.child(id).get()
        if not data:
            return None
        # Convert Firebase data to the model
        data['id'] = id
        return self.model_class(**data)
    
    def get_multi(self, skip: int = 0, limit: int = 100) -> List[T]:
        """Get multiple items with pagination"""
        data = self.base_ref.get() or {}
        items = []
        
        # Convert Firebase data to list of models
        for id, item_data in list(data.items())[skip:skip+limit]:
            item_data['id'] = id
            items.append(self.model_class(**item_data))
        
        return items
    
    def create(self, obj_in: Dict[str, Any]) -> T:
        """Create a new item"""
        # Generate an ID if not provided
        id = obj_in.get('id') or str(uuid4())
        
        # Add timestamps
        obj_in['created_at'] = datetime.utcnow().isoformat()
        obj_in['updated_at'] = datetime.utcnow().isoformat()
        
        # Remove ID from the data to be stored (it's the key)
        data_to_store = obj_in.copy()
        if 'id' in data_to_store:
            del data_to_store['id']
        
        # Store in Firebase
        self.base_ref.child(id).set(data_to_store)
        
        # Return the created item
        return self.get(id)
    
    def update(self, id: str, obj_in: Dict[str, Any]) -> Optional[T]:
        """Update an existing item"""
        # Check if item exists
        existing_data = self.base_ref.child(id).get()
        if not existing_data:
            return None
        
        # Update timestamp
        obj_in['updated_at'] = datetime.utcnow().isoformat()
        
        # Update in Firebase
        self.base_ref.child(id).update(obj_in)
        
        # Return the updated item
        return self.get(id)
    
    def delete(self, id: str) -> bool:
        """Delete an item"""
        # Check if item exists
        existing_data = self.base_ref.child(id).get()
        if not existing_data:
            return False
        
        # Delete from Firebase
        self.base_ref.child(id).delete()
        return True


class UserFirebaseRepository(FirebaseRepository):
    """Repository for User operations with Firebase"""
    
    def __init__(self, model_class):
        super().__init__(model_class, 'users')
    
    def get_by_email(self, email: str) -> Optional[T]:
        """Get a user by email"""
        # Firebase doesn't support querying by field directly, so we need to manually filter
        all_users = self.base_ref.get() or {}
        
        for id, user_data in all_users.items():
            if user_data.get('email') == email:
                user_data['id'] = id
                return self.model_class(**user_data)
                
        return None


class TodoFirebaseRepository(FirebaseRepository):
    """Repository for Todo operations with Firebase"""
    
    def __init__(self, model_class):
        super().__init__(model_class, 'todos')
    
    def get_by_user(self, user_id: str, todo_id: str) -> Optional[T]:
        """Get a todo that belongs to a specific user"""
        todo = self.get(todo_id)
        if todo and todo.user_id == user_id:
            return todo
        return None
    
    def get_multi_by_user(self, user_id: str, skip: int = 0, limit: int = 100) -> List[T]:
        """Get all todos for a specific user"""
        data = self.base_ref.get() or {}
        user_todos = []
        
        # Filter todos by user_id
        for id, todo_data in data.items():
            if todo_data.get('user_id') == user_id:
                todo_data['id'] = id
                user_todos.append(self.model_class(**todo_data))
        
        # Apply pagination
        return user_todos[skip:skip+limit]


class CaseStudyFirebaseRepository(FirebaseRepository):
    """Repository for Case Study operations with Firebase"""
    
    def __init__(self, model_class):
        super().__init__(model_class, 'case_studies')
    
    def get_by_user(self, user_id: str, case_study_id: str) -> Optional[T]:
        """Get a case study that belongs to a specific user"""
        case_study = self.get(case_study_id)
        if case_study and case_study.user_id == user_id:
            return case_study
        return None
    
    def get_multi_by_user(self, user_id: str, skip: int = 0, limit: int = 100) -> List[T]:
        """Get all case studies for a specific user"""
        data = self.base_ref.get() or {}
        user_case_studies = []
        
        # Filter case studies by user_id
        for id, case_study_data in data.items():
            if case_study_data.get('user_id') == user_id:
                case_study_data['id'] = id
                user_case_studies.append(self.model_class(**case_study_data))
        
        # Apply pagination
        return user_case_studies[skip:skip+limit]


class GuesstimateFirebaseRepository(FirebaseRepository):
    """Repository for Guesstimate operations with Firebase"""
    
    def __init__(self, model_class):
        super().__init__(model_class, 'guesstimates')
    
    def get_by_user(self, user_id: str, guesstimate_id: str) -> Optional[T]:
        """Get a guesstimate that belongs to a specific user"""
        guesstimate = self.get(guesstimate_id)
        if guesstimate and guesstimate.user_id == user_id:
            return guesstimate
        return None
    
    def get_multi_by_user(self, user_id: str, skip: int = 0, limit: int = 100) -> List[T]:
        """Get all guesstimates for a specific user"""
        data = self.base_ref.get() or {}
        user_guesstimates = []
        
        # Filter guesstimates by user_id
        for id, guesstimate_data in data.items():
            if guesstimate_data.get('user_id') == user_id:
                guesstimate_data['id'] = id
                user_guesstimates.append(self.model_class(**guesstimate_data))
        
        # Apply pagination
        return user_guesstimates[skip:skip+limit] 