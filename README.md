# Anmicius API

FastAPI backend для Томского промышленно-гуманитарного колледжа (ТПГК).

## Требования

- Python 3.11+
- PostgreSQL 14+
- Redis 6+
- MinIO (опционально)

## Быстрый запуск

```bash
# 1. Клонировать репозиторий
git clone https://github.com/Anmicius/tpgk-api.git
cd tpgk-api

# 2. Создать виртуальное окружение
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

# 3. Установить зависимости
pip install -r requirements.txt

# 4. Настроить .env (скопировать из .env.example)
cp .env.example .env
# Отредактировать .env под свои сервисы

# 5. Применить миграции
alembic upgrade head

# 6. Создать администратора
python init-admin.py

# 7. Запустить
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

API: http://localhost:8000  
Swagger: http://localhost:8000/docs

## Структура

```
├── app/
│   ├── core/              # Конфигурация, JWT, исключения
│   ├── domain/            # Бизнес-модели и интерфейсы
│   ├── application/       # Use cases
│   ├── infrastructure/    # БД, Redis, MinIO, репозитории
│   └── presentation/      # Роуты и Pydantic-схемы
├── alembic/               # Миграции
├── tests/                 # Тесты
├── .env.example           # Пример переменных окружения
├── init-admin.py          # Создание админа
└── requirements.txt       # Зависимости
```

## Лицензия

MIT
