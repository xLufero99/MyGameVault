"""Repositorio del módulo games: única capa que accede a la BD.

Agrupa el acceso a catalog (Game, Genre, Platform) y a games_genres.
"""

from __future__ import annotations

import uuid

from sqlalchemy.orm import Session

from app.games.models import Game, Genre, Platform


class GameRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def get(self, game_id: uuid.UUID) -> Game | None:
        return self._session.get(Game, game_id)

    def get_genre(self, genre_id: uuid.UUID) -> Genre | None:
        return self._session.get(Genre, genre_id)

    def get_platform(self, platform_id: uuid.UUID) -> Platform | None:
        return self._session.get(Platform, platform_id)