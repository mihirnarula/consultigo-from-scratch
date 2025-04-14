from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import SQLAlchemyError
from jose import JWTError

from app.api.api import api_router
from app.core.config import settings
from app.db.session import SessionLocal
from app.db.base import Base

# Create database tables
Base.metadata.create_all(bind=SessionLocal.bind)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
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
        # Verify database connection
        db = SessionLocal()
        db.execute("SELECT 1")
    except Exception as e:
        print(f"Database connection failed: {e}")
        raise e
    finally:
        db.close()

@app.on_event("shutdown")
async def shutdown_event():
    # Clean up resources if needed
    pass

# Include routers
app.include_router(api_router, prefix=settings.API_V1_STR) 