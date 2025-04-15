import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from app.core.config import settings
import os

# Track if Firebase is initialized
_firebase_initialized = False

def initialize_firebase():
    """Initialize Firebase Admin SDK and connect to Realtime Database"""
    global _firebase_initialized
    
    if _firebase_initialized:
        print("Firebase already initialized, skipping...")
        return True
        
    try:
        # Check if credentials file exists
        if not os.path.exists(settings.FIREBASE_CREDENTIALS_PATH):
            print(f"Firebase credentials file not found at: {settings.FIREBASE_CREDENTIALS_PATH}")
            return False
            
        # Fetch the service account key JSON file contents
        cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS_PATH)
        
        # Initialize the app with a service account, granting admin privileges
        try:
            firebase_admin.initialize_app(cred, {
                'databaseURL': settings.FIREBASE_DATABASE_URL
            })
        except ValueError as e:
            # If error is about app already initialized, that's okay
            if "already exists" not in str(e):
                raise
        
        # Set flag to True
        _firebase_initialized = True
        print("Firebase initialized successfully.")
        return True
    except Exception as e:
        print(f"Error initializing Firebase: {e}")
        return False

def get_ref(path):
    """Get a reference to a specific path in the Realtime Database"""
    if not _firebase_initialized:
        # Try to initialize if not already done
        if not initialize_firebase():
            raise ValueError("Firebase not initialized and initialization failed")
    return db.reference(path)

def get_users_ref():
    """Get a reference to the users collection"""
    return get_ref('users')

def get_todos_ref():
    """Get a reference to the todos collection"""
    return get_ref('todos') 