"""User Account Controllers."""

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated

from litestar import Controller, delete, get, patch, post
from litestar.di import Provide

from app.config import constants
from app.db.models import User as UserModel
from app.domain.accounts.guards import requires_active_user
from app.domain.teams import urls
from app.domain.teams.dependencies import provide_teams_service
from app.domain.teams.guards import requires_team_admin, requires_team_membership
from app.domain.teams.schemas import Team, TeamCreate, TeamUpdate
from app.domain.teams.services import TeamService

if TYPE_CHECKING:
    from uuid import UUID

    from advanced_alchemy.service.pagination import OffsetPagination
    from litestar.params import Dependency, Parameter

    from app.lib.dependencies import FilterTypes


class TeamController(Controller):
    """Teams."""

    tags = ["Teams"]
    dependencies = {"teams_service": Provide(provide_teams_service)}
    guards = [requires_active_user]
    signature_namespace = {
        "TeamService": TeamService,
        "TeamUpdate": TeamUpdate,
        "TeamCreate": TeamCreate,
        "UserModel": UserModel,
    }
    dto = None
    return_dto = None

    @get(
        operation_id="ListTeams",
        name="teams:list",
        summary="List Teams",
        path=urls.TEAM_LIST,
    )
    async def list_teams(
        self,
        teams_service: TeamService,
        current_user: UserModel,
        filters: Annotated[list[FilterTypes], Dependency(skip_validation=True)],
    ) -> OffsetPagination[Team]:
        """List teams that your account can access.."""
        show_all = bool(
            current_user.is_superuser
            or any(
                assigned_role.role.name
                for assigned_role in current_user.roles
                if assigned_role.role.name in {constants.SUPERUSER_ACCESS_ROLE}
            ),
        )
        if show_all:
            return await teams_service.list_and_count(*filters, to_schema=Team)
        return await teams_service.get_user_teams(*filters, user_id=current_user.id, to_schema=Team)

    @post(
        operation_id="CreateTeam",
        name="teams:create",
        summary="Create a new team.",
        path=urls.TEAM_CREATE,
    )
    async def create_team(
        self,
        teams_service: TeamService,
        current_user: UserModel,
        data: TeamCreate,
    ) -> Team:
        """Create a new team."""
        obj = data.to_dict()
        obj.update({"owner_id": current_user.id, "owner": current_user})
        return await teams_service.create(obj, to_schema=Team)

    @get(
        operation_id="GetTeam",
        name="teams:get",
        guards=[requires_team_membership],
        summary="Retrieve the details of a team.",
        path=urls.TEAM_DETAIL,
    )
    async def get_team(
        self,
        teams_service: TeamService,
        team_id: Annotated[
            UUID,
            Parameter(
                title="Team ID",
                description="The team to retrieve.",
            ),
        ],
    ) -> Team:
        """Get details about a team."""
        return await teams_service.get(team_id, to_schema=Team)

    @patch(
        operation_id="UpdateTeam",
        name="teams:update",
        guards=[requires_team_admin],
        path=urls.TEAM_UPDATE,
    )
    async def update_team(
        self,
        data: TeamUpdate,
        teams_service: TeamService,
        team_id: Annotated[
            UUID,
            Parameter(
                title="Team ID",
                description="The team to update.",
            ),
        ],
    ) -> Team:
        """Update a migration team."""
        return await teams_service.update(item_id=team_id, data=data.to_dict(), to_schema=Team)

    @delete(
        operation_id="DeleteTeam",
        name="teams:delete",
        guards=[requires_team_admin],
        summary="Remove Team",
        path=urls.TEAM_DELETE,
    )
    async def delete_team(
        self,
        teams_service: TeamService,
        team_id: Annotated[
            UUID,
            Parameter(title="Team ID", description="The team to delete."),
        ],
    ) -> None:
        """Delete a team."""
        _ = await teams_service.delete(team_id)
