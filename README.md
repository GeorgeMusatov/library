# 📚 FastAPI Library API

Это REST API-проект на FastAPI с авторизацией, управлением пользователями, авторами и книгами. Используется PostgreSQL, SQLAlchemy, Alembic и JWT.

## 🚀 Возможности

- Регистрация и авторизация пользователей (JWT)
- CRUD для авторов и книг
- Ассоциация книг с авторами
- Защищённые эндпоинты (доступ только для авторизованных пользователей)
- Поддержка миграций через Alembic
- Покрытие тестами через Pytest + HTTPX

## 🧰 Стек

- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Pytest
- Pydantic
- JWT (Python-Jose)
- Uvicorn

## 📦 Установка и запуск

### 1. Клонируйте репозиторий

git clone https://github.com/your-username/your-repo.git
cd your-repo

### 2. Создайте и активируйте виртуальное окружение
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate для Windows
### 3. Установите зависимости
bash
Copy
Edit
pip install -r requirements.txt

### 4. Примените миграции
bash
Copy
Edit
alembic upgrade head
### 5. Запустите сервер
bash
Copy
Edit
uvicorn app.main:app --reload
### 6. Документация
Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

🧪 Запуск тестов
bash
Copy
Edit
pytest
📁 Структура проекта
bash
Copy
Edit
.
├── app/
│   ├── main.py
│   ├── models/
│   ├── schemas/
│   ├── routes/
│   ├── services/
│   ├── db/
│   └── core/
├── tests/
├── alembic/
├── .env
├── requirements.txt
└── README.md
