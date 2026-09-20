"""Schemas Pydantic del módulo ratings."""

from __future__ import annotations

import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class RatingBase(BaseModel):
    user_id: uuid.UUID
    game_id: uuid.UUID
    value: int = Field(ge=1, le=10)  # BR-07


class RatingRead(RatingBase):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    created_at: datetime
    updated_at: datetime