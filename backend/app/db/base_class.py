from typing import Any
from datetime import datetime
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import Column, DateTime

@as_declarative()
class Base:
    id: Any
    __name__: str
    
    # Add created_at and updated_at to all tables
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower() 