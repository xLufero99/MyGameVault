"""Configuración de los tests.

Inyecta variables de entorno antes de importar la app, de modo que los tests
no dependan de un `.env` real ni de una BD externa (NFR-13). El orden importa:
pytest carga este conftest antes que los módulos de test.
"""

import os

os.environ.setdefault("SUPABASE_PROJECT_REF", "test-ref")
os.environ.setdefault("SUPABASE_DB_PASSWORD", "test-password")
os.environ.setdefault("SUPABASE_URL", "https://test.supabase.co")
os.environ.setdefault("SUPABASE_SECRET_KEY", "test-secret")
