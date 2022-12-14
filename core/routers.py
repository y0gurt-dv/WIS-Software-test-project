from fastapi import FastAPI

from views.author import router as authors_router
from views.book import router as book_router
from views.dicts import router as dict_router

ROUTERS = {
    'dicts': dict_router,
    'authors': authors_router,
    'books': book_router,
}


def connect_all_routers(app: FastAPI) -> FastAPI:
    for prefix, router in ROUTERS.items():
        app.include_router(
            router,
            prefix='/%s' % prefix,
            tags=[prefix.capitalize()]
        )
    return app
