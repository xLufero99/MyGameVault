"""Rutas del módulo lists (user_game_list).

Sin endpoints todavía: la primera entrega solo expone GET /health en main.py.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/lists", tags=["lists"])