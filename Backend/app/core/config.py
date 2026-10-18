"""Configuración de la aplicación vía pydantic-settings.

Los valores se leen de variables de entorno y del fichero `.env` de la raíz
del backend (NFR-08: secretos fuera del código fuente). En CI/test los tests
inyectan variables de entorno antes de importar la app, así no dependen de un
`.env` real (NFR-13).
"""

from functools import lru_cache
from urllib.parse import quote_plus

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    supabase_project_ref: str
    supabase_db_password: str
    supabase_url: str
    supabase_secret_key: str
    supabase_pooler_region: str = "us-east-1"

    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 60
    allowed_origins: str = "http://localhost:5173"

    @property
    def database_url(self) -> str:
        password = quote_plus(self.supabase_db_password)
        return (
            f"postgresql+psycopg://postgres.{self.supabase_project_ref}:{password}"
            f"@aws-0-{self.supabase_pooler_region}.pooler.supabase.com:6543/postgres"
        )

    @property
    def jwt_secret(self) -> str:
        return self.supabase_secret_key


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
