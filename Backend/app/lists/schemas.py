"""Schemas Pydantic del módulo lists (user_game_list)."""

from __future__ import annotations

import uuid
from datetime import date, datetime

from pydantic import BaseModel, ConfigDict

from app.lists.models import GameListStatus


class UserGameListBase(BaseModel):
    user_id: uuid.UUID
    game_id: uuid.UUID
    status: GameListStatus
    favorite: bool = False
    start_date: date | None = None
    end_date: date | None = None


class UserGameListRead(UserGameListBase):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    updated_at: datetime