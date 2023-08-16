# Generated by codegen.py
# pyright: reportUnusedImport=false, reportMissingTypeArgument=false

from __future__ import annotations

from enum import Enum
from typing import Dict, List, Optional

import cherwell_pydantic_api.types as ct
from cherwell_pydantic_api.generated_api_utils import ApiBaseModel

from .... import CherwellObjectID
from . import BusinessObject, Core


class FilterInfo(ApiBaseModel):
    fieldId: Optional[ct.FieldID] = None
    operator: Optional[str] = None
    value: Optional[str] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class SortInfo(ApiBaseModel):
    fieldId: Optional[ct.FieldID] = None
    sortDirection: Optional[int] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class QuickSearchConfigSavedRequest(ApiBaseModel):
    standIn: Optional[str] = None
    busObIds: Optional[List[str]] = None
    isGeneral: Optional[bool] = None


from cherwell_pydantic_api.generated_api_utils import HttpStatusCode


class ChangedOption(Enum):
    None_ = 'None'
    Use = 'Use'
    Display = 'Display'
    UseAndDisplay = 'UseAndDisplay'


class NonFinalStateOption(Enum):
    None_ = 'None'
    Use = 'Use'
    Display = 'Display'
    UseAndDisplay = 'UseAndDisplay'


class SearchAnyWordsOption(Enum):
    None_ = 'None'
    Use = 'Use'
    Display = 'Display'
    UseAndDisplay = 'UseAndDisplay'


class SearchAttachmentsOption(Enum):
    None_ = 'None'
    Use = 'Use'
    Display = 'Display'
    UseAndDisplay = 'UseAndDisplay'


class SearchRelatedOption(Enum):
    None_ = 'None'
    Use = 'Use'
    Display = 'Display'
    UseAndDisplay = 'UseAndDisplay'


class SearchTargetType(Enum):
    BusOb = 'BusOb'
    DocRepository = 'DocRepository'


class SortByOption(Enum):
    None_ = 'None'
    Use = 'Use'
    Display = 'Display'
    UseAndDisplay = 'UseAndDisplay'


from enum import Enum

import cherwell_pydantic_api.types as ct


class ChangedLimit(ApiBaseModel):
    displayName: Optional[str] = None
    units: Optional[str] = None
    value: Optional[int] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class QuickSearchConfigurationRequest(ApiBaseModel):
    busObIds: Optional[List[str]] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class QuickSearchByIdRequest(ApiBaseModel):
    busObIds: Optional[List[str]] = None
    isGeneral: Optional[bool] = None
    searchText: Optional[str] = None
    standIn: Optional[str] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class SimpleResultsListItem(ApiBaseModel):
    busObId: Optional[ct.BusObID] = None
    busObRecId: Optional[ct.BusObRecID] = None
    docRepositoryItemId: Optional[str] = None
    galleryImage: Optional[str] = None
    links: Optional[List[Core.CherwellLink]] = None
    publicId: Optional[str] = None
    scope: Optional[str] = None
    scopeOwner: Optional[str] = None
    subTitle: Optional[str] = None
    text: Optional[str] = None
    title: Optional[str] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class QuickSearchRequest(ApiBaseModel):
    busObIds: Optional[List[str]] = None
    searchText: Optional[str] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class QuickSearchSpecificByIdRequest(ApiBaseModel):
    busObIds: Optional[List[str]] = None
    standIn: Optional[str] = None
    ascending: Optional[bool] = None
    isBusObTarget: Optional[bool] = None
    nonFinalState: Optional[bool] = None
    searchAnyWords: Optional[bool] = None
    searchAttachments: Optional[bool] = None
    searchRelated: Optional[bool] = None
    searchText: Optional[str] = None
    selectedChangedLimit: Optional[ChangedLimit] = None
    selectedSortByFieldId: Optional[ct.FieldID] = None
    sortByRelevance: Optional[bool] = None
    specificSearchTargetId: Optional[str] = None
    useSortBy: Optional[bool] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class Field(ApiBaseModel):
    caption: Optional[str] = None
    currencyCulture: Optional[str] = None
    currencySymbol: Optional[str] = None
    decimalDigits: Optional[int] = None
    defaultSortOrderAscending: Optional[bool] = None
    displayName: Optional[str] = None
    fieldName: Optional[str] = None
    fullFieldId: Optional[ct.FieldID] = None
    hasDefaultSortField: Optional[bool] = None
    fieldId: Optional[ct.FieldID] = None
    isBinary: Optional[bool] = None
    isCurrency: Optional[bool] = None
    isDateTime: Optional[bool] = None
    isFilterAllowed: Optional[bool] = None
    isLogical: Optional[bool] = None
    isNumber: Optional[bool] = None
    isShortDate: Optional[bool] = None
    isShortTime: Optional[bool] = None
    isVisible: Optional[bool] = None
    sortable: Optional[bool] = None
    sortOrder: Optional[str] = None
    storageName: Optional[str] = None
    wholeDigits: Optional[int] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class SearchResultsRow(ApiBaseModel):
    busObId: Optional[ct.BusObID] = None
    busObRecId: Optional[ct.BusObRecID] = None
    links: Optional[List[Core.CherwellLink]] = None
    publicId: Optional[str] = None
    rowColor: Optional[str] = None
    searchResultsFieldValues: Optional[List[BusinessObject.FieldTemplateItem]] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class QuickSearchSpecificRequest(ApiBaseModel):
    ascending: Optional[bool] = None
    isBusObTarget: Optional[bool] = None
    nonFinalState: Optional[bool] = None
    searchAnyWords: Optional[bool] = None
    searchAttachments: Optional[bool] = None
    searchRelated: Optional[bool] = None
    searchText: Optional[str] = None
    selectedChangedLimit: Optional[ChangedLimit] = None
    selectedSortByFieldId: Optional[ct.FieldID] = None
    sortByRelevance: Optional[bool] = None
    specificSearchTargetId: Optional[str] = None
    useSortBy: Optional[bool] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class Association(ApiBaseModel):
    busObId: Optional[ct.BusObID] = None
    busObName: Optional[str] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class SearchItem(ApiBaseModel):
    association: Optional[str] = None
    links: Optional[List[Core.CherwellLink]] = None
    localizedScopeName: Optional[str] = None
    parentFolderId: Optional[str] = None
    scope: Optional[str] = None
    scopeOwner: Optional[str] = None
    searchId: Optional[str] = None
    searchName: Optional[str] = None


