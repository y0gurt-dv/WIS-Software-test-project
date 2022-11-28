from datetime import date
from typing import Optional

from fastapi import HTTPException
from pydantic import BaseModel, validator
from starlette import status

from services.author import check_name


class AuthorBaseCreateUpdateForm():
    @validator('last_name')
    def name_check(cls, v, values):
        first_name = values.get('first_name')
        if first_name:
            check_name(first_name, v)

        return v

    @validator('deathday')
    def deathday_check(cls, v, values):
        birthday = values.get('birthday')
        if birthday and v >= birthday:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Вeathday cannot be greater than or equal to birthday'
            )

        return v


class AuthorCreateForm(BaseModel, AuthorBaseCreateUpdateForm):
    first_name: str
    last_name: str
    birthday: date
    deathday: Optional[date]

    class Config:
        orm_mode = True


class AuthorUpdateForm(BaseModel, AuthorBaseCreateUpdateForm):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    birthday: Optional[date] = None
    deathday: Optional[date] = None

    class Config:
        orm_mode = True


class AuthorListForm(BaseModel):
    id: int
    first_name: str
    last_name: str
    birthday: date
    deathday: Optional[date]

    class Config:
        orm_mode = True
