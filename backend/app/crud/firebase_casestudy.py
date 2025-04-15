from typing import Optional, Dict, Any, List, Union
from datetime import datetime

from app.db.firebase_repository import CaseStudyFirebaseRepository
from app.models.firebase_models import FirebaseCaseStudy
from app.schemas.casestudy import CaseStudyCreate, CaseStudyUpdate

class CRUDFirebaseCaseStudy:
    def __init__(self):
        self.repository = CaseStudyFirebaseRepository(FirebaseCaseStudy)
    
    def get(self, id: str) -> Optional[FirebaseCaseStudy]:
        """Get case study by ID"""
        return self.repository.get(id)
    
    def get_multi(self, skip: int = 0, limit: int = 100) -> List[FirebaseCaseStudy]:
        """Get multiple case studies with pagination"""
        return self.repository.get_multi(skip, limit)
    
    def get_multi_by_user(self, user_id: str, skip: int = 0, limit: int = 100) -> List[FirebaseCaseStudy]:
        """Get case studies for a specific user"""
        return self.repository.get_multi_by_user(user_id, skip, limit)
    
    def get_by_user(self, user_id: str, case_study_id: str) -> Optional[FirebaseCaseStudy]:
        """Get a case study for a specific user"""
        return self.repository.get_by_user(user_id, case_study_id)
    
    def create(self, obj_in: CaseStudyCreate) -> FirebaseCaseStudy:
        """Create a new case study"""
        data = obj_in.dict()
        return self.repository.create(data)
    
    def create_with_user(self, obj_in: CaseStudyCreate, user_id: str) -> FirebaseCaseStudy:
        """Create a new case study with user_id"""
        data = obj_in.dict()
        data["user_id"] = user_id
        return self.repository.create(data)
    
    def update(self, id: str, obj_in: Union[CaseStudyUpdate, Dict[str, Any]]) -> Optional[FirebaseCaseStudy]:
        """Update a case study"""
        if isinstance(obj_in, CaseStudyUpdate):
            update_data = obj_in.dict(exclude_unset=True)
        else:
            update_data = obj_in
        
        return self.repository.update(id, update_data)
    
    def remove(self, id: str) -> bool:
        """Delete a case study"""
        return self.repository.delete(id)

firebase_casestudy = CRUDFirebaseCaseStudy() 