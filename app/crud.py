from app.models import users, authors, books
from app.auth import get_password_hash
from app.database import database

async def create_user(username: str, password: str):
    hashed = get_password_hash(password)
    query = users.insert().values(username=username, hashed_password=hashed)
    return await database.execute(query)

async def create_author(name: str):
    query = authors.insert().values(name=name)
    return await database.execute(query)

async def get_authors():
    query = authors.select()
    return await database.fetch_all(query)

async def create_book(title: str, author_id: int):
    query = books.insert().values(title=title, author_id=author_id)
    return await database.execute(query)

async def get_books():
    query = books.select()
    return await database.fetch_all(query)
