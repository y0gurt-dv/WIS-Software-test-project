from core import BaseModel
from sqlalchemy import Column, String

class Genre(BaseModel):
    __tablename__ = 'genres'

    slug = Column(String, primary_key=True, unique=True)
    name = Column(String)
