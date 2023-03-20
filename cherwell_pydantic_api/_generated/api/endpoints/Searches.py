from typing import Any, Dict, List, Literal, Optional, Union, AsyncIterable, Iterable
from pydantic import parse_obj_as
import cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core
import cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches
from cherwell_pydantic_api.generated_api_utils import GeneratedInterfaceBase


class SearchesInterface(GeneratedInterfaceBase):
    async def GetQuickSearchConfigurationForBusObsV1(
        self,
        dataRequest: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.QuickSearchConfigurationRequest,
    ) -> cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.QuickSearchConfigurationResponse:
        """Get a Quick Search from a list of Business Object IDs

        Operation to build a Quick Search configuration that you can use to execute a Quick Search for multiple Business Objects. The configuration  includes supplied Business Object IDs and specific search items with the following options. Use the Option Key to determine if you can change the options.


        ChangedOption

        NonFinalStateOption

        SearchAnyWordsOption

        SearchAttachmentsOption

        SearchRelatedOption

        SortByOption


        Option Key:

        0 = None (Not selected and cannot select.)

        1 = Use (Selected and cannot clear.)

        2 = Display (Not selected and can select.)

        3 = UseAndDisplay (Selected and can clear.)


        SearchTargetType:

        0 = BusOb (Business Object)

        1 = DocRepository (Document Repository)
         :param dataRequest: Request containing the Business Object IDs list.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.QuickSearchConfigurationResponse
        """
        response = await self.post_body(
            "/api/V1/getquicksearchconfigurationforbusobs",
            content=dataRequest.json(exclude_unset=True, by_alias=True),
        )
        return parse_obj_as(
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.QuickSearchConfigurationResponse,
            response,
        )

    async def GetQuickSearchConfigurationForBusObsWithViewRightsV1(
        self,
    ) -> cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.QuickSearchConfigurationResponse:
        """Get a Quick Search by Business Objects with view rights

        Operation to get a Quick Search configuration that you can use to execute a Quick Search based the current user's Business Object view rights. The configuration  includes supplied Business Object IDs and specific search items with the following options. Use the Option Key to determine if you can change the options.

        ChangedOption

        NonFinalStateOption

        SearchAnyWordsOption

        SearchAttachmentsOption

        SearchRelatedOption

        SortByOption


        Option Key:

        0 = None (Not selected and cannot select.)

        1 = Use (Selected and cannot clear.)

        2 = Display (Not selected and can select.)

        3 = UseAndDisplay (Selected and can clear.)


        SearchTargetType:

        0 = BusOb (Business Object)

        1 = DocRepository (Document Repository)
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.QuickSearchConfigurationResponse
        """
        response = await self.get(
            "/api/V1/getquicksearchconfigurationforbusobswithviewrights"
        )
        return parse_obj_as(
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.QuickSearchConfigurationResponse,
            response,
        )

    async def GetQuickSearchResultsV1(
        self,
        dataRequest: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.QuickSearchRequest,
        includeLinks: Optional[bool] = None,
    ) -> cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.SimpleResultsList:
        """Execute a Quick Search from a list of Business Object IDs and search text

        Operation to execute a Quick Search using a list of Business Object IDs and search text.
         :param dataRequest: Request object listing Business Object IDs and search text. Leave out the entire Business Object IDs parameter and all configured quick search Business Objects will be searched.
         :param includeLinks: Flag to include hyperlinks in results. Default is false.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.SimpleResultsList
        """
        params = {}
        if includeLinks is not None:
            params["includeLinks"] = includeLinks
        response = await self.post_body(
            "/api/V1/getquicksearchresults",
            params=params,
            content=dataRequest.json(exclude_unset=True, by_alias=True),
        )
        return parse_obj_as(
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.SimpleResultsList,
            response,
        )

    async def GetQuickSearchSpecificResultsV1(
        self,
        dataRequest: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.QuickSearchSpecificRequest,
        includeSchema: Optional[bool] = None,
        includeLocationFields: Optional[bool] = None,
        includeLinks: Optional[bool] = None,
    ) -> cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.SearchResultsTableResponse:
        """Execute a Quick Search on a specific Business Object

        Operation to execute a Quick Search for a specific Business Object ID. Use "Get a Quick Search from a list of Business Object IDs" to find values for specific search item options, such as NonFinalStateOption.
         :param dataRequest: Request object containing the parameters for specific Business Object Quick Search execution.
         :param includeSchema: Flag to include the schema for the results.
         :param includeLocationFields: Flag to include location fields in the results.
         :param includeLinks: Flag to include hyperlinks in results. Default is false.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.SearchResultsTableResponse
        """
        params = {}
        if includeSchema is not None:
            params["includeSchema"] = includeSchema
        if includeLocationFields is not None:
            params["includeLocationFields"] = includeLocationFields
        if includeLinks is not None:
            params["includeLinks"] = includeLinks
        response = await self.post_body(
            "/api/V1/getquicksearchspecificresults",
            params=params,
            content=dataRequest.json(exclude_unset=True, by_alias=True),
        )
        return parse_obj_as(
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.SearchResultsTableResponse,
            response,
        )

    async def GetQuickSearchSpecificResultsV2(
        self,
        dataRequest: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.QuickSearchSpecificRequest,
        includeSchema: Optional[bool] = None,
        includeLocationFields: Optional[bool] = None,
        includeLinks: Optional[bool] = None,
    ) -> cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.QuickSearchResponse:
        """Execute a Quick Search on a specific Business Object

        Operation to execute a Quick Search for a specific Business Object ID. Use "Get a Quick Search from a list of Business Object IDs" to find values for specific search item options, such as NonFinalStateOption.
         :param dataRequest: Request object containing the parameters for specific Business Object Quick Search execution.
         :param includeSchema: Flag to include the schema for the results.
         :param includeLocationFields: Flag to include location fields in the results.
         :param includeLinks: Flag to include hyperlinks in results. Default is false.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.QuickSearchResponse
        """
        params = {}
        if includeSchema is not None:
            params["includeSchema"] = includeSchema
        if includeLocationFields is not None:
            params["includeLocationFields"] = includeLocationFields
        if includeLinks is not None:
            params["includeLinks"] = includeLinks
        response = await self.post_body(
            "/api/V2/getquicksearchspecificresults",
            params=params,
            content=dataRequest.json(exclude_unset=True, by_alias=True),
        )
        return parse_obj_as(
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.QuickSearchResponse,
            response,
        )

    async def GetSearchItemsByAssociation_Scope_ScopeOwner_FolderV1(
        self,
        association: str,
        scope: str,
        scopeowner: str,
        folder: str,
        links: Optional[bool] = None,
    ) -> cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.SearchItemResponse:
        """Get all saved searches by Folder ID

        Operation that returns a tree of saved queries, including scope, search name, IDs, and location within the tree.
         :param association: Use to filter results by Business Object association ID.
         :param scope: Use to filter results by scope name or ID.
         :param scopeowner: Use to filter results by scope owner ID.
         :param folder: Use to filter results by Search Group folder ID.
         :param links: Flag to include hyperlinks in results. Default is false.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.SearchItemResponse
        """
        self.validate_path_param(association)
        self.validate_path_param(scope)
        self.validate_path_param(scopeowner)
        self.validate_path_param(folder)
        params = {}
        if links is not None:
            params["links"] = links
        response = await self.get(
            f"/api/V1/getsearchitems/association/{association}/scope/{scope}/scopeowner/{scopeowner}/folder/{folder}",
            params=params,
        )
        return parse_obj_as(
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.SearchItemResponse,
            response,
        )

    async def GetSearchItemsByAssociation_Scope_ScopeOwner_FolderV2(
        self,
        association: str,
        scope: str,
        scopeowner: str,
        folder: str,
        links: Optional[bool] = None,
    ) -> cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData:
        """Get all saved searches by Folder ID

        Operation that returns a tree of saved queries, including scope, search name, IDs, and location within the tree.
         :param association: Use to filter results by Business Object association ID.
         :param scope: Use to filter results by scope name or ID.
         :param scopeowner: Use to filter results by scope owner ID.
         :param folder: Use to filter results by Search Group folder ID.
         :param links: Flag to include hyperlinks in results. Default is false.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
        """
        self.validate_path_param(association)
        self.validate_path_param(scope)
        self.validate_path_param(scopeowner)
        self.validate_path_param(folder)
        params = {}
        if links is not None:
            params["links"] = links
        response = await self.get(
            f"/api/V2/getsearchitems/association/{association}/scope/{scope}/scopeowner/{scopeowner}/folder/{folder}",
            params=params,
        )
        return parse_obj_as(
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData,
            response,
        )

    async def GetSearchItemsByAssociation_Scope_ScopeOwnerV1(
        self,
        association: str,
        scope: str,
        scopeowner: str,
        links: Optional[bool] = None,
    ) -> cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.SearchItemResponse:
        """Get all saved searches by scope owner (sub scope)

        Operation that returns a tree of saved queries, including scope, search name, IDs, and location within the tree.
         :param association: Use to filter results by Business Object association ID.
         :param scope: Use to filter results by scope name or ID.
         :param scopeowner: Use to filter results by scope owner ID.
         :param links: Flag to include hyperlinks in results. Default is false.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.SearchItemResponse
        """
        self.validate_path_param(association)
        self.validate_path_param(scope)
        self.validate_path_param(scopeowner)
        params = {}
        if links is not None:
            params["links"] = links
        response = await self.get(
            f"/api/V1/getsearchitems/association/{association}/scope/{scope}/scopeowner/{scopeowner}",
            params=params,
        )
        return parse_obj_as(
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.SearchItemResponse,
            response,
        )

    async def GetSearchItemsByAssociation_Scope_ScopeOwnerV2(
        self,
        association: str,
        scope: str,
        scopeowner: str,
        links: Optional[bool] = None,
    ) -> cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData:
        """Get all saved searches by scope owner (sub scope)

        Operation that returns a tree of saved queries, including scope, search name, IDs, and location within the tree.
         :param association: Use to filter results by Business Object association ID.
         :param scope: Use to filter results by scope name or ID.
         :param scopeowner: Use to filter results by scope owner ID.
         :param links: Flag to include hyperlinks in results. Default is false.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
        """
        self.validate_path_param(association)
        self.validate_path_param(scope)
        self.validate_path_param(scopeowner)
        params = {}
        if links is not None:
            params["links"] = links
        response = await self.get(
            f"/api/V2/getsearchitems/association/{association}/scope/{scope}/scopeowner/{scopeowner}",
            params=params,
        )
        return parse_obj_as(
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData,
            response,
        )

    async def GetSearchItemsByAssociation_ScopeV1(
        self,
        association: str,
        scope: str,
        links: Optional[bool] = None,
    ) -> cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.SearchItemResponse:
        """Get all saved searches by scope

        Operation that returns a tree of saved queries, including scope, search name, IDs, and location within the tree.
         :param association: Use to filter results by Business Object association ID.
         :param scope: Use to filter results by scope name or ID.
         :param links: Flag to include hyperlinks in results. Default is false.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.SearchItemResponse
        """
        self.validate_path_param(association)
        self.validate_path_param(scope)
        params = {}
        if links is not None:
            params["links"] = links
        response = await self.get(
            f"/api/V1/getsearchitems/association/{association}/scope/{scope}",
            params=params,
        )
        return parse_obj_as(
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.SearchItemResponse,
            response,
        )

    async def GetSearchItemsByAssociation_ScopeV2(
        self,
        association: str,
        scope: str,
        links: Optional[bool] = None,
    ) -> cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData:
        """Get all saved searches by scope

        Operation that returns a tree of saved queries, including scope, search name, IDs, and location within the tree.
         :param association: Use to filter results by Business Object association ID.
         :param scope: Use to filter results by scope name or ID.
         :param links: Flag to include hyperlinks in results. Default is false.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
        """
        self.validate_path_param(association)
        self.validate_path_param(scope)
        params = {}
        if links is not None:
            params["links"] = links
        response = await self.get(
            f"/api/V2/getsearchitems/association/{association}/scope/{scope}",
            params=params,
        )
        return parse_obj_as(
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData,
            response,
        )

    async def GetSearchItemsByAssociationV1(
        self,
        association: str,
        links: Optional[bool] = None,
    ) -> cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.SearchItemResponse:
        """Get all saved searches by Business Object association

        Operation that returns a tree of saved queries, including scope, search name, IDs, and location within the tree.
         :param association: Use to filter results by Business Object association ID.
         :param links: Flag to include hyperlinks in results. Default is false.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.SearchItemResponse
        """
        self.validate_path_param(association)
        params = {}
        if links is not None:
            params["links"] = links
        response = await self.get(
            f"/api/V1/getsearchitems/association/{association}", params=params
        )
        return parse_obj_as(
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.SearchItemResponse,
            response,
        )

    async def GetSearchItemsByAssociationV2(
        self,
        association: str,
        links: Optional[bool] = None,
    ) -> cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData:
        """Get all saved searches by Business Object association

        Operation that returns a tree of saved queries, including scope, search name, IDs, and location within the tree.
         :param association: Use to filter results by Business Object association ID.
         :param links: Flag to include hyperlinks in results. Default is false.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
        """
        self.validate_path_param(association)
        params = {}
        if links is not None:
            params["links"] = links
        response = await self.get(
            f"/api/V2/getsearchitems/association/{association}", params=params
        )
        return parse_obj_as(
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData,
            response,
        )

    async def GetSearchItemsV1(
        self,
        links: Optional[bool] = None,
    ) -> cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.SearchItemResponse:
        """Get all saved searches by default Business Object association

        Operation that returns a tree of saved queries, including scope, search name, IDs, and location within the tree.
         :param links: Flag to include hyperlinks in results. Default is false.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.SearchItemResponse
        """
        params = {}
        if links is not None:
            params["links"] = links
        response = await self.get("/api/V1/getsearchitems", params=params)
        return parse_obj_as(
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.SearchItemResponse,
            response,
        )

    async def GetSearchItemsV2(
        self,
        links: Optional[bool] = None,
    ) -> cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData:
        """Get all saved searches by default Business Object association

        Operation that returns a tree of saved queries, including scope, search name, IDs, and location within the tree.
         :param links: Flag to include hyperlinks in results. Default is false.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData
        """
        params = {}
        if links is not None:
            params["links"] = links
        response = await self.get("/api/V2/getsearchitems", params=params)
        return parse_obj_as(
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core.ManagerData,
            response,
        )

    async def GetSearchResultsAdHocV1(
        self,
        dataRequest: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.SearchResultsRequest,
    ) -> cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.SearchResultsResponse:
        """Run an ad-hoc search

        Operation that runs an ad-hoc Business Object search. To execute a search with Prompts, the PromptId and Value are required in the Prompt request object.

        PromptType is a FieldSubType enum as described below:
        FieldSubType
        None = 0
        Text = 1
        Number = 2
        DateTime = 3
        Logical = 4
        Binary = 5
        DateOnly = 6
        TimeOnly = 7
        Json = 8
        JsonArray = 9
        Xml = 10
        XmlCollection = 11
        TimeValue = 12

         :param dataRequest: Request object to specify search parameters.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.SearchResultsResponse
        """
        response = await self.post_body(
            "/api/V1/getsearchresults",
            content=dataRequest.json(exclude_unset=True, by_alias=True),
        )
        return parse_obj_as(
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.SearchResultsResponse,
            response,
        )

    async def GetSearchResultsByIdV1(
        self,
        association: str,
        scope: str,
        scopeowner: str,
        searchid: str,
        searchTerm: Optional[str] = None,
        pagenumber: Optional[int] = None,
        pagesize: Optional[int] = None,
        includeschema: Optional[bool] = None,
        resultsAsSimpleResultsList: Optional[bool] = None,
    ) -> cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.SearchResultsResponse:
        """Run a saved search by internal ID

        Operation that returns the paged results of a saved search. When the search contains Prompts, the response contains the Prompt. Send the Prompt and the original operation parameters to  SearchResultsRequest to the getsearchresults ad-hoc http post operation.

        PromptType is a FieldSubType enum as described below:
        FieldSubType
        None = 0
        Text = 1
        Number = 2
        DateTime = 3
        Logical = 4
        Binary = 5
        DateOnly = 6
        TimeOnly = 7
        Json = 8
        JsonArray = 9
        Xml = 10
        XmlCollection = 11
        TimeValue = 12

         :param association: Specify the Business Object association ID for the saved search.
         :param scope: Specify the scope name or ID for the saved search.
         :param scopeowner: Specify the scope owner ID for the saved search. Use (None) when no scope owner exists.
         :param searchid: Specify the internal ID for the saved search. Use "Run a saved search by name" if you do not have the internal ID.
         :param searchTerm: Specify search text filter the results. Example: Use "Service Request" to filter Incident results to include only service requests.
         :param pagenumber: Specify the page number of the result set to return.
         :param pagesize: Specify the number of rows to return per page.
         :param includeschema: Use to include the table schema of the saved search. If false, results contain the fieldid and field value without field information. Default is false.
         :param resultsAsSimpleResultsList: Indicates if the results should be returned in a simple results list format or a table format. Default is a table format.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.SearchResultsResponse
        """
        self.validate_path_param(association)
        self.validate_path_param(scope)
        self.validate_path_param(scopeowner)
        self.validate_path_param(searchid)
        params = {}
        if searchTerm is not None:
            params["searchTerm"] = searchTerm
        if pagenumber is not None:
            params["pagenumber"] = pagenumber
        if pagesize is not None:
            params["pagesize"] = pagesize
        if includeschema is not None:
            params["includeschema"] = includeschema
        if resultsAsSimpleResultsList is not None:
            params["resultsAsSimpleResultsList"] = resultsAsSimpleResultsList
        response = await self.get(
            f"/api/V1/getsearchresults/association/{association}/scope/{scope}/scopeowner/{scopeowner}/searchid/{searchid}",
            params=params,
        )
        return parse_obj_as(
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.SearchResultsResponse,
            response,
        )

    async def GetSearchResultsByNameV1(
        self,
        association: str,
        scope: str,
        scopeowner: str,
        searchname: str,
        searchTerm: Optional[str] = None,
        pagenumber: Optional[int] = None,
        pagesize: Optional[int] = None,
        includeschema: Optional[bool] = None,
        resultsAsSimpleResultsList: Optional[bool] = None,
    ) -> cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.SearchResultsResponse:
        """Run a saved search by name

        Operation that returns the paged results of a saved search. When the search contains Prompts, the response contains the Prompt. Send the Prompt and the original operation parameters to  SearchResultsRequest to the getsearchresults ad-hoc http post operation.

        PromptType is a FieldSubType enum as described below:
        FieldSubType
        None = 0
        Text = 1
        Number = 2
        DateTime = 3
        Logical = 4
        Binary = 5
        DateOnly = 6
        TimeOnly = 7
        Json = 8
        JsonArray = 9
        Xml = 10
        XmlCollection = 11
        TimeValue = 12

         :param association: Specify the Business Object association ID for the saved search.
         :param scope: Specify the scope name or ID for the saved search.
         :param scopeowner: Specify the scope owner ID for the saved search. Use (None) when no scope owner exists.
         :param searchname: Specify the name of the saved search.
         :param searchTerm: Specify search text filter the results. Example: Use "Service Request" to filter Incident results to include only service requests.
         :param pagenumber: Specify the page number of the result set to return.
         :param pagesize: Specify the number of rows to return per page.
         :param includeschema: Use to include the table schema of the saved search. If false, results contain the fieldid and field value without field information. Default is false.
         :param resultsAsSimpleResultsList: Indicates if the results should be returned in a simple results list format or a table format. Default is a table format.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.SearchResultsResponse
        """
        self.validate_path_param(association)
        self.validate_path_param(scope)
        self.validate_path_param(scopeowner)
        self.validate_path_param(searchname)
        params = {}
        if searchTerm is not None:
            params["searchTerm"] = searchTerm
        if pagenumber is not None:
            params["pagenumber"] = pagenumber
        if pagesize is not None:
            params["pagesize"] = pagesize
        if includeschema is not None:
            params["includeschema"] = includeschema
        if resultsAsSimpleResultsList is not None:
            params["resultsAsSimpleResultsList"] = resultsAsSimpleResultsList
        response = await self.get(
            f"/api/V1/getsearchresults/association/{association}/scope/{scope}/scopeowner/{scopeowner}/searchname/{searchname}",
            params=params,
        )
        return parse_obj_as(
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.SearchResultsResponse,
            response,
        )

    async def GetSearchResultsExportAdHocV1(
        self,
        dataRequest: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.ExportSearchResultsRequest,
    ) -> str:
        """Export an ad-hoc search

        Operation that returns an ad-hoc search in a specified export format: 0=CSV, 1=Excel, 2=Tab, 3=Word, 4=Custom Separator, 5=Simple JSON. To execute a search with Prompts, the PromptId and Value are required in the Prompt request object.

        PromptType is a FieldSubType enum as described below:
        FieldSubType
        None = 0
        Text = 1
        Number = 2
        DateTime = 3
        Logical = 4
        Binary = 5
        DateOnly = 6
        TimeOnly = 7
        Json = 8
        JsonArray = 9
        Xml = 10
        XmlCollection = 11
        TimeValue = 12

         :param dataRequest: Request object to specify search parameters and export format.
         :return: str"""
        return await self.post_body(
            "/api/V1/getsearchresultsexport",
            content=dataRequest.json(exclude_unset=True, by_alias=True),
        )

    async def GetSearchResultsExportByIdV1(
        self,
        association: str,
        scope: str,
        scopeowner: str,
        searchid: str,
        exportformat: Literal["CSV", "Excel", "Tab", "Word", "CustomSeparator", "Json"],
        searchTerm: Optional[str] = None,
        pagenumber: Optional[int] = None,
        pagesize: Optional[int] = None,
    ) -> str:
        """Export a saved search by ID

        Operation that returns the paged results of a saved search in a specified format. When the search contains Prompts, the response contains the Prompt. Send the Prompt and the original operation parameters to  SearchResultsRequest to the getsearchresultsexport ad-hoc http post operation.

        PromptType is a FieldSubType enum as described below:
        FieldSubType
        None = 0
        Text = 1
        Number = 2
        DateTime = 3
        Logical = 4
        Binary = 5
        DateOnly = 6
        TimeOnly = 7
        Json = 8
        JsonArray = 9
        Xml = 10
        XmlCollection = 11
        TimeValue = 12

         :param association: Specify the Business Object association ID for the saved search.
         :param scope: Specify the scope name or ID for the saved search.
         :param scopeowner: Specify the scope owner ID for the saved search. Use (None) when no scope owner exists.
         :param searchid: Specify the internal ID for the saved search. Use "Run a saved search by name" if you do not have the internal ID.
         :param exportformat: Specify the format of the export
         :param searchTerm: Specify search text filter the results. Example: Use "Service Request" to filter Incident results to include only service requests.
         :param pagenumber: Specify the page number of the result set to return.
         :param pagesize: Specify the number of rows to return per page.
         :return: str"""
        self.validate_path_param(association)
        self.validate_path_param(scope)
        self.validate_path_param(scopeowner)
        self.validate_path_param(searchid)
        self.validate_path_param(exportformat)
        params = {}
        if searchTerm is not None:
            params["searchTerm"] = searchTerm
        if pagenumber is not None:
            params["pagenumber"] = pagenumber
        if pagesize is not None:
            params["pagesize"] = pagesize
        return await self.get(
            f"/api/V1/getsearchresultsexport/association/{association}/scope/{scope}/scopeowner/{scopeowner}/searchid/{searchid}/exportformat/{exportformat}",
            params=params,
        )

    async def GetSearchResultsExportByNameV1(
        self,
        association: str,
        scope: str,
        scopeowner: str,
        searchname: str,
        exportformat: Literal["CSV", "Excel", "Tab", "Word", "CustomSeparator", "Json"],
        searchTerm: Optional[str] = None,
        pagenumber: Optional[int] = None,
        pagesize: Optional[int] = None,
    ) -> str:
        """Export a saved search by name

        Operation that returns the paged results of a saved search in a specified format. When the search contains Prompts, the response contains the Prompt. Send the Prompt and the original operation parameters to  SearchResultsRequest to the getsearchresultsexport ad-hoc http post operation.

        PromptType is a FieldSubType enum as described below:
        FieldSubType
        None = 0
        Text = 1
        Number = 2
        DateTime = 3
        Logical = 4
        Binary = 5
        DateOnly = 6
        TimeOnly = 7
        Json = 8
        JsonArray = 9
        Xml = 10
        XmlCollection = 11
        TimeValue = 12

         :param association: Specify the Business Object association ID for the saved search.
         :param scope: Specify the scope name or ID for the saved search.
         :param scopeowner: Specify the scope owner ID for the saved search. Use (None) when no scope owner exists.
         :param searchname: Specify the name of the saved search.
         :param exportformat: Specify the format of the export
         :param searchTerm: Specify search text filter the results. Example: Use "Service Request" to filter Incident results to include only service requests.
         :param pagenumber: Specify the page number of the result set to return.
         :param pagesize: Specify the number of rows to return per page.
         :return: str"""
        self.validate_path_param(association)
        self.validate_path_param(scope)
        self.validate_path_param(scopeowner)
        self.validate_path_param(searchname)
        self.validate_path_param(exportformat)
        params = {}
        if searchTerm is not None:
            params["searchTerm"] = searchTerm
        if pagenumber is not None:
            params["pagenumber"] = pagenumber
        if pagesize is not None:
            params["pagesize"] = pagesize
        return await self.get(
            f"/api/V1/getsearchresultsexport/association/{association}/scope/{scope}/scopeowner/{scopeowner}/searchname/{searchname}/exportformat/{exportformat}",
            params=params,
        )

    async def GetSearchResultsAsStringByNameV1(
        self,
        scope: str,
        associationName: str,
        searchName: str,
        scopeOwner: Optional[str] = None,
    ) -> List[Dict]:
        """Get results of a saved search

        Operation that returns the results of a saved search in JSON format.

                        This API is protected by a rate limiter and will reject any requests sent from an IP Address when a certain threshold of active concurrent requests has been hit.

                        This value can be configured by the Max Concurrent Requests configuration value in the Web API config.

                        Once this limit has been reached, all subsequent requests will receive a status code of 429 (Too Many Requests).

         :param scope: Specify the scope name for the saved search.
         :param associationName: Specify the Business Object association Name for the saved search.
         :param searchName: Specify the name of the saved search.
         :param scopeOwner: Specify the scope owner ID for the saved search. Use (None) when no scope owner exists.
         :return: List[Dict]"""
        self.validate_path_param(scope)
        self.validate_path_param(associationName)
        self.validate_path_param(searchName)
        params = {}
        if scopeOwner is not None:
            params["scopeOwner"] = scopeOwner
        return await self.get(
            f"/api/V1/storedsearches/{scope}/{associationName}/{searchName}",
            params=params,
        )

    async def GetSearchResultsAsStringByNameV2(
        self,
        scope: str,
        associationName: str,
        searchName: str,
        scopeOwner: Optional[str] = None,
    ) -> List[Dict]:
        """Get results of a saved search

        Operation that returns the results of a saved search in JSON format.

        This API is protected by a rate limiter and will reject any requests sent from an IP Address when a certain threshold of active concurrent requests has been hit.

        This value can be configured by the Max Concurrent Requests configuration value in the Web API config.

        Once this limit has been reached, all subsequent requests will receive a status code of 429 (Too Many Requests).

        This version is not subject to row limits and will return the entire result set of the stored search.

         :param scope: Specify the scope name for the saved search.
         :param associationName: Specify the Business Object association Name for the saved search.
         :param searchName: Specify the name of the saved search.
         :param scopeOwner: Specify the scope owner ID for the saved search. Use (None) when no scope owner exists.
         :return: List[Dict]"""
        self.validate_path_param(scope)
        self.validate_path_param(associationName)
        self.validate_path_param(searchName)
        params = {}
        if scopeOwner is not None:
            params["scopeOwner"] = scopeOwner
        return await self.get(
            f"/api/V2/storedsearches/{scope}/{associationName}/{searchName}",
            params=params,
        )

    async def GetSearchResultsAsStringByIdV2(
        self,
        searchRequest: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.StoredSearchRequest,
    ) -> cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.StoredSearchResults:
        """Get results of a saved search

        Operation that returns the results of a saved search in JSON format.

        This API is protected by a rate limiter and will reject any requests sent from an IP Address when a certain threshold of active concurrent requests has been hit.

        This value can be configured by the Max Concurrent Requests configuration value in the Web API config.

        Once this limit has been reached, all subsequent requests will receive a status code of 429 (Too Many Requests).

        This version is not subject to row limits and will return the entire result set of the stored search.

         :param searchRequest: Request object to specify search parameters.
         :return: cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.StoredSearchResults
        """
        response = await self.post_body(
            "/api/V2/storedsearches",
            content=searchRequest.json(exclude_unset=True, by_alias=True),
        )
        return parse_obj_as(
            cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches.StoredSearchResults,
            response,
        )
