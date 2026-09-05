-- V1: schema inicial (8 tablas) segun Documentacion/data-model.md
-- Identificadores y valores de enum en ingles.

-- 1. users
create table public.users (
    id                 uuid primary key default gen_random_uuid(),
    email              varchar(255) not null unique,
    username           varchar(30)  not null unique,
    password_hash      varchar(255) not null,
    avatar_url         varchar(500),
    bio                text,
    role               text not null default 'user'
                       check (role in ('user', 'admin')),
    profile_visibility text not null default 'public'
                       check (profile_visibility in ('public', 'private')),
    created_at         timestamptz not null default now(),
    deleted_at         timestamptz
);

-- 2. genres
create table public.genres (
    id   uuid primary key default gen_random_uuid(),
    name varchar(50) not null unique
);

-- 3. platforms
create table public.platforms (
    id   uuid primary key default gen_random_uuid(),
    name varchar(50) not null unique
);

-- 4. games
create table public.games (
    id          uuid primary key default gen_random_uuid(),
    title       varchar(255) not null,
    year        int not null,
    synopsis    text,
    developer   varchar(255),
    platform_id uuid not null references public.platforms(id),
    external_id varchar(100) unique,
    created_by  uuid not null references public.users(id),
    created_at  timestamptz not null default now(),
    constraint uq_games_title_year_platform unique (title, year, platform_id)
);

create index idx_games_title        on public.games (title);
create index idx_games_year         on public.games (year);
create index idx_games_platform     on public.games (platform_id);
create index idx_games_created_by   on public.games (created_by);

-- 5. games_genres (N:M)
create table public.games_genres (
    game_id  uuid not null references public.games(id)  on delete cascade,
    genre_id uuid not null references public.genres(id) on delete cascade,
    primary key (game_id, genre_id)
);

create index idx_games_genres_genre on public.games_genres (genre_id);

-- 6. user_game_list
create table public.user_game_list (
    id         uuid primary key default gen_random_uuid(),
    user_id    uuid not null references public.users(id),
    game_id    uuid not null references public.games(id),
    status     text not null
               check (status in ('playing', 'completed', 'on_hold', 'dropped', 'plan_to_play')),
    favorite   boolean not null default false,
    start_date date,
    end_date   date,
    updated_at timestamptz not null default now(),
    constraint uq_user_game_list unique (user_id, game_id),
    constraint chk_list_dates check (end_date is null or start_date is null or end_date >= start_date)
);

create index idx_list_user on public.user_game_list (user_id);
create index idx_list_game on public.user_game_list (game_id);

-- 7. ratings
create table public.ratings (
    id         uuid primary key default gen_random_uuid(),
    user_id    uuid not null references public.users(id),
    game_id    uuid not null references public.games(id),
    value      int not null check (value between 1 and 10),
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now(),
    constraint uq_ratings unique (user_id, game_id)
);

create index idx_ratings_user on public.ratings (user_id);
create index idx_ratings_game on public.ratings (game_id);

-- 8. reviews
create table public.reviews (
    id         uuid primary key default gen_random_uuid(),
    user_id    uuid not null references public.users(id),
    game_id    uuid not null references public.games(id),
    content    text not null,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now(),
    deleted_at timestamptz
);

-- una review activa por juego por usuario; permite re-resena tras soft delete
create unique index uq_reviews_active on public.reviews (user_id, game_id) where deleted_at is null;
create index idx_reviews_user on public.reviews (user_id);
create index idx_reviews_game on public.reviews (game_id);