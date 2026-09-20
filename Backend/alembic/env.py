"""Entorno de migraciones de Alembic.

La URL de conexión se toma de app.core.config.settings tanto en modo online
como offline, para que `alembic upgrade head --sql` conozca el dialecto.
"""

from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool

# Importar todos los modelos para poblar Base.metadata.
import app.games.models  # noqa: F401,E402
import app.lists.models  # noqa: F401,E402
import app.ratings.models  # noqa: F401,E402
import app.reviews.models  # noqa: F401,E402
import app.users.models  # noqa: F401,E402
from alembic import context
from app.core.config import settings
from app.core.db import Base  # noqa: E402

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

config.set_main_option("sqlalchemy.url", settings.database_url)

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()