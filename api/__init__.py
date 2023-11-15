from fastapi import APIRouter

from .controller import generic_controller

api_router = APIRouter()
api_router.include_router(generic_controller)
