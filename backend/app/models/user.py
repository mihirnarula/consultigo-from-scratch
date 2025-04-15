from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, index=True)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    
    # Relationships
    todos = relationship("Todo", back_populates="user", cascade="all, delete-orphan")
    guesstimates = relationship("Guesstimate", back_populates="user", cascade="all, delete-orphan")

    def __str__(self):
        return self.email 