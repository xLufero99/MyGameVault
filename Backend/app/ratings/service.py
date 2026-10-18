"""Servicio del módulo ratings (scaffold, sin lógica de negocio todavía).

Cubrirá puntuar de 1 a 10 (FR-18), el upsert por usuario+juego (BR-06) y la
recalcular del promedio (BR-10, opción 1: AVG al vuelo).
"""

from __future__ import annotations

from app.ratings.repository import RatingRepository


class RatingService:
    def __init__(self, repository: RatingRepository) -> None:
        self._repository = repository