"""initial schema

Revision ID: 0001
Revises:
Create Date: 2026-09-19

Generada a mano (sin conexión a BD) a partir de data-model.md. Los nombres de
constraints/índices siguen la naming convention de app.core.db.
"""

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision = "0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Enums nativos de PostgreSQL (BR-03, NFR-20). Las columnas usan
    # create_type=False para no recrear el tipo (ajuste de revisión).
    op.execute("CREATE TYPE user_role AS ENUM ('user', 'admin')")
    op.execute("CREATE TYPE profile_visibility AS ENUM ('public', 'private')")
    op.execute(
        "CREATE TYPE game_list_status AS ENUM"
        " ('playing', 'completed', 'on_hold', 'dropped', 'plan_to_play')"
    )

    op.create_table(
        "users",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("username", sa.String(length=30), nullable=False),
        sa.Column("password_hash", sa.String(length=255), nullable=False),
        sa.Column("avatar_url", sa.String(length=500), nullable=True),
        sa.Column("bio", sa.Text(), nullable=True),
        sa.Column(
            "role",
            postgresql.ENUM("user", "admin", name="user_role", create_type=False),
            nullable=False,
            server_default="user",
        ),
        sa.Column(
            "profile_visibility",
            postgresql.ENUM("public", "private", name="profile_visibility", create_type=False),
            nullable=False,
            server_default="public",
        ),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id", name="pk_users"),
        sa.UniqueConstraint("email", name="uq_users_email"),
        sa.UniqueConstraint("username", name="uq_users_username"),
    )

    op.create_table(
        "genres",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("name", sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint("id", name="pk_genres"),
        sa.UniqueConstraint("name", name="uq_genres_name"),
    )

    op.create_table(
        "platforms",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("name", sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint("id", name="pk_platforms"),
        sa.UniqueConstraint("name", name="uq_platforms_name"),
    )

    op.create_table(
        "games",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("year", sa.Integer(), nullable=False),
        sa.Column("synopsis", sa.Text(), nullable=True),
        sa.Column("developer", sa.String(length=255), nullable=True),
        sa.Column("platform_id", sa.Uuid(), nullable=False),
        sa.Column("external_id", sa.String(length=100), nullable=True),
        sa.Column("created_by", sa.Uuid(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.PrimaryKeyConstraint("id", name="pk_games"),
        sa.ForeignKeyConstraint(["platform_id"], ["platforms.id"], name="fk_games_platform_id_platforms"),
        sa.ForeignKeyConstraint(["created_by"], ["users.id"], name="fk_games_created_by_users"),
        sa.UniqueConstraint("external_id", name="uq_games_external_id"),
        sa.UniqueConstraint("title", "year", "platform_id", name="uq_games_title_year_platform_id"),
    )
    op.create_index("ix_games_title", "games", ["title"])
    op.create_index("ix_games_year", "games", ["year"])
    op.create_index("ix_games_platform_id", "games", ["platform_id"])

    op.create_table(
        "games_genres",
        sa.Column("game_id", sa.Uuid(), nullable=False),
        sa.Column("genre_id", sa.Uuid(), nullable=False),
        sa.ForeignKeyConstraint(["game_id"], ["games.id"], name="fk_games_genres_game_id_games"),
        sa.ForeignKeyConstraint(["genre_id"], ["genres.id"], name="fk_games_genres_genre_id_genres"),
        sa.PrimaryKeyConstraint("game_id", "genre_id", name="pk_games_genres"),
    )
    op.create_index("ix_games_genres_genre_id", "games_genres", ["genre_id"])

    op.create_table(
        "user_game_list",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("user_id", sa.Uuid(), nullable=False),
        sa.Column("game_id", sa.Uuid(), nullable=False),
        sa.Column(
            "status",
            postgresql.ENUM(
                "playing", "completed", "on_hold", "dropped", "plan_to_play",
                name="game_list_status", create_type=False,
            ),
            nullable=False,
        ),
        sa.Column("favorite", sa.Boolean(), server_default=sa.text("false"), nullable=False),
        sa.Column("start_date", sa.Date(), nullable=True),
        sa.Column("end_date", sa.Date(), nullable=True),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.PrimaryKeyConstraint("id", name="pk_user_game_list"),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], name="fk_user_game_list_user_id_users"),
        sa.ForeignKeyConstraint(["game_id"], ["games.id"], name="fk_user_game_list_game_id_games"),
        sa.UniqueConstraint("user_id", "game_id", name="uq_user_game_list_user_game_id"),
        sa.CheckConstraint(
            "start_date IS NULL OR end_date IS NULL OR end_date >= start_date",
            name="date_order",
        ),
    )

    op.create_table(
        "ratings",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("user_id", sa.Uuid(), nullable=False),
        sa.Column("game_id", sa.Uuid(), nullable=False),
        sa.Column("value", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.PrimaryKeyConstraint("id", name="pk_ratings"),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], name="fk_ratings_user_id_users"),
        sa.ForeignKeyConstraint(["game_id"], ["games.id"], name="fk_ratings_game_id_games"),
        sa.CheckConstraint("value BETWEEN 1 AND 10", name="value_range"),
        sa.UniqueConstraint("user_id", "game_id", name="uq_ratings_user_game_id"),
    )
    op.create_index("ix_ratings_game_id", "ratings", ["game_id"])

    op.create_table(
        "reviews",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("user_id", sa.Uuid(), nullable=False),
        sa.Column("game_id", sa.Uuid(), nullable=False),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id", name="pk_reviews"),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], name="fk_reviews_user_id_users"),
        sa.ForeignKeyConstraint(["game_id"], ["games.id"], name="fk_reviews_game_id_games"),
        sa.UniqueConstraint("user_id", "game_id", name="uq_reviews_user_game_id"),
    )
    op.create_index("ix_reviews_game_id", "reviews", ["game_id"])


def downgrade() -> None:
    op.drop_index("ix_reviews_game_id", table_name="reviews")
    op.drop_table("reviews")

    op.drop_index("ix_ratings_game_id", table_name="ratings")
    op.drop_table("ratings")

    op.drop_table("user_game_list")

    op.drop_index("ix_games_genres_genre_id", table_name="games_genres")
    op.drop_table("games_genres")

    op.drop_index("ix_games_title", table_name="games")
    op.drop_index("ix_games_year", table_name="games")
    op.drop_index("ix_games_platform_id", table_name="games")
    op.drop_table("games")

    op.drop_table("platforms")
    op.drop_table("genres")
    op.drop_table("users")

    op.execute("DROP TYPE game_list_status")
    op.execute("DROP TYPE profile_visibility")
    op.execute("DROP TYPE user_role")