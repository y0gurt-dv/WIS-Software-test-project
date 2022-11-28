from fastapi import FastAPI
from fastapi_pagination import add_pagination

from core.routers import connect_all_routers


def get_app() -> FastAPI:
    app = FastAPI()
    app = connect_all_routers(app)
    add_pagination(app)
    return app
