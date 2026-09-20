"""Configuración de los tests.

Inyecta variables de entorno antes de importar la app, de modo que los tests
no dependan de un `.env` real ni de una BD externa (NFR-13). El orden importa:
pytest carga este conftest antes que los módulos de test.
"""

import os

os.environ.setdefault("DATABASE_URL", "sqlite+pysqlite:///:memory:")
os.environ.setdefault("JWT_SECRET", "test-secret")