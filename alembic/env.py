"""Alembic environment configuration."""

from logging.config import fileConfig

from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config

from alembic import context

from app.infrastructure.database import Base
from app.infrastructure.models import (
    SpecialtyModel,
    InterestingFactModel,
    NewsModel,
    FAQModel,
    DocumentModel,
    GalleryImageModel,
    DocumentFileModel,
    TestQuestionModel,
    AboutInfoModel,
    AdmissionInfoModel,
    UserModel,
    RefreshTokenModel,
)

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
target_metadata = Base.metadata


def get_url():
    """Get database URL from environment or config."""
    import os
    from app.core.config import get_settings

    # Сначала пробуем получить из переменной окружения
    url = os.getenv("DATABASE_URL")
    if url:
        return url

    # Если нет, используем настройки приложения
    try:
        settings = get_settings()
        return settings.database_url
    except Exception:
        # Fallback на стандартный URL (для совместимости)
        return "postgresql+asyncpg://anmicius:anmicius_secret_password@postgres:5432/anmicius_db"


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""

    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        render_as_batch=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        render_as_batch=True,
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations() -> None:
    """Run migrations in 'online' mode with async engine."""
    from app.infrastructure.database import engine

    async with engine.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await engine.dispose()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    import asyncio
    asyncio.run(run_async_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
