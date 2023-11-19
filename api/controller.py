from fastapi.routing import APIRouter

generic_controller = APIRouter()


@generic_controller.get("/")
def read_root():
    return "Hello World"


@generic_controller.get("/cars/s2000")
def get_s2000_info():
    return {
        "specification": {
            "Engine name": "VTEC",
            "Cubic capacity": "2.0L",
            "Horse power": 240,
            "Production year": "1999 - 2009",
            "Type": "Convertible",
            "Price in dollars": 35000
        }
    }
