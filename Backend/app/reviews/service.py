"""Servicio del módulo reviews (scaffold, sin lógica de negocio todavía).

Cubrirá escribir/editar/borrar reviews (FR-19..FR-21), la unicidad por
usuario+juego (BR-08) y la propiedad del autor (BR-09, con borrado por Admin
en Phase 2).
"""

from __future__ import annotations

from app.reviews.repository import ReviewRepository


class ReviewService:
    def __init__(self, repository: ReviewRepository) -> None:
        self._repository = repository