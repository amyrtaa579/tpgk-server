
# Anmicius API

FastAPI backend для управления контентом колледжа с поддержкой PostgreSQL, Redis и MinIO.

## 🚀 Возможности

- **Управление контентом**: новости, специальности, FAQ, документы
- **Приёмная кампания**: информация о поступлении, подача документов
- **Профориентационный тест**: интерактивный тест для абитуриентов
- **Админ-панель**: полный CRUD для всех сущностей
- **Кэширование**: Redis для ускорения ответов
- **Файловое хранилище**: MinIO (S3-compatible) для изображений и документов
- **Аутентификация**: JWT tokens с ролевой моделью

## 📋 Требования

- Python 3.11+
- PostgreSQL 15+
- Redis 7+
- MinIO (опционально)

## 🔧 Установка

### 1. Клонирование репозитория

```bash
git clone https://github.com/yourusername/tpgk_api.git
cd tpgk_api
```

### 2. Создание виртуального окружения

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Настройка окружения

```bash
cp .env.example .env
# Отредактируйте .env с вашими настройками
```

### 5. Применение миграций

```bash
alembic upgrade head
```

### 6. Создание администратора

```bash
python init-admin.py
```

### 7. Запуск сервера

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

API будет доступен по адресу: http://localhost:8000
Документация Swagger: http://localhost:8000/docs

## 📚 API Endpoints

### Публичные endpoints
- `GET /api/v1/about` - Информация о колледже
- `GET /api/v1/specialties` - Список специальностей
- `GET /api/v1/news` - Список новостей
- `GET /api/v1/faq` - Часто задаваемые вопросы
- `GET /api/v1/test/questions` - Вопросы профориентационного теста

### Admin endpoints (требуют аутентификацию)
- `POST /api/v1/auth/login` - Вход в систему
- `GET /api/v1/admin/users` - Список пользователей
- `POST /api/v1/admin/news` - Создание новости
- `PUT /api/v1/admin/news/{id}` - Обновление новости
- `DELETE /api/v1/admin/news/{id}` - Удаление новости

Полная документация: http://localhost:8000/docs

## 🗄️ Структура проекта

```
app/
├── core/              # Конфигурация, исключения, JWT
├── domain/            # Бизнес-модели
├── application/       # Use cases
├── infrastructure/    # БД, кэш, MinIO, репозитории
└── presentation/      # HTTP роуты, схемы
```

## 🧪 Тестирование

```bash
pytest
```

## 📝 Лицензия

MIT
