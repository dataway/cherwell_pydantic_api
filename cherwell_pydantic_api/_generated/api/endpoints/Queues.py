from typing import Any, Literal, Optional  # type: ignore

import cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core
import cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Queues
from cherwell_pydantic_api.generated_api_utils import GeneratedInterfaceBase


class QueuesInterface(GeneratedInterfaceBase):
    async def AddItemToQueueV1(
        self,
        request: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Queues.AddItemToQueueRequest,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Queues.AddItemToQueueResponse
    ):
        """Add a Business Object to a queue

        Operation to add a Business Object to a queue
         :param request: Request object containing all properties necessary to add an item to a queue. All properties are required. The standin key defines the queue to which we want to add the Business Object.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Queues.AddItemToQueueResponse
        """
        response = await self.post_body(
            "/api/V1/additemtoqueue",
            content=request.model_dump_json(exclude_unset=True, by_alias=True),
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Queues.AddItemToQueueResponse,
        )

    async def CheckInQueueItemV1(
        self,
        request: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Queues.CheckInQueueItemRequest,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Queues.CheckInQueueItemResponse
    ):
        """Check a Business Object in to a queue

        Operation to check in a queue item
         :param request: The request object for checking in an item to a queue. All properties are required except for historyNotes
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Queues.CheckInQueueItemResponse
        """
        response = await self.post_body(
            "/api/V1/checkinqueueitem",
            content=request.model_dump_json(exclude_unset=True, by_alias=True),
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Queues.CheckInQueueItemResponse,
        )

    async def CheckOutQueueItemV1(
        self,
        request: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Queues.CheckOutQueueItemRequest,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Queues.CheckOutQueueItemResponse
    ):
        """Check a Business Object out of a queue

        Operation to check out a queue item
         :param request: The request object for checking out an item from a queue. All properties are required except for historyNotes
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Queues.CheckOutQueueItemResponse
        """
        response = await self.post_body(
            "/api/V1/checkoutqueueitem",
            content=request.model_dump_json(exclude_unset=True, by_alias=True),
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Queues.CheckOutQueueItemResponse,
        )

    async def GetQueuesFolderV1(
        self,
        scope: str,
        scopeowner: str,
        folder: str,
        links: Optional[bool] = None,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
    ):
        """Get available queues.

        Get available queues for a specific Business Object type based on scope, scope owner, and folder.
         :param scope: The scope to get available queues for.
         :param scopeowner: The scope owner to get available queues for.
         :param folder: The folder to get available queues for.  This has to be the folder ID which can be retrieved by doing a getqueues operation without the folder including links option then the links will have the folder IDs.
         :param links: Whether or not to include links.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
        """
        self.validate_path_param(scope, str)
        self.validate_path_param(scopeowner, str)
        self.validate_path_param(folder, str)
        params: dict[str, Any] = {}
        if links is not None:
            params["links"] = links
        response = await self.get(
            f"/api/V1/getqueues/scope/{scope}/scopeowner/{scopeowner}/folder/{folder}",
            params=params,
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData,
        )

    async def GetQueuesScopeOwnerV1(
        self,
        scope: str,
        scopeowner: str,
        links: Optional[bool] = None,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
    ):
        """Get available queues.

        Get available queues for a specific Business Object type based on scope, and scope owner.
         :param scope: The scope to get available queues for.
         :param scopeowner: The scope owner to get available queues for.
         :param links: Whether or not to include links.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
        """
        self.validate_path_param(scope, str)
        self.validate_path_param(scopeowner, str)
        params: dict[str, Any] = {}
        if links is not None:
            params["links"] = links
        response = await self.get(
            f"/api/V1/getqueues/scope/{scope}/scopeowner/{scopeowner}", params=params
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData,
        )

    async def GetQueuesScopeV1(
        self,
        scope: str,
        links: Optional[bool] = None,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
    ):
        """Get available queues.

        Get available queues for a specific Business Object type based on scope.
         :param scope: The scope to get available queues for.
         :param links: Whether or not to include links.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
        """
        self.validate_path_param(scope, str)
        params: dict[str, Any] = {}
        if links is not None:
            params["links"] = links
        response = await self.get(f"/api/V1/getqueues/scope/{scope}", params=params)
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData,
        )

    async def GetQueuesV1(
        self,
        links: Optional[bool] = None,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
    ):
        """Get available queues.

        Get available queues for a specific Business Object.
         :param links: Whether or not to include links.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
        """
        params: dict[str, Any] = {}
        if links is not None:
            params["links"] = links
        response = await self.get("/api/V1/getqueues", params=params)
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData,
        )

    async def RemoveItemFromQueueV1(
        self,
        request: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Queues.RemoveItemFromQueueRequest,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Queues.RemoveItemFromQueueResponse
    ):
        """Remove an item from a queue

        Operation to remove an item from a queue
         :param request: The request object to remove an item from a queue. All properties are required except for historyNotes
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Queues.RemoveItemFromQueueResponse
        """
        response = await self.post_body(
            "/api/V1/removeitemfromqueue",
            content=request.model_dump_json(exclude_unset=True, by_alias=True),
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Queues.RemoveItemFromQueueResponse,
        )
