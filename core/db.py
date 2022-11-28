from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from starlette.config import Config

BaseModel = declarative_base()
config = Config('.env')


def get_database_url():
    return 'postgresql://{user}:{password}@{ip}:{port}/{db_name}'.format(
        user=config('DB_USER', cast=str, default='postgres'),
        password=config('DB_PASSWORD', cast=str, default='root'),
        ip=config('DB_HOST', cast=str, default='localhost'),
        port=config('DB_PORT', cast=str, default='5435'),
        db_name=config('DB_NAME', cast=str),
    )


def connect_db():
    url = get_database_url()
    engine = create_engine(url)
    session = Session(bind=engine)
    return session
