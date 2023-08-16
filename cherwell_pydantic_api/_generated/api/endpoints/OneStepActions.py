from typing import Any, Literal, Optional  # type: ignore

import cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core
import cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.OneStepActions
import cherwell_pydantic_api.types
from cherwell_pydantic_api.generated_api_utils import GeneratedInterfaceBase


class OneStepActionsInterface(GeneratedInterfaceBase):
    async def GetOneStepActionsByAssociation_Scope_ScopeOwner_FolderV1(
        self,
        association: str,
        scope: str,
        scopeowner: str,
        folder: str,
        links: Optional[bool] = None,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
    ):
        """Get One-Step Actions by Folder

        Operation to get One-Step Actions by Association, Scope, Scope Owner in a specific folder.
         :param association: Business Object association to get One-Step Actions for
         :param scope: Scope to get One-Step Actions for
         :param scopeowner: Scope owner to get One-Step Actions for
         :param folder: Folder to get One-Step Actions from
         :param links: Flag to include hyperlinks in results. Default is false.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
        """
        self.validate_path_param(association, str)
        self.validate_path_param(scope, str)
        self.validate_path_param(scopeowner, str)
        self.validate_path_param(folder, str)
        params: dict[str, Any] = {}
        if links is not None:
            params["links"] = links
        response = await self.get(
            f"/api/V1/getonestepactions/association/{association}/scope/{scope}/scopeowner/{scopeowner}/folder/{folder}",
            params=params,
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData,
        )

    async def GetOneStepActionsByAssociation_Scope_ScopeOwnerV1(
        self,
        association: str,
        scope: str,
        scopeowner: str,
        links: Optional[bool] = None,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
    ):
        """Get One-Step Actions by Scope Owner

        Operation to get One-Step Actions by Association, Scope, Scope Owner
         :param association: Business Object association to get One-Step Actions for
         :param scope: Scope to get One-Step Actions for
         :param scopeowner: Scope owner to get One-Step Actions for
         :param links: Flag to include hyperlinks in results. Default is false.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
        """
        self.validate_path_param(association, str)
        self.validate_path_param(scope, str)
        self.validate_path_param(scopeowner, str)
        params: dict[str, Any] = {}
        if links is not None:
            params["links"] = links
        response = await self.get(
            f"/api/V1/getonestepactions/association/{association}/scope/{scope}/scopeowner/{scopeowner}",
            params=params,
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData,
        )

    async def GetOneStepActionsByAssociation_ScopeV1(
        self,
        association: str,
        scope: str,
        links: Optional[bool] = None,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
    ):
        """Get One-Step Actions by Scope

        Operation to get One-Step Actions by Association, Scope
         :param association: Business Object association to get One-Step Actions for
         :param scope: Scope to get One-Step Actions for
         :param links: Flag to include hyperlinks in results. Default is false.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
        """
        self.validate_path_param(association, str)
        self.validate_path_param(scope, str)
        params: dict[str, Any] = {}
        if links is not None:
            params["links"] = links
        response = await self.get(
            f"/api/V1/getonestepactions/association/{association}/scope/{scope}",
            params=params,
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData,
        )

    async def GetOneStepActionsByAssociationV1(
        self,
        association: str,
        links: Optional[bool] = None,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
    ):
        """Get One-Step Actions by Association

        Operation to get One-Step Actions by Association
         :param association: Business Object association to get One-Step Actions for
         :param links: Flag to include hyperlinks in results. Default is false.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
        """
        self.validate_path_param(association, str)
        params: dict[str, Any] = {}
        if links is not None:
            params["links"] = links
        response = await self.get(
            f"/api/V1/getonestepactions/association/{association}", params=params
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData,
        )

    async def GetOneStepActionsV1(
        self,
        links: Optional[bool] = None,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
    ):
        """Get One-Step Actions by default Association

        Operation to get One-Step Actions by default Association
         :param links: Flag to include hyperlinks in results. Default is false.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
        """
        params: dict[str, Any] = {}
        if links is not None:
            params["links"] = links
        response = await self.get("/api/V1/getonestepactions", params=params)
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData,
        )

    async def RunOneStepActionByKeyForRecordByRecIdV1(
        self,
        standinkey: str,
        busobid: cherwell_pydantic_api.types.BusObIDParamType,
        busobrecid: cherwell_pydantic_api.types.BusObRecID,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.OneStepActions.OneStepActionResponse
    ):
        """Run a One-Step Action for a Business Object record

        Operation to run a One-Step Action for a Business Object record by Business Object ID and Business Object Record ID.
         :param standinkey: The key to find the One-Step Action to run
         :param busobid: Specify the Business Object ID.
         :param busobrecid: Specify the Business Object record ID.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.OneStepActions.OneStepActionResponse
        """
        self.validate_path_param(standinkey, str)
        self.validate_path_param(busobid, cherwell_pydantic_api.types.BusObIDParamType)
        self.validate_path_param(busobrecid, cherwell_pydantic_api.types.BusObRecID)
        response = await self.get(
            f"/api/V1/runonestepaction/standinkey/{standinkey}/busobid/{busobid}/busobrecid/{busobrecid}"
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.OneStepActions.OneStepActionResponse,
        )

    async def RunOneStepActionByStandInKeyV1(
        self,
        standinkey: str,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.OneStepActions.OneStepActionResponse
    ):
        """Run a stand alone One-Step Action

        Operation to run a One-Step Action that doesn't run against a Business Object Record.
         :param standinkey: The key to find the One-Step Action to run
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.OneStepActions.OneStepActionResponse
        """
        self.validate_path_param(standinkey, str)
        response = await self.get(f"/api/V1/runonestepaction/standinkey/{standinkey}")
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.OneStepActions.OneStepActionResponse,
        )

    async def RunOneStepActionV1(
        self,
        request: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.OneStepActions.OneStepActionRequest,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.OneStepActions.OneStepActionResponse
    ):
        """Run a One-Step Action using a OneStepActionRequest

        Operation to run a One-Step Action using a OneStepActionRequest. This request is used to start a One-Step Action run with additional information such as prompt values.
         :param request: Request object containing all the properties need to start a One-Step Action.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.OneStepActions.OneStepActionResponse
        """
        response = await self.post_body(
            "/api/V1/runonestepaction",
            content=request.model_dump_json(exclude_unset=True, by_alias=True),
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.OneStepActions.OneStepActionResponse,
        )
