"""Rutas del módulo ratings.

Sin endpoints todavía: la primera entrega solo expone GET /health en main.py.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/ratings", tags=["ratings"])