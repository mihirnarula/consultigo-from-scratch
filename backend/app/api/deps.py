from typing import Generator, Optional, Union

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.session import SessionLocal
from app.models.user import User as SQLUser
from app.models.firebase_models import FirebaseUser
from app.schemas.token import TokenPayload

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/auth/login"
)

# Database dependencies
def get_db() -> Generator:
    """Get SQLAlchemy database session"""
    if settings.USE_FIREBASE:
        # For Firebase, this is a no-op since we don't need a DB session
        yield None
    else:
        try:
            db = SessionLocal()
            yield db
        finally:
            db.close()

# User dependencies
def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(reusable_oauth2)
) -> Union[SQLUser, FirebaseUser]:
    """Get current user from token"""
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    
    # Get user based on database type
    if settings.USE_FIREBASE:
        from app.crud.firebase_user import firebase_user
        user = firebase_user.get(token_data.sub)
    else:
        user = db.query(SQLUser).filter(SQLUser.id == token_data.sub).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def get_current_active_user(
    current_user: Union[SQLUser, FirebaseUser] = Depends(get_current_user),
) -> Union[SQLUser, FirebaseUser]:
    """Get current active user"""
    if settings.USE_FIREBASE:
        from app.crud.firebase_user import firebase_user
        if not firebase_user.is_active(current_user):
            raise HTTPException(status_code=400, detail="Inactive user")
    else:
        if not current_user.is_active:
            raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

def get_current_active_superuser(
    current_user: Union[SQLUser, FirebaseUser] = Depends(get_current_user),
) -> Union[SQLUser, FirebaseUser]:
    """Get current active superuser"""
    if settings.USE_FIREBASE:
        from app.crud.firebase_user import firebase_user
        if not firebase_user.is_superuser(current_user):
            raise HTTPException(
                status_code=400, detail="The user doesn't have enough privileges"
            )
    else:
        if not current_user.is_superuser:
            raise HTTPException(
                status_code=400, detail="The user doesn't have enough privileges"
            )
    return current_user 