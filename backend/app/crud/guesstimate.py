from typing import List, Optional, Dict, Any, Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.guesstimate import Guesstimate
from app.schemas.guesstimate import GuesstimateCreate, GuesstimateUpdate


class CRUDGuesstimate(CRUDBase[Guesstimate, GuesstimateCreate, GuesstimateUpdate]):
    def get_multi_by_user(
        self, db: Session, *, user_id: int, skip: int = 0, limit: int = 100
    ) -> List[Guesstimate]:
        """Get all guesstimates for a specific user"""
        return (
            db.query(self.model)
            .filter(Guesstimate.user_id == user_id)
            .offset(skip)
            .limit(limit)
            .all()
        )
    
    def create_with_user(
        self, db: Session, *, obj_in: GuesstimateCreate, user_id: int
    ) -> Guesstimate:
        """Create a new guesstimate with user_id"""
        obj_in_data = obj_in.dict()
        db_obj = Guesstimate(**obj_in_data, user_id=user_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


guesstimate = CRUDGuesstimate(Guesstimate) 