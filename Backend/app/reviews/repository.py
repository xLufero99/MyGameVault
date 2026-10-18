"""Repositorio del módulo reviews: única capa que accede a la BD."""

from __future__ import annotations

import uuid

from sqlalchemy.orm import Session

from app.reviews.models import Review


class ReviewRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def get(self, review_id: uuid.UUID) -> Review | None:
        return self._session.get(Review, review_id)