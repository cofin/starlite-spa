"""user accounts

Revision ID: a026c8caab5a
Revises:
Create Date: 2023-03-26 11:47:01.493173

"""
import sqlalchemy as sa
from alembic import op

__all__ = ["downgrade", "upgrade"]


# revision identifiers, used by Alembic.
revision = "a026c8caab5a"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "team",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(length=500), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("created", sa.DateTime(), nullable=False),
        sa.Column("updated", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_team")),
    )
    op.create_index(op.f("ix_team_name"), "team", ["name"], unique=False)
    op.create_table(
        "user_account",
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("hashed_password", sa.String(length=255), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("is_superuser", sa.Boolean(), nullable=False),
        sa.Column("is_verified", sa.Boolean(), nullable=False),
        sa.Column("verified_at", sa.DateTime(), nullable=True),
        sa.Column("joined_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("created", sa.DateTime(), nullable=False),
        sa.Column("updated", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_user_account")),
        comment="User accounts for application access",
    )
    op.create_index(op.f("ix_user_account_email"), "user_account", ["email"], unique=True)
    op.create_table(
        "team_invitation",
        sa.Column("team_id", sa.Uuid(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("role", sa.String(length=50), nullable=False),
        sa.Column("is_accepted", sa.Boolean(), nullable=False),
        sa.Column("invited_by_id", sa.Uuid(), nullable=True),
        sa.Column("invited_by_email", sa.String(), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("created", sa.DateTime(), nullable=False),
        sa.Column("updated", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["invited_by_id"],
            ["user_account.id"],
            name=op.f("fk_team_invitation_invited_by_id_user_account"),
            ondelete="set null",
        ),
        sa.ForeignKeyConstraint(
            ["team_id"], ["team.id"], name=op.f("fk_team_invitation_team_id_team"), ondelete="cascade"
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_team_invitation")),
    )
    op.create_index(op.f("ix_team_invitation_email"), "team_invitation", ["email"], unique=False)
    op.create_table(
        "team_member",
        sa.Column("user_id", sa.Uuid(), nullable=False),
        sa.Column("team_id", sa.Uuid(), nullable=False),
        sa.Column("role", sa.String(length=50), nullable=False),
        sa.Column("is_owner", sa.Boolean(), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("created", sa.DateTime(), nullable=False),
        sa.Column("updated", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["team_id"], ["team.id"], name=op.f("fk_team_member_team_id_team"), ondelete="cascade"),
        sa.ForeignKeyConstraint(
            ["user_id"], ["user_account.id"], name=op.f("fk_team_member_user_id_user_account"), ondelete="cascade"
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_team_member")),
        sa.UniqueConstraint("user_id", "team_id", name=op.f("uq_team_member_user_id")),
    )
    op.create_index(op.f("ix_team_member_role"), "team_member", ["role"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_team_member_role"), table_name="team_member")
    op.drop_table("team_member")
    op.drop_index(op.f("ix_team_invitation_email"), table_name="team_invitation")
    op.drop_table("team_invitation")
    op.drop_index(op.f("ix_user_account_email"), table_name="user_account")
    op.drop_table("user_account")
    op.drop_index(op.f("ix_team_name"), table_name="team")
    op.drop_table("team")
    # ### end Alembic commands ###
