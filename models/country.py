from sqlalchemy import Column, String

from core.db import BaseModel


class Country(BaseModel):
    __tablename__ = 'countries'

    slug = Column(String, primary_key=True, unique=True)
    name = Column(String)