class ExportFormat(Enum):
    CSV = 'CSV'
    Excel = 'Excel'
    Tab = 'Tab'
    Word = 'Word'
    CustomSeparator = 'CustomSeparator'
    Json = 'Json'


from enum import Enum

import cherwell_pydantic_api.types as ct


class ExportSearchResultsRequest(ApiBaseModel):
    customSeparator: Optional[str] = None
    exportFormat: Optional[ExportFormat] = None
    exportTitle: Optional[str] = None
    association: Optional[str] = None
    associationName: Optional[str] = None
    busObId: Optional[ct.BusObID] = None
    customGridDefId: Optional[str] = None
    dateTimeFormatting: Optional[str] = None
    fieldId: Optional[ct.FieldID] = None
    fields: Optional[List[str]] = None
    filters: Optional[List[FilterInfo]] = None
    includeAllFields: Optional[bool] = None
    includeSchema: Optional[bool] = None
    pageNumber: Optional[int] = None
    pageSize: Optional[int] = None
    scope: Optional[str] = None
    scopeOwner: Optional[str] = None
    searchId: Optional[str] = None
    searchName: Optional[str] = None
    searchText: Optional[str] = None
    sorting: Optional[List[SortInfo]] = None
    promptValues: Optional[List[Core.PromptValue]] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class StoredSearchRequest(ApiBaseModel):
    associationId: Optional[str] = None
    associationName: Optional[str] = None
    gridId: Optional[str] = None
    includeSchema: Optional[bool] = None
    scope: Optional[str] = None
    scopeOwnerId: Optional[str] = None
    searchId: Optional[str] = None
    searchName: Optional[str] = None


class Type(Enum):
    Text = 'Text'
    Number = 'Number'
    Currency = 'Currency'
    Integer = 'Integer'
    Datetime = 'Datetime'
    Date = 'Date'
    Time = 'Time'
    Logical = 'Logical'


from enum import Enum

import cherwell_pydantic_api.types as ct


