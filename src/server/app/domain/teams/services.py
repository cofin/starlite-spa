from app.lib.service import RepositoryService

from .models import Team, TeamInvitation, TeamMember

__all__ = ["TeamService", "TeamInvitationService", "TeamMemberService"]


class TeamService(RepositoryService[Team]):
    """Team Service."""


class TeamMemberService(RepositoryService[TeamMember]):
    """Team Member Service."""


class TeamInvitationService(RepositoryService[TeamInvitation]):
    """Team Invitation Service."""
