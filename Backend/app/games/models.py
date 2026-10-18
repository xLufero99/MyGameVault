"""Modelos del módulo games.

Incluye el catálogo de juegos (Game) y sus entidades de catálogo auxiliares,
Genre y Platform, junto con la asociación N:M games_genres.
"""

from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Index,
    Integer,
    String,
    Table,
    Text,
    UniqueConstraint,
    Uuid,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base

games_genres = Table(
    "games_genres",
    Base.metadata,
    Column("game_id", Uuid, ForeignKey("games.id"), primary_key=True),
    Column("genre_id", Uuid, ForeignKey("genres.id"), primary_key=True),
    Index("ix_games_genres_genre_id", "genre_id"),  # FR-02, NFR-19
)


class Genre(Base):
    __tablename__ = "genres"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)


class Platform(Base):
    __tablename__ = "platforms"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)


class Game(Base):
    __tablename__ = "games"
    __table_args__ = (
        UniqueConstraint("title", "year", "platform_id", name="uq_games_title_year_platform_id"),  # BR-14
        Index("ix_games_title", "title"),  # FR-03, NFR-19
        Index("ix_games_year", "year"),  # FR-02, NFR-19
        Index("ix_games_platform_id", "platform_id"),  # FR-02, NFR-19
    )

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    synopsis: Mapped[str | None] = mapped_column(Text)
    developer: Mapped[str | None] = mapped_column(String(255))
    platform_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("platforms.id"), nullable=False
    )
    external_id: Mapped[str | None] = mapped_column(
        String(100), unique=True
    )  # id en RAWG/IGDB para sync futuro (Phase 2)
    created_by: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id"), nullable=False
    )  # admin que lo añadió — BR-16
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )

    # BR-15: un juego debe tener al menos un género en games_genres antes de
    # publicarse. Se valida a nivel de aplicación, no con constraint SQL.