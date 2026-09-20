"""Capa de acceso a datos: engine, sesiones y Base declarativa.

El repositorio es la única capa que conoce la base de datos (ver
architecture-components.puml). Se usa SQLAlchemy 2.x en modo síncrono: la
BD es PostgreSQL y los endpoints de FastAPI se ejecutan sobre el threadpool,
suficiente para el alcance del proyecto.
"""

from collections.abc import Iterator

from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.core.config import settings

# Naming convention explícita: las constraints/índices generados por SQLAlchemy
# reciben nombres estables (pk_/fk_/uq_/ck_/ix_), lo que evita falsos diffs
# en `alembic check` entre el modelo y la BD.
NAMING_CONVENTION: dict[str, str] = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

engine = create_engine(settings.database_url)

SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


class Base(DeclarativeBase):
    metadata = MetaData(naming_convention=NAMING_CONVENTION)


def get_db() -> Iterator[Session]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()