from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import SQLAlchemyError
from jose import JWTError

from app.core.config import settings
from app.db.firebase import initialize_firebase

# Initialize Firebase first if enabled
if settings.USE_FIREBASE:
    # Use Firebase
    print("Using Firebase Realtime Database")
    initialize_firebase()
    
# Now import modules that might depend on Firebase
from app.api.api import api_router
from app.db.session import SessionLocal
from app.db.base import Base

# Create database based on configuration
if not settings.USE_FIREBASE:
    # Use SQLite/PostgreSQL
    print("Using SQLAlchemy Database")
    Base.metadata.create_all(bind=SessionLocal.bind)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Error handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )

@app.exception_handler(SQLAlchemyError)
async def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
    return JSONResponse(
        status_code=500,
        content={"detail": "Database error occurred"}
    )

@app.exception_handler(JWTError)
async def jwt_exception_handler(request: Request, exc: JWTError):
    return JSONResponse(
        status_code=401,
        content={"detail": "Could not validate credentials"}
    )

# Startup and shutdown events
@app.on_event("startup")
async def startup_event():
    try:
        if not settings.USE_FIREBASE:
            # Only verify database connection for SQL databases
            # Firebase already initialized above
            db = SessionLocal()
            db.execute("SELECT 1")
            db.close()
    except Exception as e:
        print(f"Database connection failed: {e}")
        raise e

@app.on_event("shutdown")
async def shutdown_event():
    # Clean up resources if needed
    pass

# Include routers
app.include_router(api_router, prefix=settings.API_V1_STR)

# Add a test endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"} 