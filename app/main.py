from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.database import database, engine, metadata
from app import schemas, crud, auth
from app.models import users, authors, books

app = FastAPI()

metadata.create_all(engine)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/auth/register", status_code=201)
async def register(user: schemas.UserCreate):
    return await crud.create_user(user.username, user.password)

@app.post("/auth/token", response_model=schemas.Token)
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user = await auth.authenticate_user(form.username, form.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect credentials")
    token = auth.create_access_token({"sub": user["username"]})
    return {"access_token": token, "token_type": "bearer"}

@app.post("/authors/", status_code=201)
async def add_author(author: schemas.AuthorCreate, user=Depends(auth.get_current_user)):
    id = await crud.create_author(author.name)
    return {"id": id, "name": author.name}

@app.get("/authors/", response_model=list[schemas.Author])
async def list_authors():
    return await crud.get_authors()

@app.post("/books/", status_code=201)
async def add_book(book: schemas.BookCreate, user=Depends(auth.get_current_user)):
    id = await crud.create_book(book.title, book.author_id)
    return {"id": id, "title": book.title, "author_id": book.author_id}

@app.get("/books/", response_model=list[schemas.Book])
async def list_books():
    return await crud.get_books()
