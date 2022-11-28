from fastapi import HTTPException
from starlette import status

from core.db import connect_db
from models.author import Author


def check_name(first_name, last_name, database=None, raise_exception=True):
    if not database:
        database = connect_db()

    exists_author = database.query(Author).filter(
        Author.first_name == first_name,
        Author.last_name == last_name
    ).count()

    if exists_author != 0 and raise_exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Author with this first name and last name exists'
        )

    return exists_author == 0
