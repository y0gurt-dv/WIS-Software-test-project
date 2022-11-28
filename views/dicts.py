from typing import List

from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from core.db import connect_db
from forms.dicts import BaseDictForm
from models.book_type import BookType
from models.country import Country
from models.genre import Genre

router = APIRouter()


def _base_dict_create(model, form, database):
    exists_obj = (
        database.query(model)
        .filter(model.slug == form.slug)
        .one_or_none()
    )
    if exists_obj:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='%s with this slug already exists' % model.__name__
        )
    new_obj = model(**form.dict())
    database.add(new_obj)
    database.commit()
    return form


@router.get('/genres/', response_model=List[BaseDictForm])
def genres_list(database=Depends(connect_db)):
    return database.query(Genre).all()


@router.post('/genre/', response_model=BaseDictForm)
def create_genre(form: BaseDictForm, database=Depends(connect_db)):
    return _base_dict_create(
        model=Genre,
        form=form,
        database=database,
    )


@router.get('/book-types/', response_model=List[BaseDictForm])
def book_types_list(database=Depends(connect_db)):
    return database.query(BookType).all()


@router.post('/book-type/', response_model=BaseDictForm)
def create_book_type(form: BaseDictForm, database=Depends(connect_db)):
    return _base_dict_create(
        model=BookType,
        form=form,
        database=database,
    )


@router.get('/countries/', response_model=List[BaseDictForm])
def countries_list(database=Depends(connect_db)):
    return database.query(Country).all()


@router.post('/country/', response_model=BaseDictForm)
def create_country(form: BaseDictForm, database=Depends(connect_db)):
    return _base_dict_create(
        model=Country,
        form=form,
        database=database,
    )