class ColumnSchema(ApiBaseModel):
    name: Optional[str] = None
    fieldId: Optional[ct.FieldID] = None
    type: Optional[Type] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class RelatedBusinessObjectRequest(ApiBaseModel):
    allFields: Optional[bool] = None
    customGridId: Optional[str] = None
    fieldsList: Optional[List[str]] = None
    filters: Optional[List[FilterInfo]] = None
    pageNumber: Optional[int] = None
    pageSize: Optional[int] = None
    parentBusObId: Optional[ct.BusObID] = None
    parentBusObRecId: Optional[ct.BusObRecID] = None
    relationshipId: Optional[ct.RelationshipID] = None
    sorting: Optional[List[SortInfo]] = None
    useDefaultGrid: Optional[bool] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class QuickSearchItem(ApiBaseModel):
    ascending: Optional[bool] = None
    changedLimits: Optional[List[ChangedLimit]] = None
    changedOption: Optional[ChangedOption] = None
    displayName: Optional[str] = None
    galleryImage: Optional[str] = None
    hasAnyOptions: Optional[bool] = None
    nonFinalStateOption: Optional[NonFinalStateOption] = None
    searchAnyWordsOption: Optional[SearchAnyWordsOption] = None
    searchAttachmentsOption: Optional[SearchAttachmentsOption] = None
    searchRelatedOption: Optional[SearchRelatedOption] = None
    searchTargetId: Optional[str] = None
    searchTargetType: Optional[SearchTargetType] = None
    selectedChangedLimit: Optional[ChangedLimit] = None
    selectedSortByFieldId: Optional[ct.FieldID] = None
    sortByFields: Optional[Dict[str, str]] = None
    sortByOption: Optional[SortByOption] = None
    watermarkText: Optional[str] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class SimpleResultsListGroup(ApiBaseModel):
    isBusObTarget: Optional[bool] = None
    simpleResultsListItems: Optional[List[SimpleResultsListItem]] = None
    subTitle: Optional[str] = None
    targetId: Optional[str] = None
    title: Optional[str] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class SearchResultsTableResponse(ApiBaseModel):
    columns: Optional[List[Field]] = None
    rows: Optional[List[SearchResultsRow]] = None
    sorting: Optional[List[SortInfo]] = None
    totalRows: Optional[int] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class SearchFolder(ApiBaseModel):
    association: Optional[str] = None
    childFolders: Optional[List[SearchFolder]] = None
    childItems: Optional[List[SearchItem]] = None
    folderId: Optional[str] = None
    folderName: Optional[str] = None
    links: Optional[List[Core.CherwellLink]] = None
    localizedScopeName: Optional[str] = None
    parentFolderId: Optional[str] = None
    scope: Optional[str] = None
    scopeOwner: Optional[str] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class SearchResultsRequest(ApiBaseModel):
    association: Optional[str] = None
    associationName: Optional[str] = None
    busObId: Optional[ct.BusObID] = None
    customGridDefId: Optional[str] = None
    dateTimeFormatting: Optional[str] = None
    fieldId: Optional[ct.FieldID] = None
    fields: Optional[List[str]] = None
    filters: Optional[List[FilterInfo]] = None
    includeAllFields: Optional[bool] = None
    includeSchema: Optional[bool] = None
    pageNumber: Optional[int] = None
    pageSize: Optional[int] = None
    scope: Optional[str] = None
    scopeOwner: Optional[str] = None
    searchId: Optional[str] = None
    searchName: Optional[str] = None
    searchText: Optional[str] = None
    sorting: Optional[List[SortInfo]] = None
    promptValues: Optional[List[Core.PromptValue]] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class StoredSearchResults(ApiBaseModel):
    columns: Optional[List[ColumnSchema]] = None
    rows: Optional[List[List[CherwellObjectID]]] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class RelatedBusinessObjectResponse(ApiBaseModel):
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    links: Optional[List[Core.CherwellLink]] = None
    pageNumber: Optional[int] = None
    pageSize: Optional[int] = None
    parentBusObId: Optional[ct.BusObID] = None
    parentBusObPublicId: Optional[str] = None
    parentBusObRecId: Optional[ct.BusObRecID] = None
    relatedBusinessObjects: Optional[List[BusinessObject.ReadResponse]] = None
    relationshipId: Optional[ct.RelationshipID] = None
    totalRecords: Optional[int] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class QuickSearchConfigurationResponse(ApiBaseModel):
    allowQuickSearch: Optional[bool] = None
    allowSpecificSearch: Optional[bool] = None
    defaultToQuickSearch: Optional[bool] = None
    displayName: Optional[str] = None
    galleryImage: Optional[str] = None
    history: Optional[List[str]] = None
    includeAvailableInSpecific: Optional[bool] = None
    includeQuickSearchInSpecific: Optional[bool] = None
    quickSearchId: Optional[str] = None
    quickSearchItems: Optional[List[QuickSearchItem]] = None
    quickSearchWatermark: Optional[str] = None
    sortByRelevance: Optional[bool] = None
    resolvedQuickSearchWatermark: Optional[str] = None
    scope: Optional[str] = None
    scopeOwner: Optional[str] = None
    specificSearchItems: Optional[List[QuickSearchItem]] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class SimpleResultsList(ApiBaseModel):
    groups: Optional[List[SimpleResultsListGroup]] = None
    title: Optional[str] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class QuickSearchResponse(ApiBaseModel):
    searchResultsTable: Optional[SearchResultsTableResponse] = None
    simpleResultsList: Optional[SimpleResultsList] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class SearchItemResponse(ApiBaseModel):
    root: Optional[SearchFolder] = None
    supportedAssociations: Optional[List[Association]] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class SearchResultsResponse(ApiBaseModel):
    businessObjects: Optional[List[BusinessObject.ReadResponse]] = None
    hasPrompts: Optional[bool] = None
    links: Optional[List[Core.CherwellLink]] = None
    prompts: Optional[List[Core.Prompt]] = None
    searchResultsFields: Optional[List[Field]] = None
    simpleResults: Optional[SimpleResultsList] = None
    totalRows: Optional[int] = None
    hasMoreRecords: Optional[bool] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


SearchFolder.model_rebuild()
