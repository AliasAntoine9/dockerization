from fastapi.routing import APIRouter

generic_controller = APIRouter()


@generic_controller.get("/")
def read_root():
    return "Hello World"
