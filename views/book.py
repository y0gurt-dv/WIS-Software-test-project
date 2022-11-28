from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi_pagination import Page, paginate
from starlette import status

from core.db import connect_db
from forms import books as forms
from models.book import Book
from services.book import filter_books, validate_book_form

router = APIRouter()


@router.get('/', response_model=Page[forms.BookListForm])
def list_books(database=Depends(connect_db),
               book_filters=Depends(forms.BookForFilters)):

    return paginate(filter_books(book_filters, database))


@router.post('/', response_model=forms.BookListForm)
def create_book(form: forms.BookCreateForm, database=Depends(connect_db)):
    form = validate_book_form(form, database=database)
    book = Book(**form.dict())
    database.add(book)
    database.commit()

    return book


@router.delete('/{pk}/', status_code=status.HTTP_204_NO_CONTENT)
def delete_book(pk: int, database=Depends(connect_db)):
    book = database.get(Book, pk)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Book with this id does not exist',
        )

    database.delete(book)
    database.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch('/{pk}/', response_model=forms.BookListForm)
def update_book(pk: int,
                form: forms.BookUpdateForm,
                database=Depends(connect_db)):
    book = database.get(Book, pk)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Book with this id does not exist',
        )
    form = validate_book_form(form, database=database)
    new_values = form.dict(exclude_none=True)

    for field, new_value in new_values.items():
        setattr(book, field, new_value)

    database.commit()
    return book
