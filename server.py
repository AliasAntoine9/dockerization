from fastapi import FastAPI
from api import api_router


def create_api() -> FastAPI:

    api = FastAPI(
        title="Docker API",
        version="0.1.0",
        description="This API has to finish in a Docker container",
        root_path="api/v1",
        docs_url=None,
        redoc_url=None,
    )

    api.include_router(api_router)

    return api
