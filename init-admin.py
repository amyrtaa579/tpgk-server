"""Скрипт создания первого администратора."""
import asyncio
from app.core.config import get_settings
from app.core.jwt import get_password_hash
from app.infrastructure.models import UserModel
from app.infrastructure.database import async_session_maker
from sqlalchemy import select, or_

settings = get_settings()

async def init():
    async with async_session_maker() as s:
        # Проверяем существование пользователя по email ИЛИ username
        r = await s.execute(
            select(UserModel).where(
                or_(
                    UserModel.email == settings.admin_email,
                    UserModel.username == settings.admin_username
                )
            )
        )
        existing = r.scalars().first()
        
        if existing:
            print(f'=== Пользователь уже существует: {existing.username} ({existing.email}) ===')
            # Обновляем пароль и права если нужно
            existing.hashed_password = get_password_hash(settings.admin_password)
            existing.is_active = True
            existing.is_superuser = True
            await s.commit()
            print(f'=== Пароль и права обновлены ===')
        else:
            s.add(UserModel(
                email=settings.admin_email,
                username=settings.admin_username,
                hashed_password=get_password_hash(settings.admin_password),
                is_active=True,
                is_superuser=True,
            ))
            await s.commit()
            print(f'=== Admin "{settings.admin_username}" создан! ===')

asyncio.run(init())
