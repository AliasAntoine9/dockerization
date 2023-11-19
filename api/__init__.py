from fastapi import APIRouter

from .controller import generic_controller

api_router = APIRouter()
api_router.include_router(generic_controller)

__version__ = "1.0.0"
__app_name__ = "dockerization"
