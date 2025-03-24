from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config import ApiConfig


def setup_fastapi(api: ApiConfig) -> FastAPI:
    app = FastAPI(
        title = api.project_name
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins = api.allow_origins,
        allow_methods = api.allow_methods,
        allow_headers = api.allow_headers,
        allow_credentials = api.allow_credentials
    )

    return app