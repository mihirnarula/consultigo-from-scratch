from app.core.config import settings

# Define lazy loading functions for conditional imports
def get_user_crud():
    if settings.USE_FIREBASE:
        # Use Firebase implementations
        from app.crud.firebase_user import firebase_user
        return firebase_user
    else:
        # Use SQLAlchemy implementations
        from app.crud.user import user
        return user

def get_todo_crud():
    if settings.USE_FIREBASE:
        # Use Firebase implementations
        from app.crud.firebase_todo import firebase_todo
        return firebase_todo
    else:
        # Use SQLAlchemy implementations
        from app.crud.todo import todo
        return todo

def get_guesstimate_crud():
    if settings.USE_FIREBASE:
        # Use Firebase implementations
        from app.crud.firebase_guesstimate import firebase_guesstimate
        return firebase_guesstimate
    else:
        # Use SQLAlchemy implementations
        from app.crud.guesstimate import guesstimate
        return guesstimate

# Export CRUD objects via properties
class LazyLoader:
    @property
    def user(self):
        return get_user_crud()
        
    @property
    def todo(self):
        return get_todo_crud()
        
    @property
    def guesstimate(self):
        return get_guesstimate_crud()

# Create singleton instance
_instance = LazyLoader()

# Export properties
user = _instance.user
todo = _instance.todo
guesstimate = _instance.guesstimate 