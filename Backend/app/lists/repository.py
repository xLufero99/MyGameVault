"""Repositorio del módulo lists: única capa que accede a la BD."""

from __future__ import annotations

import uuid

from sqlalchemy.orm import Session

from app.lists.models import UserGameList


class UserGameListRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def get(self, entry_id: uuid.UUID) -> UserGameList | None:
        return self._session.get(UserGameList, entry_id)