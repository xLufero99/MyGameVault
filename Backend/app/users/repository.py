"""Repositorio del módulo users: única capa que accede a la BD."""

from __future__ import annotations

import uuid

from sqlalchemy.orm import Session

from app.users.models import User


class UserRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def get(self, user_id: uuid.UUID) -> User | None:
        return self._session.get(User, user_id)