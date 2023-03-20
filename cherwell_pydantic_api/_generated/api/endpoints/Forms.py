from typing import Any, Dict, List, Literal, Optional, Union, AsyncIterable, Iterable
from pydantic import parse_obj_as
import cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Forms
import cherwell_pydantic_api.types
from cherwell_pydantic_api.generated_api_utils import GeneratedInterfaceBase


class FormsInterface(GeneratedInterfaceBase):
    async def GetMobileFormForBusObByIdAndPublicIdV1(
        self,
        busobid: cherwell_pydantic_api.types.BusObIDParamType,
        publicid: str,
        foredit: Optional[bool] = None,
        formid: Optional[str] = None,
    ) -> cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Forms.MobileFormResponse:
        """Get mobile form by BusObId and Public ID

        Operation that gets a mobile form for a specific Business Object by Business Object ID and Public ID.
         :param busobid: Specify the Business Object ID.
         :param publicid: Specify the Business Object Public ID.
         :param foredit: Flag to get the edit mode version of a form.
         :param formid: Specify the form ID if the default is not desired.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Forms.MobileFormResponse
        """
        self.validate_path_param(busobid)
        self.validate_path_param(publicid)
        params = {}
        if foredit is not None:
            params["foredit"] = foredit
        if formid is not None:
            params["formid"] = formid
        response = await self.get(
            f"/api/V1/getmobileformforbusob/busobid/{busobid}/publicid/{publicid}",
            params=params,
        )
        return parse_obj_as(
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Forms.MobileFormResponse,
            response,
        )

    async def GetMobileFormForBusObByIdAndRecIdV1(
        self,
        busobid: cherwell_pydantic_api.types.BusObIDParamType,
        busobrecid: cherwell_pydantic_api.types.BusObRecID,
        foredit: Optional[bool] = None,
        formid: Optional[str] = None,
    ) -> cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Forms.MobileFormResponse:
        """Get mobile form by Business Object ID and Business Object Record ID.

        Operation that gets a mobile form for a specific Business Object by Business Object ID and record ID.
         :param busobid: Specify the Business Object ID.
         :param busobrecid: Specify the Business Object Record ID.
         :param foredit: Flag to get the edit mode version of a form.
         :param formid: Specify the form ID if the default is not desired.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Forms.MobileFormResponse
        """
        self.validate_path_param(busobid)
        self.validate_path_param(busobrecid)
        params = {}
        if foredit is not None:
            params["foredit"] = foredit
        if formid is not None:
            params["formid"] = formid
        response = await self.get(
            f"/api/V1/getmobileformforbusob/busobid/{busobid}/busobrecid/{busobrecid}",
            params=params,
        )
        return parse_obj_as(
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Forms.MobileFormResponse,
            response,
        )

    async def GetMobileFormForBusObByNameAndPublicIdV1(
        self,
        busobname: str,
        publicid: str,
        foredit: Optional[bool] = None,
        formid: Optional[str] = None,
    ) -> cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Forms.MobileFormResponse:
        """Get mobile form by Business Object name and Public ID

        Operation that gets a mobile form for a specific Business Object by Business Object name and public ID.
         :param busobname: Specify the Business Object name.
         :param publicid: Specify the Business Object public ID.
         :param foredit: Flag to get the edit mode version of a form.
         :param formid: Specify the form ID if the default is not desired.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Forms.MobileFormResponse
        """
        self.validate_path_param(busobname)
        self.validate_path_param(publicid)
        params = {}
        if foredit is not None:
            params["foredit"] = foredit
        if formid is not None:
            params["formid"] = formid
        response = await self.get(
            f"/api/V1/getmobileformforbusob/busobname/{busobname}/publicid/{publicid}",
            params=params,
        )
        return parse_obj_as(
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Forms.MobileFormResponse,
            response,
        )

    async def GetMobileFormForBusObByNameAndRecIdV1(
        self,
        busobname: str,
        busobrecid: cherwell_pydantic_api.types.BusObRecID,
        foredit: Optional[bool] = None,
        formid: Optional[str] = None,
    ) -> cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Forms.MobileFormResponse:
        """Get mobile form by Business Object name and record ID.

        Operation that gets a mobile form for a specific Business Object by Business Object name and record ID.
         :param busobname: Specify the Business Object name.
         :param busobrecid: Specify the Business Object record ID.
         :param foredit: Flag to get the edit mode version of a form.
         :param formid: Specify the form ID if the default is not desired.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Forms.MobileFormResponse
        """
        self.validate_path_param(busobname)
        self.validate_path_param(busobrecid)
        params = {}
        if foredit is not None:
            params["foredit"] = foredit
        if formid is not None:
            params["formid"] = formid
        response = await self.get(
            f"/api/V1/getmobileformforbusob/busobname/{busobname}/busobrecid/{busobrecid}",
            params=params,
        )
        return parse_obj_as(
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Forms.MobileFormResponse,
            response,
        )
