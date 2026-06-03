"""Конфигурация приложения."""
from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Настройки приложения."""

    # Application
    app_name: str = "Anmicius API"
    app_version: str = "1.0.0"
    debug: bool = False
    environment: str = "production"

    # Database
    postgres_user: str = ""
    postgres_password: str = ""
    postgres_db: str = ""
    postgres_host: str = "localhost"
    postgres_port: int = 5432

    @property
    def database_url(self) -> str:
        return f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"

    # MinIO
    minio_endpoint: str = ""
    minio_access_key: str = ""
    minio_secret_key: str = ""
    minio_bucket: str = "anmicius-media"
    minio_secure: bool = False
    minio_public_url: str = ""

    # Redis
    redis_host: str = "localhost"
    redis_port: int = 6379
    redis_db: int = 0
    redis_password: str | None = None
    redis_ttl_default: int = 300
    redis_ttl_long: int = 3600

    # CORS
    cors_origins: str = "http://localhost:3000,http://localhost:8000"

    @property
    def get_cors_origins(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",")]

    # API
    api_v1_prefix: str = "/api/v1"

    # JWT
    jwt_secret_key: str = ""
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 30
    jwt_refresh_token_expire_days: int = 30

    # Rate limiting
    rate_limit_default: str = "100/minute"

    # Pagination
    pagination_min_limit: int = 1
    pagination_max_limit: int = 100
    pagination_default_limit: int = 10

    # Admin (для init-admin.py)
    admin_email: str = "admin@example.com"
    admin_username: str = "admin"
    admin_password: str = "changeme"

    class Config:
        env_file = ".env"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    """Получить настройки приложения."""
    return Settings()
