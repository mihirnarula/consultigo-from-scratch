from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class Todo(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    is_completed = Column(Boolean, default=False)
    
    # Foreign key to User
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user = relationship("User", back_populates="todos")

    def __str__(self) -> str:
        return f"Todo(id={self.id}, title={self.title})" 