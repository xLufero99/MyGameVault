"""Servicio del módulo lists (scaffold, sin lógica de negocio todavía).

Cubrirá añadir juego a la lista (FR-15), cambiar status (FR-16), registrar
fechas de inicio/fin (FR-17), marcar favorito (FR-22) y las validaciones
BR-12 y BR-13.
"""

from __future__ import annotations

from app.lists.repository import UserGameListRepository


class UserGameListService:
    def __init__(self, repository: UserGameListRepository) -> None:
        self._repository = repository