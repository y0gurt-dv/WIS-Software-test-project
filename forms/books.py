from typing import List, Optional

from fastapi import HTTPException
from pydantic import BaseModel, validator
from starlette import status

from forms.authors import AuthorListForm
from forms.dicts import BaseDictForm


class BookListForm(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    publication_year: int

    authors: Optional[List[AuthorListForm]]
    genres: Optional[List[BaseDictForm]]
    types: Optional[List[BaseDictForm]]
    countries: Optional[List[BaseDictForm]]

    class Config:
        orm_mode = True


class BookCreateForm(BaseModel):
    title: str
    description: Optional[str] = None
    publication_year: int

    authors: List[int]
    genres: Optional[List[str]]
    types: Optional[List[str]]
    countries: Optional[List[str]]

    @validator('publication_year')
    def publication_year_check(cls, v):
        if v <= 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Invalid publication year'
            )
        return v

    class Config:
        orm_mode = True


class BookUpdateForm(BaseModel):
    title: Optional[str]
    description: Optional[str]
    publication_year: Optional[int]

    authors: Optional[List[int]]
    genres: Optional[List[str]]
    types: Optional[List[str]]
    countries: Optional[List[str]]

    @validator('publication_year')
    def publication_year_check(cls, v):
        if v <= 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Invalid publication year'
            )
        return v

    class Config:
        orm_mode = True


class BookForFilters(BaseModel):
    title: Optional[str]
    description: Optional[str]
    before_publication_year: Optional[int]
    after_publication_year: Optional[int]

    authors: Optional[str]
    genres: Optional[str]
    types: Optional[str]
    countries: Optional[str]
