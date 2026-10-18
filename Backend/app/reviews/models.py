"""Modelo del módulo reviews."""

from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Index, Text, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class Review(Base):
    __tablename__ = "reviews"
    __table_args__ = (
        UniqueConstraint("user_id", "game_id", name="uq_reviews_user_game_id"),  # BR-08
        Index("ix_reviews_game_id", "game_id"),  # FR-05
    )

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    game_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("games.id"), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))  # soft delete — FR-43

    # BR-08: un solo review por juego por usuario (UNIQUE user_id+game_id);
    # reescribir actualiza, no duplica. BR-09: solo el autor edita/borra (salvo
    # Admin, Phase 2).