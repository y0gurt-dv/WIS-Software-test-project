from typing import Optional

from fastapi import HTTPException
from starlette import status

from core.db import connect_db


def check_exist_slug(model, slug: str, database=None,
                     not_exist_raise_exception=False,
                     exist_raise_exception=False):
    """
        not_exist_raise_exception - raise exception if obj with slug not exists
        exist_raise_exception - raise exception if obj with slug exists
        Else return obj or None
    """

    if not database:
        database = connect_db()

    exists_obj: Optional[model] = database.get(model, slug)

    if exist_raise_exception and exists_obj:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='%s with this slug already exists' % model.__name__
        )
    if not_exist_raise_exception and not exists_obj:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='{} with slug "{}" not exists'.format(
                model.__name__,
                slug
            )
        )

    return exists_obj
