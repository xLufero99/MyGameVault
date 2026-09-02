# Railway + Supabase (PostgreSQL)

Configuración para que el backend (Spring Boot) se conecte a Supabase desde
Railway usando **una sola variable de conexión**, sin credenciales embebidas
en la URL.

## Variables a crear en el dashboard de Railway

En tu proyecto de Railway, ve a la pestaña de tu servicio backend →
**Variables**, y crea estas 3 variables con exactamente estos nombres:

```
DB_URL=jdbc:postgresql://db.gglcjutpvnjyfiacsaua.supabase.co:5432/postgres
DB_USER=postgres
DB_PASSWORD=el_password_real_de_supabase_sin_corchetes_ni_espacios
```

> **Importante**: `DB_PASSWORD` es el password del rol `postgres` de tu
> proyecto Supabase (el mismo que usas en local desde `.env`). Pónlo tal cual,
> sin corchetes, comillas ni espacios.

## Lo que espera la app

`application.properties` lee tres variables por separado:

```properties
spring.datasource.url=${DB_URL}
spring.datasource.username=${DB_USER}
spring.datasource.password=${DB_PASSWORD}
spring.datasource.driver-class-name=org.postgresql.Driver
```

El formato de `DB_URL` debe ser **JDBC**:

```
jdbc:postgresql://HOST:PUERTO/DB
```

**NO** uses el formato `postgresql://user:pass@host/db` (estilo libpq /
pgAdmin). Ese formato es válido para copiar/pegar en herramientas de BD, pero
**no** es el que espera el driver JDBC de PostgreSQL. Aquí el usuario y el
password van en variables separadas (`DB_USER`, `DB_PASSWORD`).

## Si Railway falla por IPv6 (conexión directa)

Si el deploy no conecta con la URL directa de Supabase (por temas de IPv6),
activa el **Transaction Pooler** de Supabase (puerto **6543**, IPv4). En ese
caso la URL cambia a:

```
DB_URL=jdbc:postgresql://aws-0-<region>.pooler.supabase.com:6543/postgres
DB_USER=postgres.gglcjutpvnjyfiacsaua
```

Reemplaza `<region>` por la región real de tu proyecto (p. ej. `us-east-1`),
que encuentras en Supabase → *Project Settings → Database → Connection string*
→ pestaña *Transaction pooler*.

## Ajustes relevantes ya configurados

- HikariCP: `maximum-pool-size=10` (acorde al plan free de Supabase via pooler).
- `ddl-auto=update` **temporal** solo para desarrollo/prueba; en producción
  debe volver a `validate` o `none`.
- Sin credenciales hardcodeadas: todo viene de variables de entorno.