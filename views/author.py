from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi_pagination import Page, paginate
from starlette import status

from core.db import connect_db
from forms import authors as forms
from models.author import Author
from services.author import check_name

router = APIRouter()


@router.get('/', response_model=Page[forms.AuthorListForm])
def list_authors(database=Depends(connect_db)):
    return paginate(database.query(Author).all())


@router.post('/', response_model=forms.AuthorListForm)
def create_author(form: forms.AuthorCreateForm, database=Depends(connect_db)):
    new_author = Author(**form.dict())
    database.add(new_author)
    database.commit()

    return new_author


@router.patch('/{pk}/', response_model=forms.AuthorListForm)
def update_author(pk: int,
                  form: forms.AuthorUpdateForm,
                  database=Depends(connect_db)):
    author: Optional[Author] = database.get(Author, pk)

    if not author:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Author with this id does not exist',
        )

    if (not form.birthday and form.deathday
            and form.deathday >= author.birthday):

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Вeathday cannot be greater than or equal to birthday'
        )

    if not form.first_name and form.last_name:
        check_name(
            first_name=author.first_name,
            last_name=form.last_name,
            database=database
        )

    if not form.last_name and form.first_name:
        check_name(
            first_name=form.first_name,
            last_name=author.last_name,
            database=database
        )

    new_values = form.dict(exclude_none=True)

    for field, new_value in new_values.items():
        setattr(author, field, new_value)

    database.commit()

    return author


@router.delete('/{pk}/', status_code=status.HTTP_204_NO_CONTENT)
def delete_author(pk: int, database=Depends(connect_db)):
    author: Optional[Author] = database.get(Author, pk)

    if not author:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Author with this id does not exist',
        )

    database.delete(author)
    database.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
