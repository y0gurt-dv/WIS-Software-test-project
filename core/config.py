from fastapi import FastAPI

from core.routers import connect_all_routers


def get_app() -> FastAPI:
    app = FastAPI()
    app = connect_all_routers(app)
    return app
