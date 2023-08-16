from typing import Any, Literal, Optional  # type: ignore

import cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams
from cherwell_pydantic_api.generated_api_utils import GeneratedInterfaceBase


class TeamsInterface(GeneratedInterfaceBase):
    async def AddUserToTeamByBatchV1(
        self,
        request: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.AddUserToTeamByBatchRequest,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.AddUserToTeamByBatchResponse
    ):
        """Add users to a team by batch

        Operation to add users to a Team by batch. To get internal IDs for users, use “Get User Information in a Batch.” To get a Team's internal ID, use "Get all available Teams."
         :param request: Request object to specify a list of add user to team request objects.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.AddUserToTeamByBatchResponse
        """
        response = await self.post_body(
            "/api/V1/addusertoteambybatch",
            content=request.model_dump_json(exclude_unset=True, by_alias=True),
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.AddUserToTeamByBatchResponse,
        )

    async def AddUserToTeamV1(
        self,
        dataRequest: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.AddUserToTeamRequest,
    ) -> None:
        """Add a user to a team

        Operation to add a user to a Team. To get the user's internal ID, use "Get a user by login ID" or "Get a user by public ID." To get a Team's internal ID, use "Get all available Teams."
         :param dataRequest: Request object to specify user and team values.
         :return: None"""
        response = await self.post_body(
            "/api/V1/addusertoteam",
            content=dataRequest.model_dump_json(exclude_unset=True, by_alias=True),
        )
        self.check_response(response)

    async def AddUserToTeamV2(
        self,
        dataRequest: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.AddUserToTeamRequest,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.AddUserToTeamResponse
    ):
        """Add a user to a team

        Operation to add a user to a Team. To get the user's internal ID, use "Get a user by login ID" or "Get a user by public ID." To get a Team's internal ID, use "Get all available Teams."
         :param dataRequest: Request object to specify user and team values.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.AddUserToTeamResponse
        """
        response = await self.post_body(
            "/api/V2/addusertoteam",
            content=dataRequest.model_dump_json(exclude_unset=True, by_alias=True),
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.AddUserToTeamResponse,
        )

    async def DeleteTeamV1(
        self,
        teamid: str,
    ) -> None:
        """Delete a Team

        Operation to delete a Team by Team ID.
         :param teamid: Specify the Team ID.
         :return: None"""
        self.validate_path_param(teamid, str)
        response = await self.delete(f"/api/V1/deleteteam/{teamid}")
        self.check_response(response)

    async def GetTeamsV1(
        self,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.TeamsResponse
    ):
        """Get all available Teams

        Operation to get IDs and names for all available Teams.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.TeamsResponse
        """
        response = await self.get("/api/V1/getteams")
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.TeamsResponse,
        )

    async def GetTeamsV2(
        self,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.TeamsV2Response
    ):
        """Get all available Teams

        Operation to get IDs and names for all available Teams.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.TeamsV2Response
        """
        response = await self.get("/api/V2/getteams")
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.TeamsV2Response,
        )

    async def GetTeamV1(
        self,
        teamid: str,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.TeamResponse
    ):
        """Get a team by its TeamId

        Operation to get Team Info for a  single Team using its Team ID. To get a Team's internal ID, use "Get all available Teams." Note that TeamType has two possible values, where TeamType = 0 for User (CSM Users), or TeamType = 1 for Workgroup (CSM Customers).
         :param teamid: The Team ID of the Team to get.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.TeamResponse
        """
        self.validate_path_param(teamid, str)
        response = await self.get(f"/api/V1/getteam/{teamid}")
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.TeamResponse,
        )

    async def GetUsersTeamsV1(
        self,
        userRecordId: str,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.TeamsResponse
    ):
        """Get Team assignments for a user

        Operation to get Team assignments for a user. To get record IDs, use "Get a user by login ID" or "Get a user by public id."
         :param userRecordId: Specify the user record ID.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.TeamsResponse
        """
        self.validate_path_param(userRecordId, str)
        response = await self.get(f"/api/V1/getusersteams/userrecordid/{userRecordId}")
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.TeamsResponse,
        )

    async def GetUsersTeamsV2(
        self,
        userRecordId: str,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.TeamsV2Response
    ):
        """Get Team assignments for a user

        Operation to get Team assignments for a user. To get record IDs, use "Get a user by login ID" or "Get a user by public id."
         :param userRecordId: Specify the user record ID.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.TeamsV2Response
        """
        self.validate_path_param(userRecordId, str)
        response = await self.get(f"/api/V2/getusersteams/userrecordid/{userRecordId}")
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.TeamsV2Response,
        )

    async def GetWorkgroupsV1(
        self,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.TeamsResponse
    ):
        """Get all available Workgroups

        Operation to get IDs and names for all available Workgroups.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.TeamsResponse
        """
        response = await self.get("/api/V1/getworkgroups")
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.TeamsResponse,
        )

    async def GetWorkgroupsV2(
        self,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.TeamsV2Response
    ):
        """Get all available Workgroups

        Operation to get IDs and names for all available Workgroups.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.TeamsV2Response
        """
        response = await self.get("/api/V2/getworkgroups")
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.TeamsV2Response,
        )

    async def RemoveUserFromTeamV1(
        self,
        teamId: str,
        userrecordid: str,
    ) -> None:
        """Operation to remove a User from a Team.

        Operation to remove a User from a Team. To get the User's record ID, use "Get a User by login ID" or "Get a User by public ID." To get a Team's internal ID, use "Get all available Teams."
         :param teamId: Specify the internal ID of the Team.
         :param userrecordid: Specify the record ID of the User to remove.
         :return: None"""
        self.validate_path_param(teamId, str)
        self.validate_path_param(userrecordid, str)
        response = await self.delete(
            f"/api/V1/removeuserfromteam/teamid/{teamId}/userrecordid/{userrecordid}"
        )
        self.check_response(response)

    async def RemoveUserFromTeamV2(
        self,
        teamId: str,
        userrecordid: str,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.RemoveUserFromTeamResponse
    ):
        """Operation to remove a User from a Team.

        Operation to remove a User from a Team. To get the User's record ID, use "Get a User by login ID" or "Get a User by public ID." To get a Team's internal ID, use "Get all available Teams."
         :param teamId: Specify the internal ID of the Team.
         :param userrecordid: Specify the record ID of the User to remove.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.RemoveUserFromTeamResponse
        """
        self.validate_path_param(teamId, str)
        self.validate_path_param(userrecordid, str)
        response = await self.delete(
            f"/api/V2/removeuserfromteam/teamid/{teamId}/userrecordid/{userrecordid}"
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.RemoveUserFromTeamResponse,
        )

    async def RemoveCustomerFromWorkgroupV1(
        self,
        workgroupid: str,
        customerrecordid: str,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.RemoveCustomerFromWorkgroupResponse
    ):
        """Remove a customer from a Workgroup

        Operation to remove a Customer from a Workgroup.  To remove, specify the Workgroup ID and the Customer Record ID.
         :param workgroupid: Specify the Workgroup ID.
         :param customerrecordid: Specify the Customer record ID.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.RemoveCustomerFromWorkgroupResponse
        """
        self.validate_path_param(workgroupid, str)
        self.validate_path_param(customerrecordid, str)
        response = await self.delete(
            f"/api/V1/removecustomerfromworkgroup/workgroupid/{workgroupid}/customerrecordid/{customerrecordid}"
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.RemoveCustomerFromWorkgroupResponse,
        )

    async def SaveTeamV1(
        self,
        request: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.TeamSaveRequest,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.TeamSaveResponse
    ):
        """Create or update a team

        Operation to create or update a Team or Workgroup.
         :param request: Request object to create Teams or Workgroups. To create a Team, use teamType and teamName. To update a team, use teamID. Team type values must be User or CustomerWorkgroup. The teamType cannot be changed for existing Teams or Workgroups.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.TeamSaveResponse
        """
        response = await self.post_body(
            "/api/V1/saveteam",
            content=request.model_dump_json(exclude_unset=True, by_alias=True),
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.TeamSaveResponse,
        )

    async def SaveTeamMemberV1(
        self,
        request: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.SaveTeamMemberRequest,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.SaveTeamMemberResponse
    ):
        """Add or Update a team member

        Operation to add or update a Team Member. To add or update, specify User ID, Team ID, and if Team Manager.   Optionally, set the Team as the User's default Team.
         :param request: The request object to add or update a Team Member. User recID specifies the User to add or update. TeamId specifies the Team to update. IsTeamManager specifies whether the User is a Team Manager, and SetAsDefaultTeam specifies whether to set this Team as the User's default team. UserRecId, TeamId, and IsTeamManager are required.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.SaveTeamMemberResponse
        """
        response = await self.post_body(
            "/api/V1/saveteammember",
            content=request.model_dump_json(exclude_unset=True, by_alias=True),
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.SaveTeamMemberResponse,
        )

    async def SaveWorkgroupMemberV1(
        self,
        request: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.SaveWorkgroupMemberRequest,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.SaveWorkgroupMemberResponse
    ):
        """Save the membership status of a Workgroup member.

        Operation to add or update a Workgroup Member.  To add or update, specify Customer Record ID, Workgroup ID, and if Workgroup Manager.
         :param request: The request object to add or update a Workgroup Member. CustomerRecordId specifies the Customer to add or update. WorkgroupId specifies the Workgroup to update. CustomerIsWorkgroupManager specifies whether the Customer is a Workgroup Manager.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.SaveWorkgroupMemberResponse
        """
        response = await self.post_body(
            "/api/V1/saveworkgroupmember",
            content=request.model_dump_json(exclude_unset=True, by_alias=True),
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Teams.SaveWorkgroupMemberResponse,
        )
