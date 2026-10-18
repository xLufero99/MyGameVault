"""Punto de entrada de la API.

Primera entrega: únicamente GET /health. Los routers de los módulos
(users, games, lists, ratings, reviews) se montarán en entregas posteriores.
"""

from fastapi import FastAPI

app = FastAPI(title="MyGameVault API", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}