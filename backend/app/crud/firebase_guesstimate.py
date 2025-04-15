from typing import Optional, Dict, Any, List, Union
from datetime import datetime

from app.db.firebase_repository import GuesstimateFirebaseRepository
from app.models.firebase_models import FirebaseGuesstimate
from app.schemas.guesstimate import GuesstimateCreate, GuesstimateUpdate

class CRUDFirebaseGuesstimate:
    def __init__(self):
        self.repository = GuesstimateFirebaseRepository(FirebaseGuesstimate)
    
    def get(self, id: str) -> Optional[FirebaseGuesstimate]:
        """Get guesstimate by ID"""
        return self.repository.get(id)
    
    def get_multi(self, skip: int = 0, limit: int = 100) -> List[FirebaseGuesstimate]:
        """Get multiple guesstimates with pagination"""
        return self.repository.get_multi(skip, limit)
    
    def get_multi_by_user(self, user_id: str, skip: int = 0, limit: int = 100) -> List[FirebaseGuesstimate]:
        """Get guesstimates for a specific user"""
        return self.repository.get_multi_by_user(user_id, skip, limit)
    
    def get_by_user(self, user_id: str, guesstimate_id: str) -> Optional[FirebaseGuesstimate]:
        """Get a guesstimate for a specific user"""
        return self.repository.get_by_user(user_id, guesstimate_id)
    
    def create(self, obj_in: GuesstimateCreate) -> FirebaseGuesstimate:
        """Create a new guesstimate"""
        data = obj_in.dict()
        return self.repository.create(data)
    
    def create_with_user(self, obj_in: GuesstimateCreate, user_id: str) -> FirebaseGuesstimate:
        """Create a new guesstimate with user_id"""
        data = obj_in.dict()
        data["user_id"] = user_id
        return self.repository.create(data)
    
    def update(self, id: str, obj_in: Union[GuesstimateUpdate, Dict[str, Any]]) -> Optional[FirebaseGuesstimate]:
        """Update a guesstimate"""
        if isinstance(obj_in, GuesstimateUpdate):
            update_data = obj_in.dict(exclude_unset=True)
        else:
            update_data = obj_in
        
        return self.repository.update(id, update_data)
    
    def remove(self, id: str) -> bool:
        """Delete a guesstimate"""
        return self.repository.delete(id)

firebase_guesstimate = CRUDFirebaseGuesstimate() 