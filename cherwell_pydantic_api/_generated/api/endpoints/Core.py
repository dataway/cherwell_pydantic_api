from typing import Any, Literal, Optional  # type: ignore

import cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core
import cherwell_pydantic_api.types
from cherwell_pydantic_api.generated_api_utils import GeneratedInterfaceBase


class CoreInterface(GeneratedInterfaceBase):
    async def DeleteGalleryImageByStandInKeyV1(
        self,
        standinkey: str,
    ) -> None:
        """Delete a gallery image

        Endpoint to delete a gallery image.
         :param standinkey: The StandIn key for the gallery image to delete.
         :return: None"""
        self.validate_path_param(standinkey, str)
        response = await self.delete(
            f"/api/V1/deletegalleryimage/standinkey/{standinkey}"
        )
        self.check_response(response)

    async def GetGalleryImagesFolderV1(
        self,
        scope: str,
        scopeowner: str,
        folder: str,
        links: Optional[bool] = None,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
    ):
        """Get gallery images by scope, scopeowner, and folder

        Get gallery images for the specified scope, scopeowner, and folder.
         :param scope: The scope to get gallery images for.
         :param scopeowner: the scopeowner to get gallery images for.
         :param folder: The folder to get gallery images for.
         :param links: Flag to include hyperlinks in results. Default is false.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
        """
        self.validate_path_param(scope, str)
        self.validate_path_param(scopeowner, str)
        self.validate_path_param(folder, str)
        params: dict[str, Any] = {}
        if links is not None:
            params["links"] = links
        response = await self.get(
            f"/api/V1/getgalleryimages/scope/{scope}/scopeowner/{scopeowner}/folder/{folder}",
            params=params,
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData,
        )

    async def GetGalleryImagesScopeOwnerV1(
        self,
        scope: str,
        scopeowner: str,
        links: Optional[bool] = None,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
    ):
        """Get gallery images by scope and scopeowner

        Get all gallery images for the specified scope and scope owner.
         :param scope: The scope to get gallery images for.
         :param scopeowner: The scopeowner to get gallery images for.
         :param links: Flag to include hyperlinks in results. Default is false.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
        """
        self.validate_path_param(scope, str)
        self.validate_path_param(scopeowner, str)
        params: dict[str, Any] = {}
        if links is not None:
            params["links"] = links
        response = await self.get(
            f"/api/V1/getgalleryimages/scope/{scope}/scopeowner/{scopeowner}",
            params=params,
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData,
        )

    async def GetGalleryImagesScopeV1(
        self,
        scope: str,
        links: Optional[bool] = None,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
    ):
        """Get gallery images by scope

        Get all gallery images for the specified scope.
         :param scope: The scope to get the images for.
         :param links: Flag to include hyperlinks in results. Default is false.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
        """
        self.validate_path_param(scope, str)
        params: dict[str, Any] = {}
        if links is not None:
            params["links"] = links
        response = await self.get(
            f"/api/V1/getgalleryimages/scope/{scope}", params=params
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData,
        )

    async def GetGalleryImagesV1(
        self,
        links: Optional[bool] = None,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
    ):
        """Get all gallery images

        Get all the gallery images in the system.
         :param links: Flag to include hyperlinks in results. Default is false.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
        """
        params: dict[str, Any] = {}
        if links is not None:
            params["links"] = links
        response = await self.get("/api/V1/getgalleryimages", params=params)
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData,
        )

    async def GetGalleryImageV1(
        self,
        name: str,
        width: Optional[int] = None,
        height: Optional[int] = None,
    ) -> cherwell_pydantic_api.types.StringResponse:
        """Get built-in images

        Operation that gets built-in images. If you are requesting an icon (.ico), you can specify width and height.
         :param name: Image name and folder location in the Image Manager. Parameter must begin with "[PlugIn]Images;" and then a period-separated list of folders. Example: "[PlugIn]Images;Images.Common.Cherwell.ico".
         :param width: Specify the width (icons only).
         :param height: Specify the height (icons only).
         :return: cherwell_pydantic_api.types.StringResponse"""
        self.validate_path_param(name, str)
        params: dict[str, Any] = {}
        if width is not None:
            params["width"] = width
        if height is not None:
            params["height"] = height
        response = await self.get(f"/api/V1/getgalleryimage/name/{name}", params=params)
        return self.parse_response(response, cherwell_pydantic_api.types.StringResponse)

    async def GetStoredValuesFolderV1(
        self,
        scope: str,
        scopeowner: str,
        folder: str,
        links: Optional[bool] = None,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
    ):
        """Get stored values by folder

        Get stored values for the specified folder.
         :param scope: The scope for which to get stored values.
         :param scopeowner: The scope owner for which to get stored values.
         :param folder: The folder for which to get stored values.
         :param links: Flag to include hyperlinks in results. Default is false.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
        """
        self.validate_path_param(scope, str)
        self.validate_path_param(scopeowner, str)
        self.validate_path_param(folder, str)
        params: dict[str, Any] = {}
        if links is not None:
            params["links"] = links
        response = await self.get(
            f"/api/V1/storedvalues/scope/{scope}/scopeowner/{scopeowner}/folder/{folder}",
            params=params,
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData,
        )

    async def GetStoredValuesScopeOwnerV1(
        self,
        scope: str,
        scopeowner: str,
        links: Optional[bool] = None,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
    ):
        """Get stored values by scope owner

        Get stored values for the specified scope and scope owner.
         :param scope: The scope for which to get stored values.
         :param scopeowner: The scope owner for which to get stored values.
         :param links: Flag to include hyperlinks in results. Default is false.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
        """
        self.validate_path_param(scope, str)
        self.validate_path_param(scopeowner, str)
        params: dict[str, Any] = {}
        if links is not None:
            params["links"] = links
        response = await self.get(
            f"/api/V1/storedvalues/scope/{scope}/scopeowner/{scopeowner}", params=params
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData,
        )

    async def GetStoredValuesScopeV1(
        self,
        scope: str,
        links: Optional[bool] = None,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
    ):
        """Get stored values by scope

        Get all the stored values for the specified scope.
         :param scope: The scope for which to get stored values.
         :param links: Flag to include hyperlinks in results. Default is false.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
        """
        self.validate_path_param(scope, str)
        params: dict[str, Any] = {}
        if links is not None:
            params["links"] = links
        response = await self.get(f"/api/V1/storedvalues/scope/{scope}", params=params)
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData,
        )

    async def GetStoredValuesV1(
        self,
        links: Optional[bool] = None,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
    ):
        """Gets all the stored values in the system

        Get all the stored values in the system.
         :param links: Flag to include hyperlinks in results. Default is false.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
        """
        params: dict[str, Any] = {}
        if links is not None:
            params["links"] = links
        response = await self.get("/api/V1/storedvalues", params=params)
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData,
        )

    async def GetStoredValueV1(
        self,
        standInKey: str,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.StoredValueResponse
    ):
        """Get a  stored value

        Get a stored value by its StandIn key.
         :param standInKey: The StandIn key for the Stored Value you would like to retrieve.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.StoredValueResponse
        """
        self.validate_path_param(standInKey, str)
        response = await self.get(f"/api/V1/getstoredvalue/standinkey/{standInKey}")
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.StoredValueResponse,
        )

    async def GetViewsV1(
        self,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ViewsResponse
    ):
        """Get a list of the views

        Operation to get a list of views that are configured in the system.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ViewsResponse
        """
        response = await self.get("/api/V1/getviews")
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ViewsResponse,
        )

    async def SaveGalleryImageV1(
        self,
        request: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.SaveGalleryImageRequest,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.SaveGalleryImageResponse
    ):
        """Create or update a gallery image

        Endpoint to Create or update a gallery image. To create a new gallery image leave the StandIn key blank. To update a gallery image provide the StandIn key of the gallery image you want to update.
        There are three different ImageTypes allowed: Imported, Url, and File. To use the Imported image type, provide the filename in the Name property, with extension, and provide the image data in a Base64 encoded format in the Base64EncodedImageData property. The max file size is 512k.
        To use the Url image type,  provide the full network share path to the file in the Name property, ie: "&#92;&#92;&#92;&#92;&#92;&#92;&#92;&#92;networkshare&#92;&#92;&#92;somefolder&#92;&#92;&#92;somefile.jpg". If the file is not accessible to all users it will not visible to all users.
        To use the File image type, provide the full path to the file in the Name property, ie: "C:&#92;&#92;&#92;somefolder&#92;&#92;&#92;somfile.jpg". If the file is not accessible to all users it will not visible to all users.
        When creating or updating an image, Name and ImageType are always required, and if the image type is "Imported", then the Base64EncodedImageData is also required.
        scope, scopeowner, and folder can all be updated independently.
         :param request: To create a new gallery image leave the StandIn key blank. To update a gallery image provide the StandIn key of the gallery image you want to update.
        There are three different ImageTypes allowed: Imported, Url, and File. To use the Imported image type, provide the filename in the Name property, with extension, and provide the image data in a Base64 encoded format in the Base64EncodedImageData property. The max file size is 512k.
        To use the Url image type,  provide the full network share path to the file in the Name property, ie: "&#92;&#92;&#92;&#92;&#92;&#92;&#92;&#92;networkshare&#92;&#92;&#92;somefolder&#92;&#92;&#92;somefile.jpg". If the file is not accessible to all users it will not visible to all users.
        To use the File image type, provide the full path to the file in the Name property, ie: "C:&#92;&#92;&#92;somefolder&#92;&#92;&#92;somfile.jpg". If the file is not accessible to all users it will not visible to all users.
        When creating or updating an image, Name and ImageType are always required, and if the image type is "Imported", then the Base64EncodedImageData is also required.
        scope, scopeowner, and folder can all be updated independently.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.SaveGalleryImageResponse
        """
        response = await self.post_body(
            "/api/V1/savegalleryimage",
            content=request.model_dump_json(exclude_unset=True, by_alias=True),
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.SaveGalleryImageResponse,
        )

    async def SaveStoredValueV1(
        self,
        request: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.SaveStoredValueRequest,
    ) -> (
        cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.StoredValueResponse
    ):
        """Create or update a stored value

        Operation to create or update a stored value. To update, specify the StandIn key for the stored value to update. To create leave StandIn key blank, and provide a name, a scope, a type, and a value.
         :param request: The stored value to create or update. To update include the StandIn key for the associated stored value. To create, name, scope, type, and value are required.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.StoredValueResponse
        """
        response = await self.post_body(
            "/api/V1/savestoredvalue",
            content=request.model_dump_json(exclude_unset=True, by_alias=True),
        )
        return self.parse_response(
            response,
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.StoredValueResponse,
        )

    async def SetCultureV1(
        self,
        culturecode: str,
    ) -> cherwell_pydantic_api.types.StringResponse:
        """Set the culture for the current user

        Operation to update the current users culture by culture code. This returns a new access token that has the updated information in it.
         :param culturecode: The culture code to set for the current user.
         :return: cherwell_pydantic_api.types.StringResponse"""
        self.validate_path_param(culturecode, str)
        response = await self.put(f"/api/V1/setculture/culturecode/{culturecode}")
        return self.parse_response(response, cherwell_pydantic_api.types.StringResponse)
