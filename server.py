from fastapi import FastAPI

api = FastAPI(
    title="Docker API",
    description="This API has to finish in a Docker container",
    version="0.1.0",
)


@api.get("/")
def read_root():
    return "Hello World"
