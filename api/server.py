from fastapi import FastAPI
from api import api_router, __version__


def create_api() -> FastAPI:

    api = FastAPI(
        title="Docker API",
        version=__version__,
        description="This API has to finish in a Docker container",
        docs_url=None,
        redoc_url=None,
    )

    api.include_router(api_router)

    return api
