from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class AuthorCreate(BaseModel):
    name: str

class Author(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class BookCreate(BaseModel):
    title: str
    author_id: int

class Book(BaseModel):
    id: int
    title: str
    author_id: int

    class Config:
        from_attributes = True
