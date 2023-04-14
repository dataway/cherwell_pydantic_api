from typing import Any, Literal, Optional  # type: ignore

import pydantic

import cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core
import cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security
from cherwell_pydantic_api.generated_api_utils import GeneratedInterfaceBase


class ServiceInterface(GeneratedInterfaceBase):
    async def GetServiceInfoV1(
        self,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ServiceInfoResponse
    ):
        """Get information about the REST Api and CSM

        Operation to get information about the REST API and CSM.  The response is latest REST API operation version, CSM version, and CSM system date and time.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ServiceInfoResponse
        """
        response = await self.get("/api/V1/serviceinfo")
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ServiceInfoResponse,
        )

    async def LogoutUserV1(self) -> None:
        """Log out user by token

        Operation that logs out the user referenced in the authentication token.
         :return: None"""
        response = await self.delete("/api/V1/logout")
        self.check_response(response)

    async def Token(
        self,
        grant_type: str,
        client_id: pydantic.SecretStr,
        client_secret: Optional[pydantic.SecretStr] = None,
        username: Optional[str] = None,
        password: Optional[pydantic.SecretStr] = None,
        refresh_token: Optional[str] = None,
        auth_mode: Optional[
            Literal["Internal", "Windows", "LDAP", "SAML", "Auto"]
        ] = None,
        site_name: Optional[str] = None,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.TokenResponse
    ):
        """Get an access token

        Operation to request an access token for one of the following authentication modes. Or, you can request an access token using a refresh token. An API client key is required in both cases, and the authentication mode you use must be the mode used by the CSM Browser Client.

        Internal - Use a CSM username and password. If no other mode is specified, Internal mode is used.

        Windows - Uses the server variable LOGON_USER to attempt to find a CSM user.  You can also use domain&#92;username and password.

        LDAP - Uses the LDAP settings configured for CSM and the server variable LOGON_USER to attempt to find a CSM user. You can also use domain&#92;username and password.

        SAML - Uses the SAML settings configured for CSM to validate credentials and find the CSM user.

        Auto - Uses the enabled authentication types configured for CSM.
         :param grant_type: The type of grant being requested: password or refresh_token.
         :param client_id: The API client key for the client making the token request.
         :param client_secret: The API client secret for the native client making the token request.  This is only required for native clients.
         :param username: Specify the login ID for the CSM user who will be granted the access token.
         :param password: Specify the password assigned to the login ID.
         :param refresh_token: Specify the refresh token used to grant another access token.
         :param auth_mode: Specify the Authentication Mode to use for requesting an access token.
         :param site_name: If for portal specify the Site name to use for requesting an access token.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.TokenResponse
        """
        post = {"grant_type": grant_type, "client_id": client_id.get_secret_value()}
        params: dict[str, Any] = {}
        if client_secret is not None:
            post["client_secret"] = client_secret.get_secret_value()
        if username is not None:
            post["username"] = username
        if password is not None:
            post["password"] = password.get_secret_value()
        if refresh_token is not None:
            post["refresh_token"] = refresh_token
        if auth_mode is not None:
            params["auth_mode"] = auth_mode
        if site_name is not None:
            params["site_name"] = site_name
        response = await self.post_form("/token", params=params, data=post)
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.TokenResponse,
        )
