"""Modelos del módulo users.

Enums nativos de PostgreSQL (BR-03, NFR-20) y soft delete (BR-05 pendiente).
"""

from __future__ import annotations

import enum
import uuid
from datetime import datetime

from sqlalchemy import DateTime, Enum, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


def _enum_values(enum_cls: type[enum.Enum]) -> list[str]:
    return [member.value for member in enum_cls]


class UserRole(str, enum.Enum):
    USER = "user"
    ADMIN = "admin"


class ProfileVisibility(str, enum.Enum):
    PUBLIC = "public"
    PRIVATE = "private"


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)  # BR-01
    username: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)  # BR-02
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)  # NFR-04
    avatar_url: Mapped[str | None] = mapped_column(String(500))
    bio: Mapped[str | None] = mapped_column(Text)
    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole, name="user_role", values_callable=_enum_values),
        nullable=False,
        default=UserRole.USER,
        server_default=UserRole.USER.value,
    )  # BR-03
    profile_visibility: Mapped[ProfileVisibility] = mapped_column(
        Enum(ProfileVisibility, name="profile_visibility", values_callable=_enum_values),
        nullable=False,
        default=ProfileVisibility.PUBLIC,
        server_default=ProfileVisibility.PUBLIC.value,
    )  # BR-04
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))  # soft delete