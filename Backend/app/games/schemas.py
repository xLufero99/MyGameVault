"""Schemas Pydantic del módulo games (juegos + genres + platforms)."""

from __future__ import annotations

import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class GenreBase(BaseModel):
    name: str


class GenreRead(GenreBase):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID


class PlatformBase(BaseModel):
    name: str


class PlatformRead(PlatformBase):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID


class GameBase(BaseModel):
    title: str
    year: int
    synopsis: str | None = None
    developer: str | None = None
    platform_id: uuid.UUID
    external_id: str | None = None


class GameRead(GameBase):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    created_by: uuid.UUID
    created_at: datetime