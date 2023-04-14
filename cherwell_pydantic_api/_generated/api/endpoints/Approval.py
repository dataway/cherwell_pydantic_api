from typing import Any, Literal, Optional  # type: ignore

import cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Approval
import cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject
from cherwell_pydantic_api.generated_api_utils import GeneratedInterfaceBase


class ApprovalInterface(GeneratedInterfaceBase):
    async def ActionApprovalV1(
        self,
        approvalRecId: str,
        approvalAction: str,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.SaveResponse
    ):
        """Action an Approval

        Operation that actions an Approval Business Object. Use this method, passing either approve, abstain or deny to update the Business Object's state
         :param approvalRecId:
         :param approvalAction:
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.SaveResponse
        """
        self.validate_path_param(approvalRecId, str)
        self.validate_path_param(approvalAction, str)
        response = await self.post(f"/api/V1/approval/{approvalRecId}/{approvalAction}")
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.SaveResponse,
        )

    async def GetApprovalByRecIdV1(
        self,
        approvalRecId: str,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Approval.ApprovalReadResponse
    ):
        """Get Approval

        Operation that returns an Approval Business Object.  Use the provided links to action the Approval
         :param approvalRecId:
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Approval.ApprovalReadResponse
        """
        self.validate_path_param(approvalRecId, str)
        response = await self.get(f"/api/V1/approval/{approvalRecId}")
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Approval.ApprovalReadResponse,
        )

    async def GetMyApprovalsV1(
        self,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Approval.GetApprovalsResponse
    ):
        """Get all waiting Approvals for the current user

        Operation that returns a list of Approval Business Objects that are in a state of 'Waiting' for the current user.  Use the provided links to action the Approval
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Approval.GetApprovalsResponse
        """
        response = await self.get("/api/V1/getmyapprovals")
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Approval.GetApprovalsResponse,
        )

    async def GetMyPendingApprovalsV1(
        self,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Approval.GetApprovalsResponse
    ):
        """Get all waiting approvals that were created by the current user

        Operation that returns a list of Approval Business Objects that are in a state of 'Waiting' that were created by the current user.  Use the provided links to action the Approval
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Approval.GetApprovalsResponse
        """
        response = await self.get("/api/V1/getmypendingapprovals")
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Approval.GetApprovalsResponse,
        )
