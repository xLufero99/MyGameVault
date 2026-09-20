"""Repositorio del módulo ratings: única capa que accede a la BD."""

from __future__ import annotations

import uuid

from sqlalchemy.orm import Session

from app.ratings.models import Rating


class RatingRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def get(self, rating_id: uuid.UUID) -> Rating | None:
        return self._session.get(Rating, rating_id)