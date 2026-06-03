"""
Скрипт создания первого администратора.
Данные берутся из переменных окружения.
"""
import asyncio
import os
from app.core.jwt import get_password_hash
from app.infrastructure.models import UserModel
from app.infrastructure.database import async_session_maker
from sqlalchemy import select


async def init():
    email = os.getenv("ADMIN_EMAIL", "admin@example.com")
    username = os.getenv("ADMIN_USERNAME", "admin")
    password = os.getenv("ADMIN_PASSWORD", "changeme")

    async with async_session_maker() as s:
        r = await s.execute(select(UserModel).where(UserModel.username == username))
        if not r.scalar_one_or_none():
            s.add(UserModel(
                email=email,
                username=username,
                hashed_password=get_password_hash(password),
                is_active=True,
                is_superuser=True,
            ))
            await s.commit()
            print(f'=== Admin "{username}" created! ===')
        else:
            print(f'=== Admin "{username}" already exists ===')


asyncio.run(init())
