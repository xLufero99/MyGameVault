"""Modelo del módulo ratings."""

from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import CheckConstraint, DateTime, ForeignKey, Index, Integer, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class Rating(Base):
    __tablename__ = "ratings"
    __table_args__ = (
        CheckConstraint("value BETWEEN 1 AND 10", name="value_range"),  # BR-07
        UniqueConstraint("user_id", "game_id", name="uq_ratings_user_game_id"),  # BR-06
        Index("ix_ratings_game_id", "game_id"),  # BR-10/NFR-01: AVG al vuelo por juego
    )

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    game_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("games.id"), nullable=False)
    value: Mapped[int] = mapped_column(Integer, nullable=False)  # 1..10 (CHECK)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

    # BR-06: un usuario solo puntúa un juego una vez; volver a puntuar
    # actualiza el valor (UNIQUE user_id+game_id + lógica upsert, aún no
    # implementada). BR-10: el promedio se recalcula con cada alta/baja/update.