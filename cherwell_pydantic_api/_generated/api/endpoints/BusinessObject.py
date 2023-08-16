from typing import Any, Literal, Optional  # type: ignore

import cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts
import cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject
import cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches
import cherwell_pydantic_api.types
from cherwell_pydantic_api.generated_api_utils import GeneratedInterfaceBase


class BusinessObjectInterface(GeneratedInterfaceBase):
    async def DeleteBusinessObjectBatchV1(
        self,
        request: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.BatchDeleteRequest,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.BatchDeleteResponse
    ):
        """Delete Business Objects in a batch

        Operation to delete a batch of Business Objects.
         :param request: Specify an array of Business Object IDs and record IDs or public IDs. Use a flag to stop on error or continue on error.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.BatchDeleteResponse
        """
        response = await self.post_body(
            "/api/V1/deletebusinessobjectbatch",
            content=request.model_dump_json(exclude_unset=True, by_alias=True),
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.BatchDeleteResponse,
        )

    async def DeleteBusinessObjectByPublicIdV1(
        self,
        busobid: cherwell_pydantic_api.types.BusObIDParamType,
        publicid: str,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.DeleteResponse
    ):
        """Delete a Business Object by public ID

        Operation to delete a Business Object by Business Object ID.
         :param busobid: Specify the Business Object ID.
         :param publicid: Specify the Business Object public ID.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.DeleteResponse
        """
        self.validate_path_param(busobid, cherwell_pydantic_api.types.BusObIDParamType)
        self.validate_path_param(publicid, str)
        response = await self.delete(
            f"/api/V1/deletebusinessobject/busobid/{busobid}/publicid/{publicid}"
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.DeleteResponse,
        )

    async def DeleteBusinessObjectByRecIdV1(
        self,
        busobid: cherwell_pydantic_api.types.BusObIDParamType,
        busobrecid: cherwell_pydantic_api.types.BusObRecID,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.DeleteResponse
    ):
        """Delete a Business Object by record ID

        Operation to delete a single Business Object.
         :param busobid: Specify the Business Object ID.
         :param busobrecid:  Specify the Business Object record ID.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.DeleteResponse
        """
        self.validate_path_param(busobid, cherwell_pydantic_api.types.BusObIDParamType)
        self.validate_path_param(busobrecid, cherwell_pydantic_api.types.BusObRecID)
        response = await self.delete(
            f"/api/V1/deletebusinessobject/busobid/{busobid}/busobrecid/{busobrecid}"
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.DeleteResponse,
        )

    async def DeleteRelatedBusinessObjectByPublicIdV1(
        self,
        parentbusobid: cherwell_pydantic_api.types.BusObIDParamType,
        parentbusobrecid: cherwell_pydantic_api.types.BusObRecID,
        relationshipid: cherwell_pydantic_api.types.RelationshipID,
        publicid: str,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.RelatedBusinessObjectResponse
    ):
        """Delete a related Business Object by public ID

        Operation to delete a related Business Object. (Use "Unlink Related Business Object" to unlink two Business Objects rather that deleting the related Business Object.)
         :param parentbusobid: Specify the Business Object ID for the parent Business Object.
         :param parentbusobrecid: Specify the record ID for the parent Business Object
         :param relationshipid: Specify the Relationship ID for the related Business Object you want to delete.
         :param publicid: Specify the public ID for the related Business Object you want to delete. Use only for Business Objects with unique public IDs. Use "Delete a related Business Object by record ID" when public IDs are not unique.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.RelatedBusinessObjectResponse
        """
        self.validate_path_param(
            parentbusobid, cherwell_pydantic_api.types.BusObIDParamType
        )
        self.validate_path_param(
            parentbusobrecid, cherwell_pydantic_api.types.BusObRecID
        )
        self.validate_path_param(
            relationshipid, cherwell_pydantic_api.types.RelationshipID
        )
        self.validate_path_param(publicid, str)
        response = await self.delete(
            f"/api/V1/deleterelatedbusinessobject/parentbusobid/{parentbusobid}/parentbusobrecid/{parentbusobrecid}/relationshipid/{relationshipid}/publicid/{publicid}"
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.RelatedBusinessObjectResponse,
        )

    async def DeleteRelatedBusinessObjectByRecIdV1(
        self,
        parentbusobid: cherwell_pydantic_api.types.BusObIDParamType,
        parentbusobrecid: cherwell_pydantic_api.types.BusObRecID,
        relationshipid: cherwell_pydantic_api.types.RelationshipID,
        busobrecid: cherwell_pydantic_api.types.BusObRecID,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.RelatedBusinessObjectResponse
    ):
        """Delete a related Business Object by record ID

        Operation to delete a related Business Object. (Use "Unlink Related Business Object" to unlink two Business Objects rather that deleting the related Business Object.)
         :param parentbusobid: Specify the Business Object ID for the parent Business Object.
         :param parentbusobrecid: Specify the record ID for the parent Business Object
         :param relationshipid: Specify the Relationship ID for the related Business Object you want to delete.
         :param busobrecid: Specify the record ID for the related Business Object you want to delete.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.RelatedBusinessObjectResponse
        """
        self.validate_path_param(
            parentbusobid, cherwell_pydantic_api.types.BusObIDParamType
        )
        self.validate_path_param(
            parentbusobrecid, cherwell_pydantic_api.types.BusObRecID
        )
        self.validate_path_param(
            relationshipid, cherwell_pydantic_api.types.RelationshipID
        )
        self.validate_path_param(busobrecid, cherwell_pydantic_api.types.BusObRecID)
        response = await self.delete(
            f"/api/V1/deleterelatedbusinessobject/parentbusobid/{parentbusobid}/parentbusobrecid/{parentbusobrecid}/relationshipid/{relationshipid}/busobrecid/{busobrecid}"
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.RelatedBusinessObjectResponse,
        )

    async def FieldValuesLookupV1(
        self,
        request: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.FieldValuesLookupRequest,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.FieldValuesLookupResponse
    ):
        """Get lookup values for fields

        Operation to get potentially valid values for Business Object fields.
         :param request: Request object that specifies the Business Object and fields for which values are to be returned.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.FieldValuesLookupResponse
        """
        response = await self.post_body(
            "/api/V1/fieldvalueslookup",
            content=request.model_dump_json(exclude_unset=True, by_alias=True),
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.FieldValuesLookupResponse,
        )

    async def GetActivitiesV1(
        self,
        busobid: cherwell_pydantic_api.types.BusObIDParamType,
        busobrecid: cherwell_pydantic_api.types.BusObRecID,
        pageSize: int,
        pageNumber: Optional[int] = None,
        activityType: Optional[
            Literal["All", "Audit", "Communication", "Notes", "Pinned"]
        ] = None,
    ) -> list[
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.BusObActivity
    ]:
        """Retrieve all activities for a business object

        Operation to retrieve all activities for a business object. Activities are mapped to history tracking business objects.
         :param busobid: Specify the Business Object ID.
         :param busobrecid: Specify the Business Object record ID.
         :param pageSize: Specify the number of rows to return per page. Maximum value is 2000 per page.
         :param pageNumber: Specify the page number of the result set to return.
         :param activityType: The category of activities to retrieve. Will default to All if not specified.
         :return: list[cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.BusObActivity]
        """
        self.validate_path_param(busobid, cherwell_pydantic_api.types.BusObIDParamType)
        self.validate_path_param(busobrecid, cherwell_pydantic_api.types.BusObRecID)
        params: dict[str, Any] = {}
        if pageNumber is not None:
            params["pageNumber"] = pageNumber
        if activityType is not None:
            params["activityType"] = activityType
        response = await self.get(
            f"/api/V1/getactivities/busobid/{busobid}/busobrecid/{busobrecid}/pagesize/{pageSize}",
            params=params,
        )
        return self.parse_response(
            response,
            list[
                cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.BusObActivity
            ],
        )

    async def GetBusinessObjectAttachmentByAttachmentIdV1(
        self,
        attachmentid: str,
        busobid: cherwell_pydantic_api.types.BusObIDParamType,
        busobrecid: cherwell_pydantic_api.types.BusObRecID,
    ) -> cherwell_pydantic_api.types.FileDownload:
        """Get an imported Business Object attachment

        Operation to get a Business Object attachment that has been imported into the system.  HTTP Range Header can be used but is optional.
         :param attachmentid: Specify the internal ID of the attachment record that contains information about the imported file.
         :param busobid: Specify the Business Object ID.
         :param busobrecid: Specify the Business Object record ID.
         :return: cherwell_pydantic_api.types.FileDownload"""
        self.validate_path_param(attachmentid, str)
        self.validate_path_param(busobid, cherwell_pydantic_api.types.BusObIDParamType)
        self.validate_path_param(busobrecid, cherwell_pydantic_api.types.BusObRecID)
        response = await self.get(
            f"/api/V1/getbusinessobjectattachment/attachmentid/{attachmentid}/busobid/{busobid}/busobrecid/{busobrecid}"
        )
        return self.download_response(response)

    async def GetBusinessObjectAttachmentsByIdAndPublicIdV1(
        self,
        busobid: cherwell_pydantic_api.types.BusObIDParamType,
        publicid: str,
        type: cherwell_pydantic_api.types.RecordAttachmentType,
        attachmenttype: cherwell_pydantic_api.types.AttachmentType,
        includelinks: Optional[bool] = None,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.AttachmentsResponse
    ):
        """Get attachments by Business Object public ID

        Operation to get attachments for a Business Object by Business Object ID and public ID.
         :param busobid: Specify the Business Object ID.
         :param publicid: Specify the Business Object public ID for the record that contains the attachments.
         :param type: Record attachment type:

        None - Not applicable to the REST API.

        File - Linked files.

        FileManagerFile - Imported files.

        BusOb - Attached Business Objects.

        History - Information about the attachment, if any is available. For example, an e-mail message may store the name of an attachment sent.

        Other - Not applicable to the REST API.

         :param attachmenttype: For file types, select the type of attachment:

        Imported - Attachment was imported into database.

        Linked - Attachment is linked to an external file.

        URL - Attachment is a URL.
         :param includelinks: Flag to include hyperlinks in results. Default is false.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.AttachmentsResponse
        """
        self.validate_path_param(busobid, cherwell_pydantic_api.types.BusObIDParamType)
        self.validate_path_param(publicid, str)
        self.validate_path_param(type, cherwell_pydantic_api.types.RecordAttachmentType)
        self.validate_path_param(
            attachmenttype, cherwell_pydantic_api.types.AttachmentType
        )
        params: dict[str, Any] = {}
        if includelinks is not None:
            params["includelinks"] = includelinks
        response = await self.get(
            f"/api/V1/getbusinessobjectattachments/busobid/{busobid}/publicid/{publicid}/type/{type}/attachmenttype/{attachmenttype}",
            params=params,
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.AttachmentsResponse,
        )

    async def GetBusinessObjectAttachmentsByIdAndRecIdV1(
        self,
        busobid: cherwell_pydantic_api.types.BusObIDParamType,
        busobrecid: cherwell_pydantic_api.types.BusObRecID,
        type: cherwell_pydantic_api.types.RecordAttachmentType,
        attachmenttype: cherwell_pydantic_api.types.AttachmentType,
        includelinks: Optional[bool] = None,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.AttachmentsResponse
    ):
        """Get attachments by Business Object record ID

        Operation to get attachments for a Business Object by Business Object ID and record ID.
         :param busobid: Specify the Business Object ID.
         :param busobrecid: Specify the Business Object record ID.
         :param type: Record attachment type:

        None - Not applicable to the REST API.

        File - Linked files.

        FileManagerFile - Imported files.

        BusOb - Attached Business Objects.

        History - Information about the attachment, if any is available. For example, an e-mail message may store the name of an attachment sent.

        Other - Not applicable to the REST API.

         :param attachmenttype: For file types, select the type of attachment:

        Imported - Attachment was imported into database.

        Linked - Attachment is linked to an external file.

        URL - Attachment is a URL.
         :param includelinks: Flag to include hyperlinks in results. Default is false.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.AttachmentsResponse
        """
        self.validate_path_param(busobid, cherwell_pydantic_api.types.BusObIDParamType)
        self.validate_path_param(busobrecid, cherwell_pydantic_api.types.BusObRecID)
        self.validate_path_param(type, cherwell_pydantic_api.types.RecordAttachmentType)
        self.validate_path_param(
            attachmenttype, cherwell_pydantic_api.types.AttachmentType
        )
        params: dict[str, Any] = {}
        if includelinks is not None:
            params["includelinks"] = includelinks
        response = await self.get(
            f"/api/V1/getbusinessobjectattachments/busobid/{busobid}/busobrecid/{busobrecid}/type/{type}/attachmenttype/{attachmenttype}",
            params=params,
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.AttachmentsResponse,
        )

    async def GetBusinessObjectAttachmentsByNameAndPublicIdV1(
        self,
        busobname: str,
        publicid: str,
        type: cherwell_pydantic_api.types.RecordAttachmentType,
        attachmenttype: cherwell_pydantic_api.types.AttachmentType,
        includelinks: Optional[bool] = None,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.AttachmentsResponse
    ):
        """Get attachments by Business Object name and public ID

        Operation to get attachments for a Business Object by Business Object Name and public ID.
         :param busobname: Specify the Business Object name.
         :param publicid: Specify the Business Object public ID for the record that contains the attachments.
         :param type: Record attachment type:

        None - Not applicable to the REST API.

        File - Linked files.

        FileManagerFile - Imported files.

        BusOb - Attached Business Objects.

        History - Information about the attachment, if any is available. For example, an e-mail message may store the name of an attachment sent.

        Other - Not applicable to the REST API.

         :param attachmenttype: For file types, select the type of attachment:

        Imported - Attachment was imported into database.

        Linked - Attachment is linked to an external file.

        URL - Attachment is a URL.
         :param includelinks: Flag to include hyperlinks in results. Default is false.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.AttachmentsResponse
        """
        self.validate_path_param(busobname, str)
        self.validate_path_param(publicid, str)
        self.validate_path_param(type, cherwell_pydantic_api.types.RecordAttachmentType)
        self.validate_path_param(
            attachmenttype, cherwell_pydantic_api.types.AttachmentType
        )
        params: dict[str, Any] = {}
        if includelinks is not None:
            params["includelinks"] = includelinks
        response = await self.get(
            f"/api/V1/getbusinessobjectattachments/busobname/{busobname}/publicid/{publicid}/type/{type}/attachmenttype/{attachmenttype}",
            params=params,
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.AttachmentsResponse,
        )

    async def GetBusinessObjectAttachmentsByNameAndRecIdV1(
        self,
        busobname: str,
        busobrecid: cherwell_pydantic_api.types.BusObRecID,
        type: cherwell_pydantic_api.types.RecordAttachmentType,
        attachmenttype: cherwell_pydantic_api.types.AttachmentType,
        includelinks: Optional[bool] = None,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.AttachmentsResponse
    ):
        """Get attachments by Business Object name and record ID

        Operation to get attachments for a Business Object by name and record ID.
         :param busobname: Specify the Business Object name.
         :param busobrecid: Specify the Business Object record ID.
         :param type: Record attachment type:

        None - Not applicable to the REST API.

        File - Linked files.

        FileManagerFile - Imported files.

        BusOb - Attached Business Objects.

        History - Information about the attachment, if any is available. For example, an e-mail message may store the name of an attachment sent.

        Other - Not applicable to the REST API.

         :param attachmenttype: For file types, select the type of attachment:

        Imported - Attachment was imported into database.

        Linked - Attachment is linked to an external file.

        URL - Attachment is a URL.
         :param includelinks: Flag to include hyperlinks in results. Default is false.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.AttachmentsResponse
        """
        self.validate_path_param(busobname, str)
        self.validate_path_param(busobrecid, cherwell_pydantic_api.types.BusObRecID)
        self.validate_path_param(type, cherwell_pydantic_api.types.RecordAttachmentType)
        self.validate_path_param(
            attachmenttype, cherwell_pydantic_api.types.AttachmentType
        )
        params: dict[str, Any] = {}
        if includelinks is not None:
            params["includelinks"] = includelinks
        response = await self.get(
            f"/api/V1/getbusinessobjectattachments/busobname/{busobname}/busobrecid/{busobrecid}/type/{type}/attachmenttype/{attachmenttype}",
            params=params,
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.AttachmentsResponse,
        )

    async def GetBusinessObjectAttachmentsV1(
        self,
        attachmentsRequest: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.AttachmentsRequest,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.AttachmentsResponse
    ):
        """Get Business Object attachments by request object

        Operation to get attachments for a Business Object by attachments request object.
         :param attachmentsRequest: Object with all the parameters to request an attachments list. You can also request a list of types to get more than just one type at a time.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.AttachmentsResponse
        """
        response = await self.post_body(
            "/api/V1/getbusinessobjectattachments",
            content=attachmentsRequest.model_dump_json(
                exclude_unset=True, by_alias=True
            ),
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.AttachmentsResponse,
        )

    async def GetBusinessObjectBatchV1(
        self,
        request: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.BatchReadRequest,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.BatchReadResponse
    ):
        """Get a batch of Business Object records

        Operation that returns a batch of Business Object records that includes a list of field record IDs, display names, and values for each record.
         :param request: Specify an array of Business Object IDs, record IDs, or public IDs. Use a flag to stop on error or continue on error.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.BatchReadResponse
        """
        response = await self.post_body(
            "/api/V1/getbusinessobjectbatch",
            content=request.model_dump_json(exclude_unset=True, by_alias=True),
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.BatchReadResponse,
        )

    async def GetBusinessObjectByPublicIdV1(
        self,
        busobid: cherwell_pydantic_api.types.BusObIDParamType,
        publicid: str,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.ReadResponse
    ):
        """Get a Business Object record

        Operation that returns a Business Object record that includes a list of fields and their record IDs, names, and set values.
         :param busobid: Specify the Business Object ID.
         :param publicid: Specify the Business Object public ID.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.ReadResponse
        """
        self.validate_path_param(busobid, cherwell_pydantic_api.types.BusObIDParamType)
        self.validate_path_param(publicid, str)
        response = await self.get(
            f"/api/V1/getbusinessobject/busobid/{busobid}/publicid/{publicid}"
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.ReadResponse,
        )

    async def GetBusinessObjectByRecIdV1(
        self,
        busobid: cherwell_pydantic_api.types.BusObIDParamType,
        busobrecid: cherwell_pydantic_api.types.BusObRecID,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.ReadResponse
    ):
        """Get a Business Object record

        Operation that returns a Business Object record that includes a list of fields and their record IDs, names, and set values.
         :param busobid: Specify the Business Object ID.
         :param busobrecid: Specify the Business Object record ID.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.ReadResponse
        """
        self.validate_path_param(busobid, cherwell_pydantic_api.types.BusObIDParamType)
        self.validate_path_param(busobrecid, cherwell_pydantic_api.types.BusObRecID)
        response = await self.get(
            f"/api/V1/getbusinessobject/busobid/{busobid}/busobrecid/{busobrecid}"
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.ReadResponse,
        )

    async def GetBusinessObjectByScanCodeBusObIdV1(
        self,
        scanCode: str,
        busobid: cherwell_pydantic_api.types.BusObIDParamType,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.BarcodeLookupResponse
    ):
        """Get a Business Object by its scan code and Business Object ID

        Operation to get a Business Object based on its associated scan code and Business Object ID.
         :param scanCode: The scan code for a Business Object record.
         :param busobid: The Business Object ID.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.BarcodeLookupResponse
        """
        self.validate_path_param(scanCode, str)
        self.validate_path_param(busobid, cherwell_pydantic_api.types.BusObIDParamType)
        response = await self.get(
            f"/api/V1/getbusinessobject/scancode/{scanCode}/busobid/{busobid}"
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.BarcodeLookupResponse,
        )

    async def GetBusinessObjectByScanCodeBusObNameV1(
        self,
        scanCode: str,
        busobname: str,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.BarcodeLookupResponse
    ):
        """Get a Business Object by its scan code and Business Object name

        Operation to get a Business Object based on its associated scan code and Business Object name.
         :param scanCode: The scan code for a Business Object record.
         :param busobname: The Business Bbject name.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.BarcodeLookupResponse
        """
        self.validate_path_param(scanCode, str)
        self.validate_path_param(busobname, str)
        response = await self.get(
            f"/api/V1/getbusinessobject/scancode/{scanCode}/busobname/{busobname}"
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.BarcodeLookupResponse,
        )

    async def GetBusinessObjectSchemaV1(
        self,
        busobId: cherwell_pydantic_api.types.BusObIDParamType,
        includerelationships: Optional[bool] = None,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.SchemaResponse
    ):
        """Get a Business Object schema

        Operation that returns the schema for a Business Object and, optionally, its related Business Objects.
         :param busobId: Specify the Business Object ID.
         :param includerelationships: Flag to include schemas for related Business Object. Default is false.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.SchemaResponse
        """
        self.validate_path_param(busobId, cherwell_pydantic_api.types.BusObIDParamType)
        params: dict[str, Any] = {}
        if includerelationships is not None:
            params["includerelationships"] = includerelationships
        response = await self.get(
            f"/api/V1/getbusinessobjectschema/busobid/{busobId}", params=params
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.SchemaResponse,
        )

    async def GetBusinessObjectSummariesV1(
        self,
        type: cherwell_pydantic_api.types.BusinessObjectType,
    ) -> list[
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.Summary
    ]:
        """Get Business Object summaries by type

        Operation that returns a list of Business Object summaries by type (Major, Supporting, Lookup, Groups, and All).
         :param type: Use to show:
        All - All objects
        Major - Major objects only
        Supporting - Supporting objects only
        Lookup - Lookup objects only
        Groups - Groups only
         :return: list[cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.Summary]
        """
        self.validate_path_param(type, cherwell_pydantic_api.types.BusinessObjectType)
        response = await self.get(f"/api/V1/getbusinessobjectsummaries/type/{type}")
        return self.parse_response(
            response,
            list[
                cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.Summary
            ],
        )

    async def GetBusinessObjectSummaryByIdV1(
        self,
        busobid: cherwell_pydantic_api.types.BusObIDParamType,
    ) -> list[
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.Summary
    ]:
        """Get a Business Object summary by ID

        Operation that returns a single Business Object summary by ID.
         :param busobid: Specify a Business Object ID to get its summary.
         :return: list[cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.Summary]
        """
        self.validate_path_param(busobid, cherwell_pydantic_api.types.BusObIDParamType)
        response = await self.get(f"/api/V1/getbusinessobjectsummary/busobid/{busobid}")
        return self.parse_response(
            response,
            list[
                cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.Summary
            ],
        )

    async def GetBusinessObjectSummaryByNameV1(
        self,
        busobname: str,
    ) -> list[
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.Summary
    ]:
        """Get a Business Object summary by name

        Operation that returns a single Business Object summary by name.
         :param busobname: Specify a Business Object name to get its summary.
         :return: list[cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.Summary]
        """
        self.validate_path_param(busobname, str)
        response = await self.get(
            f"/api/V1/getbusinessobjectsummary/busobname/{busobname}"
        )
        return self.parse_response(
            response,
            list[
                cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.Summary
            ],
        )

    async def GetBusinessObjectTemplateV1(
        self,
        request: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.TemplateRequest,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.TemplateResponse
    ):
        """Get Business Object templates for create

        Operation that returns a template to create Business Objects.  The template includes placeholders for field values. You can then send the template with these values to the Business Object Save operation.
         :param request: Specify the Business Object ID. Use true to include all required fields or all fields. Specify an optional fields list by adding field names in a comma-delimited list ["field1", "field2"].
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.TemplateResponse
        """
        response = await self.post_body(
            "/api/V1/getbusinessobjecttemplate",
            content=request.model_dump_json(exclude_unset=True, by_alias=True),
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.TemplateResponse,
        )

    async def GetRelatedBusinessObjectByRequestV1(
        self,
        relatedBusinessObjectRequest: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.RelatedBusinessObjectRequest,
        includelinks: Optional[bool] = None,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.RelatedBusinessObjectResponse
    ):
        """Get related Business Objects using a request object

        Operation to get related Business Objects for a specific relationship. Specify a list of fields to include in the response. The order of parameter usage and overrides is: all fields set to true overrides default overrides;  custom grid overrides field list settings.
         :param relatedBusinessObjectRequest: Request object containing all the possible parameters to get related Business Objects.
         :param includelinks: Flag to include hyperlinks in results. Default is false.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.RelatedBusinessObjectResponse
        """
        params: dict[str, Any] = {}
        if includelinks is not None:
            params["includelinks"] = includelinks
        response = await self.post_body(
            "/api/V1/getrelatedbusinessobject",
            params=params,
            content=relatedBusinessObjectRequest.model_dump_json(
                exclude_unset=True, by_alias=True
            ),
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.RelatedBusinessObjectResponse,
        )

    async def GetRelatedBusinessObjectV1(
        self,
        parentbusobid: cherwell_pydantic_api.types.BusObIDParamType,
        parentbusobrecid: cherwell_pydantic_api.types.BusObRecID,
        relationshipid: cherwell_pydantic_api.types.RelationshipID,
        pageNumber: Optional[int] = None,
        pageSize: Optional[int] = None,
        allfields: Optional[bool] = None,
        usedefaultgrid: Optional[bool] = None,
        includelinks: Optional[bool] = None,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.RelatedBusinessObjectResponse
    ):
        """Get related Business Objects by ID

        Operation to get the related objects for a Business Object relationship specifying all fields or default grid as the field to return.
         :param parentbusobid: Specify the Business Object ID for the parent Business Object.
         :param parentbusobrecid: Specify the record ID for the parent Business Object.
         :param relationshipid: Specify the Relationship ID for the related Business Object you want to return.
         :param pageNumber: Specify the page number of the result set to return.
         :param pageSize: Specify the number of rows to return per page.
         :param allfields: Flag to include all related Business Object fields.  Default is true if not supplied.  If true, then UseDefaultGrid is not used.
         :param usedefaultgrid: Flag to trigger the use of the related Business Objects default grid for the list of fields to return.
         :param includelinks: Flag to include hyperlinks in results. Default is false.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.RelatedBusinessObjectResponse
        """
        self.validate_path_param(
            parentbusobid, cherwell_pydantic_api.types.BusObIDParamType
        )
        self.validate_path_param(
            parentbusobrecid, cherwell_pydantic_api.types.BusObRecID
        )
        self.validate_path_param(
            relationshipid, cherwell_pydantic_api.types.RelationshipID
        )
        params: dict[str, Any] = {}
        if pageNumber is not None:
            params["pageNumber"] = pageNumber
        if pageSize is not None:
            params["pageSize"] = pageSize
        if allfields is not None:
            params["allfields"] = allfields
        if usedefaultgrid is not None:
            params["usedefaultgrid"] = usedefaultgrid
        if includelinks is not None:
            params["includelinks"] = includelinks
        response = await self.get(
            f"/api/V1/getrelatedbusinessobject/parentbusobid/{parentbusobid}/parentbusobrecid/{parentbusobrecid}/relationshipid/{relationshipid}",
            params=params,
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.RelatedBusinessObjectResponse,
        )

    async def GetRelatedBusinessObjectWithCustomGridV1(
        self,
        parentbusobid: cherwell_pydantic_api.types.BusObIDParamType,
        parentbusobrecid: cherwell_pydantic_api.types.BusObRecID,
        relationshipid: cherwell_pydantic_api.types.RelationshipID,
        gridid: str,
        pageNumber: Optional[int] = None,
        pageSize: Optional[int] = None,
        includelinks: Optional[bool] = None,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.RelatedBusinessObjectResponse
    ):
        """Get related Business Objects custom grid

        Operation to get related Business Objects for a specific relationship. Specify a custom grid ID as the fields to return.
         :param parentbusobid: Specify the Business Object ID for the parent Business Object.
         :param parentbusobrecid: Specify the record ID for the parent Business Object.
         :param relationshipid: Specify the Relationship ID for the related Business Object you want to return.
         :param gridid: Specify the ID for the custom grid that contains the field list.
         :param pageNumber: Specify the page number of the result set to return.
         :param pageSize: Specify the number of rows to return per page.
         :param includelinks: Flag to include hyperlinks in results. Default is false.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.RelatedBusinessObjectResponse
        """
        self.validate_path_param(
            parentbusobid, cherwell_pydantic_api.types.BusObIDParamType
        )
        self.validate_path_param(
            parentbusobrecid, cherwell_pydantic_api.types.BusObRecID
        )
        self.validate_path_param(
            relationshipid, cherwell_pydantic_api.types.RelationshipID
        )
        self.validate_path_param(gridid, str)
        params: dict[str, Any] = {}
        if pageNumber is not None:
            params["pageNumber"] = pageNumber
        if pageSize is not None:
            params["pageSize"] = pageSize
        if includelinks is not None:
            params["includelinks"] = includelinks
        response = await self.get(
            f"/api/V1/getrelatedbusinessobject/parentbusobid/{parentbusobid}/parentbusobrecid/{parentbusobrecid}/relationshipid/{relationshipid}/gridid/{gridid}",
            params=params,
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.RelatedBusinessObjectResponse,
        )

    async def LinkRelatedBusinessObjectByRecIdV1(
        self,
        parentbusobid: cherwell_pydantic_api.types.BusObIDParamType,
        parentbusobrecid: cherwell_pydantic_api.types.BusObRecID,
        relationshipid: cherwell_pydantic_api.types.RelationshipID,
        busobid: cherwell_pydantic_api.types.BusObIDParamType,
        busobrecid: cherwell_pydantic_api.types.BusObRecID,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.RelatedBusinessObjectResponse
    ):
        """Link related Business Objects

        Operation to link related Business Objects.
         :param parentbusobid: Specify the Business Object ID for the parent Business Object.
         :param parentbusobrecid: Specify the record ID for the parent Business Object.
         :param relationshipid: Specify the Relationship ID for the related Business Object you want to link.
         :param busobid: Specify the Business Object ID of the Business Object to be linked.
         :param busobrecid: Specify the Business Object record ID of the Business Object to be linked.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.RelatedBusinessObjectResponse
        """
        self.validate_path_param(
            parentbusobid, cherwell_pydantic_api.types.BusObIDParamType
        )
        self.validate_path_param(
            parentbusobrecid, cherwell_pydantic_api.types.BusObRecID
        )
        self.validate_path_param(
            relationshipid, cherwell_pydantic_api.types.RelationshipID
        )
        self.validate_path_param(busobid, cherwell_pydantic_api.types.BusObIDParamType)
        self.validate_path_param(busobrecid, cherwell_pydantic_api.types.BusObRecID)
        response = await self.get(
            f"/api/V1/linkrelatedbusinessobject/parentbusobid/{parentbusobid}/parentbusobrecid/{parentbusobrecid}/relationshipid/{relationshipid}/busobid/{busobid}/busobrecid/{busobrecid}"
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.RelatedBusinessObjectResponse,
        )

    async def LinkRelatedBusinessObjectByRecIdV2(
        self,
        parentbusobid: cherwell_pydantic_api.types.BusObIDParamType,
        parentbusobrecid: cherwell_pydantic_api.types.BusObRecID,
        relationshipid: cherwell_pydantic_api.types.RelationshipID,
        busobid: cherwell_pydantic_api.types.BusObIDParamType,
        busobrecid: cherwell_pydantic_api.types.BusObRecID,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.ResponseBase
    ):
        """Link related Business Objects

        Operation to link related Business Objects.
         :param parentbusobid: Specify the Business Object ID for the parent Business Object.
         :param parentbusobrecid: Specify the record ID for the parent Business Object.
         :param relationshipid: Specify the Relationship ID for the related Business Object you want to link.
         :param busobid: Specify the Business Object ID of the Business Object to be linked.
         :param busobrecid: Specify the Business Object record ID of the Business Object to be linked.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.ResponseBase
        """
        self.validate_path_param(
            parentbusobid, cherwell_pydantic_api.types.BusObIDParamType
        )
        self.validate_path_param(
            parentbusobrecid, cherwell_pydantic_api.types.BusObRecID
        )
        self.validate_path_param(
            relationshipid, cherwell_pydantic_api.types.RelationshipID
        )
        self.validate_path_param(busobid, cherwell_pydantic_api.types.BusObIDParamType)
        self.validate_path_param(busobrecid, cherwell_pydantic_api.types.BusObRecID)
        response = await self.get(
            f"/api/V2/linkrelatedbusinessobject/parentbusobid/{parentbusobid}/parentbusobrecid/{parentbusobrecid}/relationshipid/{relationshipid}/busobid/{busobid}/busobrecid/{busobrecid}"
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.ResponseBase,
        )

    async def RemoveBusinessObjectAttachmentByIdAndPublicIdV1(
        self,
        attachmentid: str,
        busobid: cherwell_pydantic_api.types.BusObIDParamType,
        publicid: str,
    ) -> None:
        """Remove an attachment by Business Object ID and public ID

        Operation to remove an attachment from a Business Object using the attachment record ID, Business Object ID, and Business Object public ID.
         :param attachmentid: Specify the internal ID of the attachment record.
         :param busobid: Specify the Business Object ID.
         :param publicid: Specify the Business Object public ID.
         :return: None"""
        self.validate_path_param(attachmentid, str)
        self.validate_path_param(busobid, cherwell_pydantic_api.types.BusObIDParamType)
        self.validate_path_param(publicid, str)
        response = await self.delete(
            f"/api/V1/removebusinessobjectattachment/attachmentid/{attachmentid}/busobid/{busobid}/publicid/{publicid}"
        )
        self.check_response(response)

    async def RemoveBusinessObjectAttachmentByIdAndRecIdV1(
        self,
        attachmentid: str,
        busobid: cherwell_pydantic_api.types.BusObIDParamType,
        busobrecid: cherwell_pydantic_api.types.BusObRecID,
    ) -> None:
        """Remove an attachment by Business Object ID and record ID

        Operation to remove an attachment from a Business Object using the attachment record ID, Business Object ID, and Business Object record ID.
         :param attachmentid: Specify the internal ID of the attachment record.
         :param busobid: Specify the Business Object ID.
         :param busobrecid: Specify the Business Object record ID.
         :return: None"""
        self.validate_path_param(attachmentid, str)
        self.validate_path_param(busobid, cherwell_pydantic_api.types.BusObIDParamType)
        self.validate_path_param(busobrecid, cherwell_pydantic_api.types.BusObRecID)
        response = await self.delete(
            f"/api/V1/removebusinessobjectattachment/attachmentid/{attachmentid}/busobid/{busobid}/busobrecid/{busobrecid}"
        )
        self.check_response(response)

    async def RemoveBusinessObjectAttachmentByNameAndPublicIdV1(
        self,
        attachmentid: str,
        busobname: str,
        publicid: str,
    ) -> None:
        """Remove an attachment by Business Object name and public ID

        Operation to remove an attachment from a Business Object using the attachment record ID, Business Object name, and Business Object record ID.
         :param attachmentid: Specify the internal ID of the attachment record.
         :param busobname: Specify the Business Object name.
         :param publicid: Specify the Business Object public ID.
         :return: None"""
        self.validate_path_param(attachmentid, str)
        self.validate_path_param(busobname, str)
        self.validate_path_param(publicid, str)
        response = await self.delete(
            f"/api/V1/removebusinessobjectattachment/attachmentid/{attachmentid}/busobname/{busobname}/publicid/{publicid}"
        )
        self.check_response(response)

    async def RemoveBusinessObjectAttachmentByNameAndRecIdV1(
        self,
        attachmentid: str,
        busobname: str,
        busobrecid: cherwell_pydantic_api.types.BusObRecID,
    ) -> None:
        """Remove an attachment by Business Object name and record ID

        Operation to remove an attachment from a Business Object using the attachment record ID, Business Object name, and Business Object public ID.
         :param attachmentid: Specify the internal ID of the attachment record.
         :param busobname: Specify the Business Object name.
         :param busobrecid: Specify the Business Object record ID.
         :return: None"""
        self.validate_path_param(attachmentid, str)
        self.validate_path_param(busobname, str)
        self.validate_path_param(busobrecid, cherwell_pydantic_api.types.BusObRecID)
        response = await self.delete(
            f"/api/V1/removebusinessobjectattachment/attachmentid/{attachmentid}/busobname/{busobname}/busobrecid/{busobrecid}"
        )
        self.check_response(response)

    async def SaveBusinessObjectAttachmentBusObV1(
        self,
        request: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.SaveBusObAttachmentRequest,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.AttachmentsResponse
    ):
        """Attach a Business Object to a Business Object

        Operation to attach a Business Object to a Business Object. This links the Business Object but does not create a relationship between the two. (Use "Link Related Business Objects" to create a relationship.)
         :param request: Request object used to specify the Business Objects to attach. You can use Business Object name or ID and Business Object record ID or public ID.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.AttachmentsResponse
        """
        response = await self.post_body(
            "/api/V1/savebusinessobjectattachmentbusob",
            content=request.model_dump_json(exclude_unset=True, by_alias=True),
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.AttachmentsResponse,
        )

    async def SaveBusinessObjectAttachmentLinkV1(
        self,
        request: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.SaveLinkAttachmentRequest,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.AttachmentsResponse
    ):
        """Attach a file via UNC

        Operation to attach a file to a Business Object via a path (UNC recommended).
         :param request: Request object used to specify the file path (UNC recommended) and the Business Object. You can use Business Object name or ID and Business Object record ID or public ID.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.AttachmentsResponse
        """
        response = await self.post_body(
            "/api/V1/savebusinessobjectattachmentlink",
            content=request.model_dump_json(exclude_unset=True, by_alias=True),
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.AttachmentsResponse,
        )

    async def SaveBusinessObjectAttachmentUrlV1(
        self,
        request: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.SaveUrlAttachmentRequest,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.AttachmentsResponse
    ):
        """Attach a URL path

        Operation to attach a URL path to a Business Object.
         :param request: Request object used to specify the URL path and Business Object. You can use Business Object name or ID and Business Object record ID or public ID.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.AttachmentsResponse
        """
        response = await self.post_body(
            "/api/V1/savebusinessobjectattachmenturl",
            content=request.model_dump_json(exclude_unset=True, by_alias=True),
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.AttachmentsResponse,
        )

    async def SaveBusinessObjectBatchV1(
        self,
        request: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.BatchSaveRequest,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.BatchSaveResponse
    ):
        """Create or update a batch of Business Objects

        Operation that creates or updates an array of Business Objects in a batch. To update, specify record ID or public ID. To create, leave record ID and public ID empty.
         :param request: Specify the array of Business Object templates.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.BatchSaveResponse
        """
        response = await self.post_body(
            "/api/V1/savebusinessobjectbatch",
            content=request.model_dump_json(exclude_unset=True, by_alias=True),
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.BatchSaveResponse,
        )

    async def SaveBusinessObjectV1(
        self,
        request: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.SaveRequest,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.SaveResponse
    ):
        """Create or Update a Business Object

        Operation that creates a new Business Object or updates an existing Business Object. To create, leave record ID and public ID empty. Upon creating or saving, a cache key is returned to use for subsequent requests. If the object is not found in the cache with said cache key, specify record ID or public ID to save and return a new cache key. Set persist = true, to actually save the Business Object to disk, persist = false will just cache it.
         :param request: Specify a list of fields from a Business Object template.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.SaveResponse
        """
        response = await self.post_body(
            "/api/V1/savebusinessobject",
            content=request.model_dump_json(exclude_unset=True, by_alias=True),
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.SaveResponse,
        )

    async def SaveRelatedBusinessObjectV1(
        self,
        request: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.RelatedSaveRequest,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.RelatedSaveResponse
    ):
        """Create or update a related Business Object

        Operation that creates or updates a related Business Object. To update, specify record ID or public ID. To create, leave record ID and public ID empty.
         :param request: Request object specifying the parent the Business Object, the Relationship, and field values for the Business Object to create or update.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.RelatedSaveResponse
        """
        response = await self.post_body(
            "/api/V1/saverelatedbusinessobject",
            content=request.model_dump_json(exclude_unset=True, by_alias=True),
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject.RelatedSaveResponse,
        )

    async def UnLinkRelatedBusinessObjectByRecIdV1(
        self,
        parentbusobid: cherwell_pydantic_api.types.BusObIDParamType,
        parentbusobrecid: cherwell_pydantic_api.types.BusObRecID,
        relationshipid: cherwell_pydantic_api.types.RelationshipID,
        busobid: cherwell_pydantic_api.types.BusObIDParamType,
        busobrecid: cherwell_pydantic_api.types.BusObRecID,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.RelatedBusinessObjectResponse
    ):
        """UnLink related Business Objects

        Operation to unlink related Business Objects.
         :param parentbusobid: Specify the Business Object ID for the parent Business Object.
         :param parentbusobrecid: Specify the record ID for the parent Business Object.
         :param relationshipid: Specify the Relationship ID for the related Business Object you want to unlink.
         :param busobid: Specify the Business Object ID of the Business Object to be unlinked.
         :param busobrecid: Specify the Business Object record ID of the Business Object to be unlinked.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.RelatedBusinessObjectResponse
        """
        self.validate_path_param(
            parentbusobid, cherwell_pydantic_api.types.BusObIDParamType
        )
        self.validate_path_param(
            parentbusobrecid, cherwell_pydantic_api.types.BusObRecID
        )
        self.validate_path_param(
            relationshipid, cherwell_pydantic_api.types.RelationshipID
        )
        self.validate_path_param(busobid, cherwell_pydantic_api.types.BusObIDParamType)
        self.validate_path_param(busobrecid, cherwell_pydantic_api.types.BusObRecID)
        response = await self.delete(
            f"/api/V1/unlinkrelatedbusinessobject/parentbusobid/{parentbusobid}/parentbusobrecid/{parentbusobrecid}/relationshipid/{relationshipid}/busobid/{busobid}/busobrecid/{busobrecid}"
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.RelatedBusinessObjectResponse,
        )

    async def UploadBusinessObjectAttachmentByIdAndPublicIdV1(
        self,
        body: cherwell_pydantic_api.types.FileUpload,
        filename: str,
        busobid: cherwell_pydantic_api.types.BusObIDParamType,
        publicid: str,
        offset: int,
        totalsize: int,
        attachmentid: Optional[str] = None,
        displaytext: Optional[str] = None,
    ) -> cherwell_pydantic_api.types.StringResponse:
        """Upload an attachment by Business Object ID and public ID

        Operation to upload an attachment to a Business Object record using a Business Object ID and public ID. The body of the request is the byte array of the file part being uploaded.
         :param body: The request body
         :param filename: Specify the name of the file being uploaded. If no attachment name is provided, the file name is used.
         :param busobid: Specify the Business Object ID.
         :param publicid: Specify the Business Object public ID  to attach the file to.
         :param offset: The offset is the starting index of the file part being uploaded.  If this is the first part then the offset will be zero.
         :param totalsize: The entire file size in bytes.
         :param attachmentid: Specify the attachment ID of an uploaded file to upload subsequent parts and ensure each part gets appended to the parts that have already been uploaded.
         :param displaytext: Specify the attachment name, which is the display text for the attachment record.
         :return: cherwell_pydantic_api.types.StringResponse"""
        self.validate_path_param(filename, str)
        self.validate_path_param(busobid, cherwell_pydantic_api.types.BusObIDParamType)
        self.validate_path_param(publicid, str)
        params: dict[str, Any] = {}
        if attachmentid is not None:
            params["attachmentid"] = attachmentid
        if displaytext is not None:
            params["displaytext"] = displaytext
        response = await self.post_body(
            f"/api/V1/uploadbusinessobjectattachment/filename/{filename}/busobid/{busobid}/publicid/{publicid}/offset/{offset}/totalsize/{totalsize}",
            params=params,
            content=body,
            content_type="application/octet-stream",
        )
        return self.parse_response(response, cherwell_pydantic_api.types.StringResponse)

    async def UploadBusinessObjectAttachmentByIdAndRecIdV1(
        self,
        body: cherwell_pydantic_api.types.FileUpload,
        filename: str,
        busobid: cherwell_pydantic_api.types.BusObIDParamType,
        busobrecid: cherwell_pydantic_api.types.BusObRecID,
        offset: int,
        totalsize: int,
        attachmentid: Optional[str] = None,
        displaytext: Optional[str] = None,
    ) -> cherwell_pydantic_api.types.StringResponse:
        """Upload an attachment by Business Object ID and record ID

        Operation to upload an attachment to a Business Object record using a Business Object ID and record ID. The body of the request is the byte array of the file part being uploaded.
         :param body: The request body
         :param filename: Specify the name of the file being uploaded. If no attachment name is provided, the file name is used.
         :param busobid: Specify the Business Object ID.
         :param busobrecid: Specify the Business Object record ID to attach the file to.
         :param offset: The offset is the starting index of the file part being uploaded.  If this is the first part then the offset will be zero.
         :param totalsize: The entire file size in bytes.
         :param attachmentid: Specify the attachment ID of an uploaded file to upload subsequent parts and ensure each part gets appended to the parts that have already been uploaded.
         :param displaytext: Specify the attachment name, which is the display text for the attachment record.
         :return: cherwell_pydantic_api.types.StringResponse"""
        self.validate_path_param(filename, str)
        self.validate_path_param(busobid, cherwell_pydantic_api.types.BusObIDParamType)
        self.validate_path_param(busobrecid, cherwell_pydantic_api.types.BusObRecID)
        params: dict[str, Any] = {}
        if attachmentid is not None:
            params["attachmentid"] = attachmentid
        if displaytext is not None:
            params["displaytext"] = displaytext
        response = await self.post_body(
            f"/api/V1/uploadbusinessobjectattachment/filename/{filename}/busobid/{busobid}/busobrecid/{busobrecid}/offset/{offset}/totalsize/{totalsize}",
            params=params,
            content=body,
            content_type="application/octet-stream",
        )
        return self.parse_response(response, cherwell_pydantic_api.types.StringResponse)

    async def UploadBusinessObjectAttachmentByNameAndPublicIdV1(
        self,
        body: cherwell_pydantic_api.types.FileUpload,
        filename: str,
        busobname: str,
        publicid: str,
        offset: int,
        totalsize: int,
        attachmentid: Optional[str] = None,
        displaytext: Optional[str] = None,
    ) -> cherwell_pydantic_api.types.StringResponse:
        """Upload an attachment by Business Object name and public ID

        Operation to upload an attachment to a Business Object record using a Business Object name and public ID. The body of the request is the byte array of the file part being uploaded.
         :param body: The request body
         :param filename: Specify the name of the file being uploaded. If no attachment name is provided, the file name is used.
         :param busobname: Specify the Business Object name.
         :param publicid: Specify the Business Object public ID  to attach the file to.
         :param offset: The offset is the starting index of the file part being uploaded.  If this is the first part then the offset will be zero.
         :param totalsize: The entire file size in bytes.
         :param attachmentid: Specify the attachment ID of an uploaded file to upload subsequent parts and ensure each part gets appended to the parts that have already been uploaded.
         :param displaytext: Specify the attachment name, which is the display text for the attachment record.
         :return: cherwell_pydantic_api.types.StringResponse"""
        self.validate_path_param(filename, str)
        self.validate_path_param(busobname, str)
        self.validate_path_param(publicid, str)
        params: dict[str, Any] = {}
        if attachmentid is not None:
            params["attachmentid"] = attachmentid
        if displaytext is not None:
            params["displaytext"] = displaytext
        response = await self.post_body(
            f"/api/V1/uploadbusinessobjectattachment/filename/{filename}/busobname/{busobname}/publicid/{publicid}/offset/{offset}/totalsize/{totalsize}",
            params=params,
            content=body,
            content_type="application/octet-stream",
        )
        return self.parse_response(response, cherwell_pydantic_api.types.StringResponse)

    async def UploadBusinessObjectAttachmentByNameAndRecIdV1(
        self,
        body: cherwell_pydantic_api.types.FileUpload,
        filename: str,
        busobname: str,
        busobrecid: cherwell_pydantic_api.types.BusObRecID,
        offset: int,
        totalsize: int,
        attachmentid: Optional[str] = None,
        displaytext: Optional[str] = None,
    ) -> cherwell_pydantic_api.types.StringResponse:
        """Upload an attachment by Business Object name and record ID

        Operation to upload an attachment to a Business Object record using a Business Object name and record ID. The body of the request is the byte array of the file part being uploaded.
         :param body: The request body
         :param filename: Specify the name of the file being uploaded. If no attachment name is provided, the file name is used.
         :param busobname: Specify the Business Object name.
         :param busobrecid: Specify the Business Object record ID to attach the file to.
         :param offset: The offset is the starting index of the file part being uploaded.  If this is the first part then the offset will be zero.
         :param totalsize: The entire file size in bytes.
         :param attachmentid: Specify the attachment ID of an uploaded file to upload subsequent parts and ensure each part gets appended to the parts that have already been uploaded.
         :param displaytext: Specify the attachment name, which is the display text for the attachment record.
         :return: cherwell_pydantic_api.types.StringResponse"""
        self.validate_path_param(filename, str)
        self.validate_path_param(busobname, str)
        self.validate_path_param(busobrecid, cherwell_pydantic_api.types.BusObRecID)
        params: dict[str, Any] = {}
        if attachmentid is not None:
            params["attachmentid"] = attachmentid
        if displaytext is not None:
            params["displaytext"] = displaytext
        response = await self.post_body(
            f"/api/V1/uploadbusinessobjectattachment/filename/{filename}/busobname/{busobname}/busobrecid/{busobrecid}/offset/{offset}/totalsize/{totalsize}",
            params=params,
            content=body,
            content_type="application/octet-stream",
        )
        return self.parse_response(response, cherwell_pydantic_api.types.StringResponse)
