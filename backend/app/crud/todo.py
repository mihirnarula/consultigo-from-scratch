from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.crud.base import CRUDBase
from app.models.todo import Todo
from app.schemas.todo import TodoCreate, TodoUpdate

class CRUDTodo(CRUDBase[Todo, TodoCreate, TodoUpdate]):
    def get_multi_by_user(
        self, db: Session, *, user_id: int, skip: int = 0, limit: int = 100
    ) -> List[Todo]:
        try:
            return (
                db.query(self.model)
                .filter(Todo.user_id == user_id)
                .offset(skip)
                .limit(limit)
                .all()
            )
        except SQLAlchemyError:
            db.rollback()
            raise

    def get_by_user(
        self, db: Session, *, user_id: int, todo_id: int
    ) -> Optional[Todo]:
        try:
            return (
                db.query(self.model)
                .filter(Todo.user_id == user_id, Todo.id == todo_id)
                .first()
            )
        except SQLAlchemyError:
            db.rollback()
            raise

    def create_with_user(
        self, db: Session, *, obj_in: TodoCreate, user_id: int
    ) -> Todo:
        try:
            obj_in_data = obj_in.dict()
            db_obj = self.model(**obj_in_data, user_id=user_id)
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
            return db_obj
        except SQLAlchemyError:
            db.rollback()
            raise

todo = CRUDTodo(Todo) 