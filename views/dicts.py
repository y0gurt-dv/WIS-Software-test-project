from fastapi import APIRouter, Depends, Response
from fastapi_pagination import Page, paginate
from starlette import status

from core.db import connect_db
from forms.dicts import BaseDictForm
from models.book_type import BookType
from models.country import Country
from models.genre import Genre
from services.dicts import check_exist_slug

router = APIRouter()


def _base_dict_create(model, form, database):
    check_exist_slug(
        model=model,
        slug=form.slug,
        database=database,
        exist_raise_exception=True,
    )

    new_obj = model(**form.dict())
    database.add(new_obj)
    database.commit()
    return form


def _base_dict_delete(model, slug, database):
    obj = check_exist_slug(
        model=model,
        slug=slug,
        database=database,
        not_exist_raise_exception=True,
    )
    obj.books = []

    database.delete(obj)
    database.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get('/genres/', response_model=Page[BaseDictForm])
def genres_list(database=Depends(connect_db)):
    return paginate(database.query(Genre).all())


@router.post('/genre/', response_model=BaseDictForm)
def create_genre(form: BaseDictForm, database=Depends(connect_db)):
    return _base_dict_create(
        model=Genre,
        form=form,
        database=database,
    )


@router.delete('/genre/{slug}/', status_code=status.HTTP_204_NO_CONTENT)
def delete_genre(slug: str, database=Depends(connect_db)):
    return _base_dict_delete(
        model=Genre,
        slug=slug,
        database=database
    )


@router.get('/book-types/', response_model=Page[BaseDictForm])
def book_types_list(database=Depends(connect_db)):
    return paginate(database.query(BookType).all())


@router.post('/book-type/', response_model=BaseDictForm)
def create_book_type(form: BaseDictForm, database=Depends(connect_db)):
    return _base_dict_create(
        model=BookType,
        form=form,
        database=database,
    )


@router.delete('/book-type/{slug}/', status_code=status.HTTP_204_NO_CONTENT)
def delete_book_type(slug: str, database=Depends(connect_db)):
    return _base_dict_delete(
        model=BookType,
        slug=slug,
        database=database
    )


@router.get('/countries/', response_model=Page[BaseDictForm])
def countries_list(database=Depends(connect_db)):
    return paginate(database.query(Country).all())


@router.post('/country/', response_model=BaseDictForm)
def create_country(form: BaseDictForm, database=Depends(connect_db)):
    return _base_dict_create(
        model=Country,
        form=form,
        database=database,
    )


@router.delete('/country/{slug}/', status_code=status.HTTP_204_NO_CONTENT)
def delete_country(slug: str, database=Depends(connect_db)):
    return _base_dict_delete(
        model=Country,
        slug=slug,
        database=database
    )
