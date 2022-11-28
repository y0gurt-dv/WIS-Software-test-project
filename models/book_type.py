from core import BaseModel
from sqlalchemy import Column, String

class BookType(BaseModel):
    __tablename__ = 'book_types'

    slug = Column(String, primary_key=True, unique=True)
    name = Column(String)
