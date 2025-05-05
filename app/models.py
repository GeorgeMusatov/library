from sqlalchemy import Table, Column, Integer, String, ForeignKey
from app.database import metadata

users = Table(
    "users", metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("username", String, unique=True, index=True),
    Column("hashed_password", String),
)

authors = Table(
    "authors", metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, unique=True),
)

books = Table(
    "books", metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("author_id", Integer, ForeignKey("authors.id")),
)
