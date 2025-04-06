from fastapi import APIRouter

from backend.app.endpoints import nasa


api_router = APIRouter()

api_router.include_router(nasa.router)

