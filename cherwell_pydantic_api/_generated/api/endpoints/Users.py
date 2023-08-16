from typing import Any, Literal, Optional  # type: ignore

import cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users
from cherwell_pydantic_api.generated_api_utils import GeneratedInterfaceBase


class UsersInterface(GeneratedInterfaceBase):
    async def DeleteUserBatchV1(
        self,
        request: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserBatchDeleteRequest,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserBatchDeleteResponse
    ):
        """Delete a batch of users

        Operation to delete a batch of users. To get record IDs, use "Get a user by login ID" or "Get a user by public id."
         :param request: Request object listing record IDs for users to be deleted and an error flag.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserBatchDeleteResponse
        """
        response = await self.post_body(
            "/api/V1/deleteuserbatch",
            content=request.model_dump_json(exclude_unset=True, by_alias=True),
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserBatchDeleteResponse,
        )

    async def DeleteUserBatchV2(
        self,
        request: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserBatchDeleteRequest,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserBatchDeleteV2Response
    ):
        """Delete a batch of users

        Operation to delete a batch of users. To get record IDs, use "Get a user by login ID" or "Get a user by public id."
         :param request: Request object listing record IDs for users to be deleted and an error flag.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserBatchDeleteV2Response
        """
        response = await self.post_body(
            "/api/V2/deleteuserbatch",
            content=request.model_dump_json(exclude_unset=True, by_alias=True),
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserBatchDeleteV2Response,
        )

    async def DeleteUserV1(
        self,
        userrecordid: str,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserDeleteResponse
    ):
        """Delete a user by record ID

        Operation to delete a user by record ID. To get record IDs, use "Get a user by login ID" or "Get a user by public id."
         :param userrecordid: Specify the record ID of the user you want to delete
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserDeleteResponse
        """
        self.validate_path_param(userrecordid, str)
        response = await self.delete(f"/api/V1/deleteuser/userrecordid/{userrecordid}")
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserDeleteResponse,
        )

    async def DeleteUserV2(
        self,
        userrecordid: str,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserDeleteV2Response
    ):
        """Delete a user by record ID

        Operation to delete a user by record ID. To get record IDs, use "Get a user by login ID" or "Get a user by public id."
         :param userrecordid: Specify the record ID of the user you want to delete
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserDeleteV2Response
        """
        self.validate_path_param(userrecordid, str)
        response = await self.delete(f"/api/V2/deleteuser/userrecordid/{userrecordid}")
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserDeleteV2Response,
        )

    async def GetListOfUsers(
        self,
        loginidfilter: Literal["Internal", "Windows", "Both"],
        stoponerror: Optional[bool] = None,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserListResponse
    ):
        """Get a list of all system users.

        Operation to get a list of all system users.
         :param loginidfilter: Specify the login ID filter to apply to the users list.
         :param stoponerror: Specify whether the operation is interrupted if retrieving any user causes an error.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserListResponse
        """
        params: dict[str, Any] = {"loginidfilter": loginidfilter}
        if stoponerror is not None:
            params["stoponerror"] = stoponerror
        response = await self.get("/api/V1/getlistofusers", params=params)
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserListResponse,
        )

    async def GetUserBatchV1(
        self,
        request: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserBatchReadRequest,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserBatchReadResponse
    ):
        """Get user information in a batch

        Operation to get user information in a batch. To get record IDs, use "Get a user by login ID" or "Get a user by public id."
         :param request: Request object that lists user record IDs or public IDs of users and an error flag.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserBatchReadResponse
        """
        response = await self.post_body(
            "/api/V1/getuserbatch",
            content=request.model_dump_json(exclude_unset=True, by_alias=True),
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserBatchReadResponse,
        )

    async def GetUserByLoginIdV1(
        self,
        loginid: str,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.User
    ):
        """Get a user by login ID

        Operation to get detailed user information by login ID. Use to get user record IDs and account settings, for example. This operation has been deprecated by a V2 operation of the same name, but with query string parameters.
         :param loginid: Specify the user's login ID.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.User
        """
        self.validate_path_param(loginid, str)
        response = await self.get(f"/api/V1/getuserbyloginid/loginid/{loginid}")
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.User,
        )

    async def GetUserByLoginIdV2(
        self,
        loginid: str,
        loginidtype: Literal["Internal", "Windows"],
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.User
    ):
        """Get a user by login ID and login ID type

        Operation to get detailed user information by login ID. Use to get user record IDs and account settings, for example.
         :param loginid: Specify the user's login ID.
         :param loginidtype: Specify the login ID type.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.User
        """
        params: dict[str, Any] = {"loginid": loginid, "loginidtype": loginidtype}
        response = await self.get("/api/V2/getuserbyloginid", params=params)
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.User,
        )

    async def GetUserByLoginIdV3(
        self,
        loginid: str,
        loginidtype: Literal["Internal", "Windows"],
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserV2
    ):
        """Get a user by login ID and login ID type

        Operation to get detailed user information by login ID. Use to get user record IDs and account settings, for example.
         :param loginid: Specify the user's login ID.
         :param loginidtype: Specify the login ID type.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserV2
        """
        params: dict[str, Any] = {"loginid": loginid, "loginidtype": loginidtype}
        response = await self.get("/api/V3/getuserbyloginid", params=params)
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserV2,
        )

    async def GetUserByPublicIdV1(
        self,
        publicid: str,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserReadResponse
    ):
        """Get a user by public ID

        Operation to get detailed user information by public ID. Use to get user record IDs and account settings, for example.
         :param publicid: Specify the user's public ID.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserReadResponse
        """
        self.validate_path_param(publicid, str)
        response = await self.get(f"/api/V1/getuserbypublicid/publicid/{publicid}")
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserReadResponse,
        )

    async def GetUserByPublicIdV2(
        self,
        publicid: str,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserReadV2Response
    ):
        """Get a user by public ID

        Operation to get detailed user information by public ID. Use to get user record IDs and account settings, for example.
         :param publicid: Specify the user's public ID.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserReadV2Response
        """
        self.validate_path_param(publicid, str)
        response = await self.get(f"/api/V2/getuserbypublicid/publicid/{publicid}")
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserReadV2Response,
        )

    async def GetUserByRecId(
        self,
        recid: str,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserV2
    ):
        """Get a user by record ID

        Operation to get detailed user information by record ID.  Use to get user public IDs and account settings, for example.
         :param recid: Specify the user's record ID
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserV2
        """
        self.validate_path_param(recid, str)
        response = await self.get(f"/api/V1/getuserbyrecid/recid/{recid}")
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserV2,
        )

    async def SaveUserBatchV1(
        self,
        request: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserBatchSaveRequest,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserBatchSaveResponse
    ):
        """Create or update users in a batch

        Operation to create or update users in a batch. To update, specify record ID. To create, leave record ID empty.
         :param request: Request object listing user record IDs and an error flag.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserBatchSaveResponse
        """
        response = await self.post_body(
            "/api/V1/saveuserbatch",
            content=request.model_dump_json(exclude_unset=True, by_alias=True),
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserBatchSaveResponse,
        )

    async def SaveUserBatchV2(
        self,
        request: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserBatchSaveV2Request,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserBatchSaveV2Response
    ):
        """Create or update users in a batch

        Operation to create or update users in a batch. To update, specify record ID. To create, leave record ID empty.
         :param request: Request object listing user record IDs and an error flag.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserBatchSaveV2Response
        """
        response = await self.post_body(
            "/api/V2/saveuserbatch",
            content=request.model_dump_json(exclude_unset=True, by_alias=True),
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserBatchSaveV2Response,
        )

    async def SaveUserV1(
        self,
        request: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserSaveRequest,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserSaveResponse
    ):
        """Create or update a user

        Operation to create or update a user.  The response is a collection because if you use a public ID, more than one user could be updated since public IDs may not be unique.
         :param request: Request object to specify user parameters and fields with values to be created or updated. The loginId and either the Business Object record ID or Public ID are required.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserSaveResponse
        """
        response = await self.post_body(
            "/api/V1/saveuser",
            content=request.model_dump_json(exclude_unset=True, by_alias=True),
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserSaveResponse,
        )

    async def SaveUserV2(
        self,
        request: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserSaveV2Request,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserSaveV2Response
    ):
        """Create or update a user

        Operation to create or update a user.  The response is a collection because if you use a public ID, more than one user could be updated since public IDs may not be unique.
         :param request: Request object to specify user parameters and fields with values to be created or updated. The loginId and either the Business Object record ID or Public ID are required.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserSaveV2Response
        """
        response = await self.post_body(
            "/api/V2/saveuser",
            content=request.model_dump_json(exclude_unset=True, by_alias=True),
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserSaveV2Response,
        )
