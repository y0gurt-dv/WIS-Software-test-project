from core import BaseModel
from sqlalchemy import Column, String

class Country(BaseModel):
    __tablename__ = 'countries'

    slug = Column(String, primary_key=True, unique=True)
    name = Column(String)
