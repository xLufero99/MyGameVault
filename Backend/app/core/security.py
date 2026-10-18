"""Seguridad (placeholder).

La autenticación se implementará en una entrega posterior. Aquí solo se deja
constancia de las operaciones planeadas, sin lógica por ahora:

- hash_password / verify_password con pwdlib[argon2] (NFR-04: contraseñas
  siempre hasheadas, nunca en texto plano).
- create_access_token / decode_access_token con pyjwt (NFR-05: JWT con
  expiración y renovación de token).
"""