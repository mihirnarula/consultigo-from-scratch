from fastapi import APIRouter

from app.api.endpoints import auth, todos, users, guesstimate

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(todos.router, prefix="/todos", tags=["todos"])
api_router.include_router(guesstimate.router, prefix="/guesstimates", tags=["guesstimates"]) 