from typing import Any, Literal, Optional  # type: ignore

import cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security
import cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users
import cherwell_pydantic_api.types
from cherwell_pydantic_api.generated_api_utils import GeneratedInterfaceBase


class SecurityInterface(GeneratedInterfaceBase):
    async def GetClientSecuritySettingsV1(
        self,
        applicationtype: Literal[
            "NotSet",
            "RichClient",
            "BrowserClient",
            "BrowserPortal",
            "MobileClient",
            "ServiceMonitor",
        ],
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.ClientSecuritySettingsResponse
    ):
        """Get client security settings

        Operation to get the configured client security settings. Returns true if internal, Windows, LDAP, or SAML are enabled as authentication methods.
         :param applicationtype: The type of CSM application to return security settings for.  Application type is Desktop Client, Browser Client, Browser Portal or Cherwell Mobile.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.ClientSecuritySettingsResponse
        """
        self.validate_path_param(
            applicationtype,
            Literal[
                "NotSet",
                "RichClient",
                "BrowserClient",
                "BrowserPortal",
                "MobileClient",
                "ServiceMonitor",
            ],
        )
        response = await self.get(
            f"/api/V1/getclientsecuritysettings/applicationtype/{applicationtype}"
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.ClientSecuritySettingsResponse,
        )

    async def GetRolesV1(
        self,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.RoleReadResponse
    ):
        """Get all available Roles

        Operation to get all available Roles.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.RoleReadResponse
        """
        response = await self.get("/api/V1/getroles")
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.RoleReadResponse,
        )

    async def GetRolesV2(
        self,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.RoleReadV2Response
    ):
        """Get all available Roles

        Operation to get all available Roles.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.RoleReadV2Response
        """
        response = await self.get("/api/V2/getroles")
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.RoleReadV2Response,
        )

    async def GetSecurityGroupBusinessObjectPermissionsByBusObIdV1(
        self,
        groupid: str,
        busObId: cherwell_pydantic_api.types.BusObIDParamType,
    ) -> list[
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.BusinessObjectPermission
    ]:
        """Get Business Object permissions by Security Group

        Operation to get specific Business Object permissions for a Security Group.
         :param groupid: Specify the Security Group ID.
         :param busObId: Specify the Business Object ID.
         :return: list[cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.BusinessObjectPermission]
        """
        self.validate_path_param(groupid, str)
        self.validate_path_param(busObId, cherwell_pydantic_api.types.BusObIDParamType)
        response = await self.get(
            f"/api/V1/getsecuritygroupbusinessobjectpermissions/groupid/{groupid}/busobid/{busObId}"
        )
        return self.parse_response(
            response,
            list[
                cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.BusinessObjectPermission
            ],
        )

    async def GetSecurityGroupBusinessObjectPermissionsByBusObIdV2(
        self,
        groupid: str,
        busObId: cherwell_pydantic_api.types.BusObIDParamType,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.GetSecurityGroupBusinessObjectPermissionsResponse
    ):
        """Get Business Object permissions by Security Group

        Operation to get specific Business Object permissions for a Security Group.
         :param groupid: Specify the Security Group ID.
         :param busObId: Specify the Business Object ID.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.GetSecurityGroupBusinessObjectPermissionsResponse
        """
        self.validate_path_param(groupid, str)
        self.validate_path_param(busObId, cherwell_pydantic_api.types.BusObIDParamType)
        response = await self.get(
            f"/api/V2/getsecuritygroupbusinessobjectpermissions/groupid/{groupid}/busobid/{busObId}"
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.GetSecurityGroupBusinessObjectPermissionsResponse,
        )

    async def GetSecurityGroupBusinessObjectPermissionsByBusObNameV1(
        self,
        groupname: str,
        busobname: str,
    ) -> list[
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.BusinessObjectPermission
    ]:
        """Get Business Object permissions by Security Group

        Operation to get specific Business Object permissions for a Security Group.
         :param groupname: Specify the Security Group name.
         :param busobname: Specify the Business Object name.
         :return: list[cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.BusinessObjectPermission]
        """
        self.validate_path_param(groupname, str)
        self.validate_path_param(busobname, str)
        response = await self.get(
            f"/api/V1/getsecuritygroupbusinessobjectpermissions/groupname/{groupname}/busobname/{busobname}"
        )
        return self.parse_response(
            response,
            list[
                cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.BusinessObjectPermission
            ],
        )

    async def GetSecurityGroupBusinessObjectPermissionsByBusObNameV2(
        self,
        groupname: str,
        busobname: str,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.GetSecurityGroupBusinessObjectPermissionsResponse
    ):
        """Get Business Object permissions by Security Group

        Operation to get specific Business Object permissions for a Security Group.
         :param groupname: Specify the Security Group name.
         :param busobname: Specify the Business Object name.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.GetSecurityGroupBusinessObjectPermissionsResponse
        """
        self.validate_path_param(groupname, str)
        self.validate_path_param(busobname, str)
        response = await self.get(
            f"/api/V2/getsecuritygroupbusinessobjectpermissions/groupname/{groupname}/busobname/{busobname}"
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.GetSecurityGroupBusinessObjectPermissionsResponse,
        )

    async def GetSecurityGroupBusinessObjectPermissionsForCurrentUserByBusObIdV1(
        self,
        busObId: cherwell_pydantic_api.types.BusObIDParamType,
    ) -> list[
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.BusinessObjectPermission
    ]:
        """Get Business Object permission for current user

        Operation to get Business Object permissions for the currently logged-in user's Security Group.
         :param busObId: Specify the Business Object ID.
         :return: list[cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.BusinessObjectPermission]
        """
        self.validate_path_param(busObId, cherwell_pydantic_api.types.BusObIDParamType)
        response = await self.get(
            f"/api/V1/getsecuritygroupbusinessobjectpermissionsforcurrentuserbybusobid/busobid/{busObId}"
        )
        return self.parse_response(
            response,
            list[
                cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.BusinessObjectPermission
            ],
        )

    async def GetSecurityGroupBusinessObjectPermissionsForCurrentUserByBusObIdV2(
        self,
        busObId: cherwell_pydantic_api.types.BusObIDParamType,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.GetSecurityGroupBusinessObjectPermissionsResponse
    ):
        """Get Business Object permission for current user

        Operation to get Business Object permissions for the currently logged-in user's Security Group.
         :param busObId: Specify the Business Object ID.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.GetSecurityGroupBusinessObjectPermissionsResponse
        """
        self.validate_path_param(busObId, cherwell_pydantic_api.types.BusObIDParamType)
        response = await self.get(
            f"/api/V2/getsecuritygroupbusinessobjectpermissionsforcurrentuserbybusobid/busobid/{busObId}"
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.GetSecurityGroupBusinessObjectPermissionsResponse,
        )

    async def GetSecurityGroupBusinessObjectPermissionsForCurrentUserByBusObNameV1(
        self,
        busobname: str,
    ) -> list[
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.BusinessObjectPermission
    ]:
        """Get Business Object permissions for current user

        Operation to get Business Object permissions for currently logged in user's Security Group.
         :param busobname: Specify the Business Object name.
         :return: list[cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.BusinessObjectPermission]
        """
        self.validate_path_param(busobname, str)
        response = await self.get(
            f"/api/V1/getsecuritygroupbusinessobjectpermissionsforcurrentuserbybusobname/busobname/{busobname}"
        )
        return self.parse_response(
            response,
            list[
                cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.BusinessObjectPermission
            ],
        )

    async def GetSecurityGroupBusinessObjectPermissionsForCurrentUserByBusObNameV2(
        self,
        busobname: str,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.GetSecurityGroupBusinessObjectPermissionsResponse
    ):
        """Get Business Object permissions for current user

        Operation to get Business Object permissions for currently logged in user's Security Group.
         :param busobname: Specify the Business Object name.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.GetSecurityGroupBusinessObjectPermissionsResponse
        """
        self.validate_path_param(busobname, str)
        response = await self.get(
            f"/api/V2/getsecuritygroupbusinessobjectpermissionsforcurrentuserbybusobname/busobname/{busobname}"
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.GetSecurityGroupBusinessObjectPermissionsResponse,
        )

    async def GetSecurityGroupCategoriesV1(
        self,
    ) -> list[
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.RightCategory
    ]:
        """Get all Security Group categories

        Operation to get IDs and names for all available Security Group categories.
         :return: list[cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.RightCategory]
        """
        response = await self.get("/api/V1/getsecuritygroupcategories")
        return self.parse_response(
            response,
            list[
                cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.RightCategory
            ],
        )

    async def GetSecurityGroupCategoriesV2(
        self,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.SecurityRightCategoriesResponse
    ):
        """Get all Security Group categories

        Operation to get IDs and names for all available Security Group categories.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.SecurityRightCategoriesResponse
        """
        response = await self.get("/api/V2/getsecuritygroupcategories")
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.SecurityRightCategoriesResponse,
        )

    async def GetSecurityGroupRightsByGroupIdAndCategoryIdV1(
        self,
        groupid: str,
        categoryid: str,
    ) -> list[
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.Right
    ]:
        """Get permissions for a Security Group by category

        Operation to get permissions for a Security Group by category. To get Security Group IDs, use "Get all available Security Groups." To get Security Group category IDs, use "Get all Security Group categories."
         :param groupid: Specify the Security Group ID
         :param categoryid: Specify the Security Group category ID
         :return: list[cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.Right]
        """
        self.validate_path_param(groupid, str)
        self.validate_path_param(categoryid, str)
        response = await self.get(
            f"/api/V1/getsecuritygrouprights/groupid/{groupid}/categoryid/{categoryid}"
        )
        return self.parse_response(
            response,
            list[
                cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.Right
            ],
        )

    async def GetSecurityGroupRightsByGroupIdAndCategoryIdV2(
        self,
        groupid: str,
        categoryid: str,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.SecurityRightsResponse
    ):
        """Get permissions for a Security Group by category

        Operation to get permissions for a Security Group by category. To get Security Group IDs, use "Get all available Security Groups." To get Security Group category IDs, use "Get all Security Group categories."
         :param groupid: Specify the Security Group ID
         :param categoryid: Specify the Security Group category ID
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.SecurityRightsResponse
        """
        self.validate_path_param(groupid, str)
        self.validate_path_param(categoryid, str)
        response = await self.get(
            f"/api/V2/getsecuritygrouprights/groupid/{groupid}/categoryid/{categoryid}"
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.SecurityRightsResponse,
        )

    async def GetSecurityGroupRightsByGroupNameAndCategoryNameV1(
        self,
        groupname: str,
        categoryname: str,
    ) -> list[
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.Right
    ]:
        """Get permissions for a Security Group by category

        Operation to get permissions for a Security Group by category.
         :param groupname: Specify the Security Group name.
         :param categoryname: Specify the Security Group category name.
         :return: list[cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.Right]
        """
        self.validate_path_param(groupname, str)
        self.validate_path_param(categoryname, str)
        response = await self.get(
            f"/api/V1/getsecuritygrouprights/groupname/{groupname}/categoryname/{categoryname}"
        )
        return self.parse_response(
            response,
            list[
                cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.Right
            ],
        )

    async def GetSecurityGroupRightsByGroupNameAndCategoryNameV2(
        self,
        groupname: str,
        categoryname: str,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.SecurityRightsResponse
    ):
        """Get permissions for a Security Group by category

        Operation to get permissions for a Security Group by category.
         :param groupname: Specify the Security Group name.
         :param categoryname: Specify the Security Group category name.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.SecurityRightsResponse
        """
        self.validate_path_param(groupname, str)
        self.validate_path_param(categoryname, str)
        response = await self.get(
            f"/api/V2/getsecuritygrouprights/groupname/{groupname}/categoryname/{categoryname}"
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.SecurityRightsResponse,
        )

    async def GetSecurityGroupRightsForCurrentUserByCategoryIdV1(
        self,
        categoryid: str,
    ) -> list[
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.Right
    ]:
        """Get current user's permissions by Security Group category by ID

        Operation to get permissions for the current user's Security Group by category. To get Security Group category IDs, use "Get all Security Group categories."
         :param categoryid: Specify the Security Group category ID.
         :return: list[cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.Right]
        """
        self.validate_path_param(categoryid, str)
        response = await self.get(
            f"/api/V1/getsecuritygrouprightsforcurrentuserbycategoryid/categoryid/{categoryid}"
        )
        return self.parse_response(
            response,
            list[
                cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.Right
            ],
        )

    async def GetSecurityGroupRightsForCurrentUserByCategoryIdV2(
        self,
        categoryid: str,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.SecurityRightsResponse
    ):
        """Get current user's permissions by Security Group category by ID

        Operation to get permissions for the current user's Security Group by category. To get Security Group category IDs, use "Get all Security Group categories."
         :param categoryid: Specify the Security Group category ID.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.SecurityRightsResponse
        """
        self.validate_path_param(categoryid, str)
        response = await self.get(
            f"/api/V2/getsecuritygrouprightsforcurrentuserbycategoryid/categoryid/{categoryid}"
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.SecurityRightsResponse,
        )

    async def GetSecurityGroupRightsForCurrentUserByCategoryNameV1(
        self,
        categoryname: str,
    ) -> list[
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.Right
    ]:
        """Get current user's permissions by Security Group category by name

        Operation to get permissions for the current user's Security Group by category.
         :param categoryname: Specify the Security Group category name.
         :return: list[cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.Right]
        """
        self.validate_path_param(categoryname, str)
        response = await self.get(
            f"/api/V1/getsecuritygrouprightsforcurrentuserbycategoryname/categoryname/{categoryname}"
        )
        return self.parse_response(
            response,
            list[
                cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.Right
            ],
        )

    async def GetSecurityGroupRightsForCurrentUserByCategoryNameV2(
        self,
        categoryname: str,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.SecurityRightsResponse
    ):
        """Get current user's permissions by Security Group category by name

        Operation to get permissions for the current user's Security Group by category.
         :param categoryname: Specify the Security Group category name.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.SecurityRightsResponse
        """
        self.validate_path_param(categoryname, str)
        response = await self.get(
            f"/api/V2/getsecuritygrouprightsforcurrentuserbycategoryname/categoryname/{categoryname}"
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.SecurityRightsResponse,
        )

    async def GetSecurityGroupsV1(
        self,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.SecurityGroupResponse
    ):
        """Get all available Security Groups

        Operation to get IDs, names, and descriptions for all available Security Groups.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.SecurityGroupResponse
        """
        response = await self.get("/api/V1/getsecuritygroups")
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.SecurityGroupResponse,
        )

    async def GetSecurityGroupsV2(
        self,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.SecurityGroupV2Response
    ):
        """Get all available Security Groups

        Operation to get IDs, names, and descriptions for all available Security Groups.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.SecurityGroupV2Response
        """
        response = await self.get("/api/V2/getsecuritygroups")
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Security.SecurityGroupV2Response,
        )

    async def GetUsersInSecurityGroupV1(
        self,
        groupid: str,
    ) -> list[
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.User
    ]:
        """Get users in a Security Group

        Operation to get the users in a specified Security Group. Use "Get all available Security Groups" to get Security Group record IDs.
         :param groupid: Specify the Security Group ID.
         :return: list[cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.User]
        """
        self.validate_path_param(groupid, str)
        response = await self.get(f"/api/V1/getusersinsecuritygroup/groupid/{groupid}")
        return self.parse_response(
            response,
            list[
                cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.User
            ],
        )

    async def GetUsersInSecurityGroupV2(
        self,
        groupid: str,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserReadV2Response
    ):
        """Get users in a Security Group

        Operation to get the users in a specified Security Group. Use "Get all available Security Groups" to get Security Group record IDs.
         :param groupid: Specify the Security Group ID.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserReadV2Response
        """
        self.validate_path_param(groupid, str)
        response = await self.get(f"/api/V2/getusersinsecuritygroup/groupid/{groupid}")
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Users.UserReadV2Response,
        )
