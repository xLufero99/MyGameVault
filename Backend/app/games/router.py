"""Rutas del módulo games (catalog + genres + platforms).

Sin endpoints todavía: la primera entrega solo expone GET /health en main.py.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/games", tags=["games"])