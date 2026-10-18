"""Schemas Pydantic del módulo users (scaffold mínimo, espejo de data-model.md)."""

from __future__ import annotations

import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr

from app.users.models import ProfileVisibility, UserRole


class UserBase(BaseModel):
    email: EmailStr
    username: str
    avatar_url: str | None = None
    bio: str | None = None
    role: UserRole = UserRole.USER
    profile_visibility: ProfileVisibility = ProfileVisibility.PUBLIC


class UserRead(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    created_at: datetime
    deleted_at: datetime | None = None