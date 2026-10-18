"""Servicio del módulo users (scaffold, sin lógica de negocio todavía).

Registrará/hará login (FR-12, FR-13), gestión de perfil y visibilidad (FR-23,
FR-24) y borrado de cuenta (FR-26, NFR-22).
"""

from __future__ import annotations

from app.users.repository import UserRepository


class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository