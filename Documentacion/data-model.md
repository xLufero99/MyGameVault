# Relational Data Model — Video Game Tracking Platform

Hybrid design: the catalog is manually loaded by the Admin (FR-39), with the schema prepared to sync from an external API (RAWG/IGDB) later without redesign (nullable `external_id` field).

---

## Table: users

| Field | Type | Constraints | Note |
|---|---|---|---|
| id | UUID | PK | |
| email | varchar(255) | UNIQUE, NOT NULL | BR-01 |
| username | varchar(30) | UNIQUE, NOT NULL | BR-02 — always visible even if the profile is private |
| password_hash | varchar(255) | NOT NULL | NFR-04 — never plain text |
| avatar_url | varchar(500) | NULL | |
| bio | text | NULL | |
| role | enum('user','admin') | NOT NULL, DEFAULT 'user' | BR-03, NFR-20 — extensible enum, not boolean |
| profile_visibility | enum('public','private') | NOT NULL, DEFAULT 'public' | BR-04 |
| created_at | timestamp | NOT NULL, DEFAULT now() | |
| deleted_at | timestamp | NULL | soft delete — see pending BR-05 |

**Index:** `email`, `username` (already covered by UNIQUE).

---

## Table: genres

| Field | Type | Constraints |
|---|---|---|
| id | UUID | PK |
| name | varchar(50) | UNIQUE, NOT NULL |

## Table: platforms

| Field | Type | Constraints |
|---|---|---|
| id | UUID | PK |
| name | varchar(50) | UNIQUE, NOT NULL |

---

## Table: games

| Field | Type | Constraints | Note |
|---|---|---|---|
| id | UUID | PK | |
| title | varchar(255) | NOT NULL | |
| year | int | NOT NULL | |
| synopsis | text | NULL | |
| developer | varchar(255) | NULL | |
| platform_id | UUID | FK → platforms.id, NOT NULL | |
| external_id | varchar(100) | NULL, UNIQUE | id in RAWG/IGDB, for future sync (Phase 2) |
| created_by | UUID | FK → users.id, NOT NULL | admin who added it — BR-16 |
| created_at | timestamp | NOT NULL, DEFAULT now() | |

**Composite constraint:** `UNIQUE (title, year, platform_id)` — BR-14
**Indexes:** `title` (search), `year`, `platform_id` — NFR-19

## Table: games_genres (N:M)

| Field | Type | Constraints |
|---|---|---|
| game_id | UUID | FK → games.id |
| genre_id | UUID | FK → genres.id |

**Composite PK:** `(game_id, genre_id)`
**Rule:** a game must have at least 1 row here before being published — BR-15 (validated at the application level, not as a pure SQL constraint)

---

## Table: user_game_list

Represents each user's personal list (status + dates + favorite).

| Field | Type | Constraints | Note |
|---|---|---|---|
| id | UUID | PK | |
| user_id | UUID | FK → users.id, NOT NULL | |
| game_id | UUID | FK → games.id, NOT NULL | |
| status | enum('playing','completed','on_hold','dropped','plan_to_play') | NOT NULL | BR-11 |
| favorite | boolean | NOT NULL, DEFAULT false | BR-13 |
| start_date | date | NULL | |
| end_date | date | NULL | BR-12: guaranteed by CHECK `ck_user_game_list_date_order` (`start_date IS NULL OR end_date IS NULL OR end_date >= start_date`) |
| updated_at | timestamp | NOT NULL, DEFAULT now() | |

**Composite constraint:** `UNIQUE (user_id, game_id)` — a game can only have one status at a time per user (BR-11)

---

## Table: ratings

| Field | Type | Constraints | Note |
|---|---|---|---|
| id | UUID | PK | |
| user_id | UUID | FK → users.id, NOT NULL | |
| game_id | UUID | FK → games.id, NOT NULL | |
| value | int | NOT NULL, CHECK (value BETWEEN 1 AND 10) | BR-07 |
| created_at | timestamp | NOT NULL, DEFAULT now() | |
| updated_at | timestamp | NOT NULL, DEFAULT now() | |

**Composite constraint:** `UNIQUE (user_id, game_id)` — BR-06, rating again updates, does not duplicate

## Table: reviews

| Field | Type | Constraints | Note |
|---|---|---|---|
| id | UUID | PK | |
| user_id | UUID | FK → users.id, NOT NULL | |
| game_id | UUID | FK → games.id, NOT NULL | |
| content | text | NOT NULL | |
| created_at | timestamp | NOT NULL, DEFAULT now() | |
| updated_at | timestamp | NOT NULL, DEFAULT now() | |
| deleted_at | timestamp | NULL | soft delete — allows the Admin to hide it without losing the record (Phase 2, FR-43) |

**Composite constraint:** `UNIQUE (user_id, game_id)` — BR-08

---

## Derived field: average_rating

Not stored as a manually editable column. Two implementation options (to be decided at the architecture stage, not here):

1. **Computed on the fly**: `AVG(value)` over `ratings` filtered by `game_id` on every query to the game page. Simpler, but more expensive as the catalog grows.
2. **Cached column** `average_rating` on the `games` table, updated via trigger or at the application layer every time a rating is inserted/updated/deleted (BR-10). Faster to read, requires keeping it in sync.

For the expected MVP size, option 1 (computed on the fly with an index on `game_id`) is sufficient and avoids sync bugs.

---

## Open items to resolve before writing migrations

- **BR-05**: are a deleted user's reviews/ratings cascade-deleted or anonymized? Modeled above with `deleted_at` (soft delete) on `users`, which allows anonymizing instead of deleting — but the exact display policy for `users.deleted_at IS NOT NULL` still needs to be decided.
- If the external API is integrated later, `external_id` is already in place to map the synced record without touching the rest of the schema.

---

## Implementation notes (Python + SQLAlchemy backend)

These formalize choices already applied when generating the initial Alembic migration (rev `0001`), so the docs and the schema stay aligned:

- **Timestamps** are stored as `timestamptz` (`timestamp` in the tables above is implemented as `TIMESTAMP WITH TIME ZONE` / `sa.DateTime(timezone=True)`), with `DEFAULT now()` as documented.
- **Enums** (`role`, `profile_visibility`, `status`) are native PostgreSQL `ENUM` types. The type for `users.role` is named `user_role` and the type for `user_game_list.status` is named `game_list_status`, so the DB-level names don't collide with column names.
- **Extra indexes beyond those listed above**, added to serve reads without relying on leading-column order of composite keys:
  - `ratings(game_id)` — supports the on-the-fly `AVG(value)` per game (option 1, BR-10). The `UNIQUE (user_id, game_id)` does not cover it because it starts with `user_id`.
  - `reviews(game_id)` — FR-05 (reviews listed per game).
  - `games_genres(genre_id)` — FR-02/NFR-19 (filter by genre); the composite PK only covers lookups starting by `game_id`.
- **BR-12 (dates order)** is guaranteed at the DB level via the named CHECK `ck_user_game_list_date_order` on `user_game_list`.
- **Open item FR-04**: the requirements mention screenshots for the game detail page, but there is no field/table for covers or screenshots in the model. It will need a decision and a schema change before any image-related feature is built.
