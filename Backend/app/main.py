"""Punto de entrada de la API.

Primera entrega: únicamente GET /health. Los routers de los módulos
(users, games, lists, ratings, reviews) se montarán en entregas posteriores.
"""

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.core.config import settings

app = FastAPI(title="MyGameVault API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


"""Ruta de salud de la API."""

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "TODO CORRECTO"}


