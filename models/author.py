import sqlalchemy as db

from core.db import BaseModel


class Author(BaseModel):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)

    birthday = db.Column(db.Date)
    deathday = db.Column(db.Date, nullable=True)
