"""Modelo del módulo lists: la lista personal de juegos (user_game_list)."""

from __future__ import annotations

import enum
import uuid
from datetime import date, datetime

from sqlalchemy import (
    Boolean,
    CheckConstraint,
    Date,
    DateTime,
    Enum,
    ForeignKey,
    UniqueConstraint,
    func,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


def _enum_values(enum_cls: type[enum.Enum]) -> list[str]:
    return [member.value for member in enum_cls]


class GameListStatus(str, enum.Enum):
    PLAYING = "playing"
    COMPLETED = "completed"
    ON_HOLD = "on_hold"
    DROPPED = "dropped"
    PLAN_TO_PLAY = "plan_to_play"


class UserGameList(Base):
    __tablename__ = "user_game_list"
    __table_args__ = (
        UniqueConstraint("user_id", "game_id", name="uq_user_game_list_user_game_id"),  # BR-11
        CheckConstraint(
            "start_date IS NULL OR end_date IS NULL OR end_date >= start_date",
            name="date_order",  # BR-12 — garantizado por CHECK
        ),
    )

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    game_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("games.id"), nullable=False)
    status: Mapped[GameListStatus] = mapped_column(
        Enum(GameListStatus, name="game_list_status", values_callable=_enum_values),
        nullable=False,
    )  # BR-11: un solo status por juego en la lista
    favorite: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False, server_default=text("false")
    )  # BR-13
    start_date: Mapped[date | None] = mapped_column(Date)
    end_date: Mapped[date | None] = mapped_column(Date)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

    # BR-12: end_date >= start_date (si ambas existen) — garantizado por CHECK
    # (ck_user_game_list_date_order).
    # BR-13: solo se puede marcar favorite un juego ya presente en la lista.
    # Pendiente de confirmar si favorite depende del status o es independiente.