from typing import Any, Dict, List, Literal, Optional, Union, AsyncIterable, Iterable
from pydantic import parse_obj_as
import cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts
import cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Lifecycle
from cherwell_pydantic_api.generated_api_utils import GeneratedInterfaceBase


class LifecycleInterface(GeneratedInterfaceBase):
    async def GetStages(
        self,
        businessObjectDefinitionId: str,
    ) -> cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Lifecycle.GetStagesResponse:
        """Get lifecycle stages

        Gets all of the stages on the lifecycle for a Business Object
         :param businessObjectDefinitionId:
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Lifecycle.GetStagesResponse
        """
        self.validate_path_param(businessObjectDefinitionId)
        response = await self.get(
            f"/api/V1/{businessObjectDefinitionId}/lifecycle/stages"
        )
        return parse_obj_as(
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Lifecycle.GetStagesResponse,
            response,
        )

    async def GetStatuses(
        self,
        businessObjectDefinitionId: str,
    ) -> cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Lifecycle.GetStatusesResponse:
        """Get lifecycle statuses

        Gets all of the statuses on the lifecycle for a Business Object
         :param businessObjectDefinitionId:
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Lifecycle.GetStatusesResponse
        """
        self.validate_path_param(businessObjectDefinitionId)
        response = await self.get(
            f"/api/V1/{businessObjectDefinitionId}/lifecycle/statuses"
        )
        return parse_obj_as(
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Lifecycle.GetStatusesResponse,
            response,
        )

    async def GetTransitions(
        self,
        businessObjectDefinitionId: str,
    ) -> cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Lifecycle.GetTransitionsResponse:
        """Get lifecycle transitions

        Gets all of the transitions on the lifecycle for a Business Object
         :param businessObjectDefinitionId:
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Lifecycle.GetTransitionsResponse
        """
        self.validate_path_param(businessObjectDefinitionId)
        response = await self.get(
            f"/api/V1/{businessObjectDefinitionId}/lifecycle/transitions"
        )
        return parse_obj_as(
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Lifecycle.GetTransitionsResponse,
            response,
        )

    async def GetRecordStatus(
        self,
        businessObjectDefinitionId: str,
        recordId: str,
    ) -> cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Lifecycle.GetRecordStatusResponse:
        """Get current lifecycle status for record

        Gets the current lifecycle status of a business object record
         :param businessObjectDefinitionId:
         :param recordId:
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Lifecycle.GetRecordStatusResponse
        """
        self.validate_path_param(businessObjectDefinitionId)
        self.validate_path_param(recordId)
        response = await self.get(
            f"/api/V1/{businessObjectDefinitionId}/records/{recordId}/status"
        )
        return parse_obj_as(
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Lifecycle.GetRecordStatusResponse,
            response,
        )

    async def GetRecordStage(
        self,
        businessObjectDefinitionId: str,
        recordId: str,
    ) -> cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Lifecycle.GetRecordStatusResponse:
        """Get current lifecycle stage for record

        Gets the current lifecycle stage of a business object record
         :param businessObjectDefinitionId:
         :param recordId:
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Lifecycle.GetRecordStatusResponse
        """
        self.validate_path_param(businessObjectDefinitionId)
        self.validate_path_param(recordId)
        response = await self.get(
            f"/api/V1/{businessObjectDefinitionId}/records/{recordId}/stage"
        )
        return parse_obj_as(
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Lifecycle.GetRecordStatusResponse,
            response,
        )

    async def GetTransitionOptions(
        self,
        businessObjectDefinitionId: str,
        recordId: str,
    ) -> cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Lifecycle.GetTransitionOptionsResponse:
        """Get lifecycle transition options for record

        Gets the lifecycle transition options currently available to a business object record
         :param businessObjectDefinitionId:
         :param recordId:
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Lifecycle.GetTransitionOptionsResponse
        """
        self.validate_path_param(businessObjectDefinitionId)
        self.validate_path_param(recordId)
        response = await self.get(
            f"/api/V1/{businessObjectDefinitionId}/records/{recordId}/transitionOptions"
        )
        return parse_obj_as(
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Lifecycle.GetTransitionOptionsResponse,
            response,
        )

    async def TransitionRecord(
        self,
        businessObjectDefinitionId: str,
        recordId: str,
        transitionRecordRequest: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Lifecycle.TransitionRecordRequest,
    ) -> cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.ResponseBase:
        """Transition a business object record

        Transitions a business object record in to the specified lifecycle status
         :param businessObjectDefinitionId:
         :param recordId:
         :param transitionRecordRequest: The request body
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.ResponseBase
        """
        self.validate_path_param(businessObjectDefinitionId)
        self.validate_path_param(recordId)
        response = await self.post_body(
            f"/api/V1/{businessObjectDefinitionId}/records/{recordId}/transitions",
            content=transitionRecordRequest.json(exclude_unset=True, by_alias=True),
        )
        return parse_obj_as(
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.ResponseBase,
            response,
        )
