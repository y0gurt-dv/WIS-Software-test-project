from fastapi import HTTPException
from starlette import status

from models.author import Author
from models.book import Book
from models.book_type import BookType
from models.country import Country
from models.genre import Genre
from services.dicts import check_exist_slug

_RELATIONSHIPS_FIELDS = {
    'genres': Genre,
    'types': BookType,
    'countries': Country
}


def _validate_relationships(model, slug, database):
    obj = check_exist_slug(
        model=model,
        slug=slug,
        not_exist_raise_exception=True,
        database=database
    )
    return obj


def validate_book_title(title, database):
    check_title_book = database.query(Book).filter(
        Book.title == title
    ).one_or_none()

    if check_title_book:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Book with title "{}" already exists'.format(
                title
            )
        )


def validate_book_form(form, database):
    for field, model in _RELATIONSHIPS_FIELDS.items():
        values = getattr(form, field, [])
        if not values:
            continue

        for value_idx, value in enumerate(values):
            values[value_idx] = _validate_relationships(
                model=model,
                slug=value,
                database=database
            )
        setattr(form, field, values)

    authors = form.authors
    if authors:
        for author_id_idx, author_id in enumerate(authors):
            author = database.get(Author, author_id)
            if not author:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='Author with id "{}" not exists'.format(
                        author_id
                    )
                )
            authors[author_id_idx] = author

    title = form.title
    if title:
        validate_book_title(form.title, database)

    return form


def filter_books(filters_form, database):
    filters = []

    if filters_form.title:
        filters.append(Book.title.like(filters_form.title))

    if filters_form.description:
        filters.append(Book.description.like(filters_form.description))

    if filters_form.before_publication_year:
        filters.append(
            Book.publication_year <= filters_form.before_publication_year
        )

    if filters_form.after_publication_year:
        filters.append(
            Book.publication_year >= filters_form.after_publication_year
        )

    if filters_form.authors:
        authors_ids = map(int, filters_form.authors.split(','))
        filters.append(Book.authors.any(Author.id.in_(authors_ids)))
    if filters_form.genres:
        genres = filters_form.genres.split(',')
        filters.append(Book.genres.any(Genre.slug.in_(genres)))
    if filters_form.types:
        types = filters_form.types.split(',')
        filters.append(Book.types.any(BookType.slug.in_(types)))
    if filters_form.countries:
        countries = filters_form.countries.split(',')
        filters.append(Book.countries.any(Country.slug.in_(countries)))

    query = database.query(Book).filter(*filters).all()
    return query
