import sqlalchemy as db
from sqlalchemy.orm import relationship

from core.db import BaseModel

book_authors = db.Table(
    'book_authors',
    BaseModel.metadata,
    db.Column('book_id', db.Integer, db.ForeignKey('books.id')),
    db.Column('author_id', db.Integer, db.ForeignKey('authors.id')),
)

book_genres = db.Table(
    'book_genres',
    BaseModel.metadata,
    db.Column('book_id', db.Integer, db.ForeignKey('books.id')),
    db.Column('genre_slug', db.String, db.ForeignKey('genres.slug')),
)

book_book_types = db.Table(
    'book_book_types',
    BaseModel.metadata,
    db.Column('book_id', db.Integer, db.ForeignKey('books.id')),
    db.Column('type_slug', db.String, db.ForeignKey('book_types.slug')),
)

book_countries = db.Table(
    'book_countries',
    BaseModel.metadata,
    db.Column('book_id', db.Integer, db.ForeignKey('books.id')),
    db.Column('country_slug', db.String, db.ForeignKey('countries.slug')),
)


class Book(BaseModel):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String)
    description = db.Column(db.Text, nullable=True)
    publication_year = db.Column(db.Integer)

    authors = relationship('Author', secondary=book_authors, backref='books')
    genres = relationship('Genre', secondary=book_genres, backref='books')
    types = relationship('BookType', secondary=book_book_types,
                         backref='books')
    countries = relationship('Country', secondary=book_countries,
                             backref='books')
