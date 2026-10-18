"""Rutas del módulo reviews.

Sin endpoints todavía: la primera entrega solo expone GET /health en main.py.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/reviews", tags=["reviews"])