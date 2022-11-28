from sqlalchemy import Column, String

from core.db import BaseModel


class Genre(BaseModel):
    __tablename__ = 'genres'

    slug = Column(String, primary_key=True, unique=True)
    name = Column(String)
