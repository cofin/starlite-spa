"""User Account Controllers."""
from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import select
from sqlalchemy.orm import joinedload, load_only, noload, selectinload

from app.db.models import Tag, Team, TeamInvitation, TeamMember, User
from app.domain.teams.services import TeamInvitationService, TeamMemberService, TeamService

__all__ = ("provide_team_members_service", "provide_teams_service", "provide_team_invitations_service")


if TYPE_CHECKING:
    from collections.abc import AsyncGenerator

    from sqlalchemy.ext.asyncio import AsyncSession


async def provide_teams_service(db_session: AsyncSession) -> AsyncGenerator[TeamService, None]:
    """Construct repository and service objects for the request."""
    async with TeamService.new(
        session=db_session,
        statement=select(Team)
        .order_by(Team.name)
        .options(
            selectinload(Team.tags).options(load_only(Tag.name, Tag.slug, Tag.description, Tag.id)),
            selectinload(Team.members).options(
                load_only(
                    TeamMember.id,
                    TeamMember.user_id,
                    TeamMember.team_id,
                    TeamMember.role,
                    TeamMember.is_owner,
                ),
                joinedload(TeamMember.user, innerjoin=True).options(
                    load_only(User.name, User.email).options(selectinload(User.roles)),
                ),
            ),
        ),
    ) as service:
        yield service


async def provide_team_members_service(db_session: AsyncSession) -> AsyncGenerator[TeamMemberService, None]:
    """Construct repository and service objects for the request."""
    async with TeamMemberService.new(
        session=db_session,
        statement=select(TeamMember).options(
            noload("*"),
            joinedload(TeamMember.team, innerjoin=True).options(noload("*")),
            joinedload(TeamMember.user, innerjoin=True).options(noload("*")),
        ),
    ) as service:
        yield service


async def provide_team_invitations_service(db_session: AsyncSession) -> AsyncGenerator[TeamInvitationService, None]:
    """Construct repository and service objects for the request."""
    async with TeamInvitationService.new(
        session=db_session,
        statement=select(TeamInvitation).options(
            noload("*"),
            joinedload(TeamInvitation.team, innerjoin=True).options(noload("*")),
            joinedload(TeamInvitation.invited_by, innerjoin=True).options(noload("*")),
        ),
    ) as service:
        yield service
