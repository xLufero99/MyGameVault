"""Configuración de la aplicación vía pydantic-settings.

Los valores se leen de variables de entorno y del fichero `.env` de la raíz
del backend (NFR-08: secretos fuera del código fuente). En CI/test los tests
inyectan variables de entorno antes de importar la app, así no dependen de un
`.env` real (NFR-13).
"""

from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_ROOT = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=PROJECT_ROOT / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    database_url: str
    jwt_secret: str
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 60


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()