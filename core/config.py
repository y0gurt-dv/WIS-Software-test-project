from fastapi import FastAPI
from starlette.config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


config = Config('.env')

DATABASE_URL = 'postgresql://{user}:{password}@{ip}:{port}/{db_name}'.format(
    user=config('DB_USER', cast=str, default='postgres'),
    password=config('DB_PASSWORD', cast=str, default='root'),
    ip=config('DB_HOST', cast=str, default='localhost'),
    port=config('DB_PORT', cast=str, default='5435'),
    db_name=config('DB_NAME', cast=str),
)


def get_app() -> FastAPI:
    app = FastAPI()
    return app

def connect_db():
    engine = create_engine(DATABASE_URL)
    session = Session(bind=engine)
    return session
 
