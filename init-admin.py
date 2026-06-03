"""Скрипт создания первого администратора."""
import asyncio
from app.core.config import get_settings
from app.core.jwt import get_password_hash
from app.infrastructure.models import UserModel
from app.infrastructure.database import async_session_maker
from sqlalchemy import select

settings = get_settings()

async def init():
    async with async_session_maker() as s:
        r = await s.execute(select(UserModel).where(UserModel.username == settings.admin_username))
        if not r.scalar_one_or_none():
            s.add(UserModel(
                email=settings.admin_email,
                username=settings.admin_username,
                hashed_password=get_password_hash(settings.admin_password),
                is_active=True,
                is_superuser=True,
            ))
            await s.commit()
            print(f'=== Admin "{settings.admin_username}" created! ===')
        else:
            print(f'=== Admin "{settings.admin_username}" already exists ===')

asyncio.run(init())
