from fastapi.testclient import TestClient
from app.main import app
import pytest
from app.models import users
from app.database import database

client = TestClient(app)

@pytest.fixture(scope="function", autouse=True)
async def clear_users():
    query = users.test.db.delete()  # Очищаем таблицу users
    await database.execute(query)


def test_register_and_login(client):
    username = generate_random_username()  # Генерируем уникальное имя
    response = client.post("/auth/register", json={"username": username, "password": "1234"})
    assert response.status_code == 200


def test_register_and_login():
    client.post("/auth/register", json={"username": "2", "password": "1234"})
    response = client.post("/auth/token", data={"username": "2", "password": "1234"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_author_book_flow():
    client.post("/auth/register", json={"username": "1", "password": "1234"})
    token = client.post("/auth/token", data={"username": "1", "password": "1234"}).json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    response = client.post("/authors/", json={"name": "Author1"}, headers=headers)
    assert response.status_code == 201
    author_id = response.json()["id"]

    response = client.post("/books/", json={"title": "Book1", "author_id": author_id}, headers=headers)
    assert response.status_code == 201
