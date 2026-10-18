"""Servicio del módulo games (scaffold, sin lógica de negocio todavía).

Cubrirá el catálogo (FR-01..FR-03, FR-39..FR-42), filtros por género,
plataforma y año, y la validación BR-15 (≥1 género antes de publicar).
"""

from __future__ import annotations

from app.games.repository import GameRepository


class GameService:
    def __init__(self, repository: GameRepository) -> None:
        self._repository = repository