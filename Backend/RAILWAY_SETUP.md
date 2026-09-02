# Railway + Supabase (PostgreSQL)

Configuración para que el backend (Spring Boot) se conecte a Supabase desde
Railway usando **Transaction Pooler** (IPv4), la misma estructura que el
proyecto Duelith.

## Variables a crear en el dashboard de Railway

En tu proyecto de Railway, ve a la pestaña de tu servicio backend →
**Variables**, y crea estas variables:

```
SUPABASE_DB_PASSWORD=<el_password_real_de_supabase>
SUPABASE_PROJECT_REF=gglcjutpvnjyfiacsaua
```

## Lo que espera la app

`application.properties` usa esta configuración de pooler (IPv4):

```properties
spring.datasource.url=jdbc:postgresql://aws-0-us-west-2.pooler.supabase.com:5432/postgres?sslmode=require&connectTimeout=30000&socketTimeout=30000
spring.datasource.username=postgres.${SUPABASE_PROJECT_REF}
spring.datasource.password=${SUPABASE_DB_PASSWORD}
spring.datasource.driver-class-name=org.postgresql.Driver
```

El username se forma como `postgres.<project-ref>` (ej. `postgres.gglcjutpvnjyfiacsaua`).

## Si la región de Supabase no es us-west-2

Si tu proyecto Supabase está en otra región, cambia `us-west-2` en la URL
por la correcta (ej. `us-east-1`). La encuentras en Supabase →
*Project Settings → Database → Connection string → Transaction pooler*.

## Nota

La conexión directa (puerto 5432 sin pooler) usa IPv6, que Railway no
soporta. Por eso se usa el Transaction Pooler que expone IPv4.
