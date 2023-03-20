# generated by datamodel-codegen:
#   filename:  swagger.json
#   timestamp: 2023-03-19T19:24:29+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional

import cherwell_pydantic_api.types as ct
from cherwell_pydantic_api.generated_api_utils import ApiBaseModel

from .... import CherwellObjectID
from ... import CherwellNameValuePair


class CherwellLink(ApiBaseModel):
    name: Optional[str] = None
    url: Optional[str] = None


import cherwell_pydantic_api.types as ct
from cherwell_pydantic_api.generated_api_utils import HttpStatusCode


class ManagerItem(ApiBaseModel):
    association: Optional[str] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    galleryImage: Optional[str] = None
    id: Optional[str] = None
    links: Optional[List[CherwellLink]] = None
    localizedScopeName: Optional[str] = None
    name: Optional[str] = None
    parentFolder: Optional[str] = None
    parentIsScopeFolder: Optional[bool] = None
    scope: Optional[str] = None
    scopeOwner: Optional[str] = None
    standInKey: Optional[str] = None


class StoredValueType(Enum):
    Text = 'Text'
    Number = 'Number'
    DateTime = 'DateTime'
    Logical = 'Logical'
    Color = 'Color'
    Json = 'Json'
    JsonArray = 'JsonArray'
    Xml = 'Xml'
    XmlCollection = 'XmlCollection'


import cherwell_pydantic_api.types as ct


class StoredValueResponse(ApiBaseModel):
    description: Optional[str] = None
    folder: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    scope: Optional[str] = None
    scopeOwner: Optional[str] = None
    standInKey: Optional[str] = None
    storedValueType: Optional[StoredValueType] = None
    value: Optional[str] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


import cherwell_pydantic_api.types as ct


class View(ApiBaseModel):
    name: Optional[str] = None
    viewId: Optional[str] = None
    image: Optional[str] = None


class Level(Enum):
    Fatal = 'Fatal'
    Error = 'Error'
    Warning = 'Warning'
    Info = 'Info'
    Stats = 'Stats'
    Debug = 'Debug'


import cherwell_pydantic_api.types as ct


class LogRequest(ApiBaseModel):
    keyValueProperties: Optional[List[CherwellObjectID]] = None
    level: Optional[Level] = None
    message: Optional[str] = None


class ImageType(Enum):
    Imported = 'Imported'
    File = 'File'
    Url = 'Url'


import cherwell_pydantic_api.types as ct


class SaveGalleryImageRequest(ApiBaseModel):
    base64EncodedImageData: Optional[str] = None
    description: Optional[str] = None
    folder: Optional[str] = None
    imageType: Optional[ImageType] = None
    name: Optional[str] = None
    scope: Optional[str] = None
    scopeOwner: Optional[str] = None
    standInKey: Optional[str] = None


import cherwell_pydantic_api.types as ct


class SaveGalleryImageResponse(ApiBaseModel):
    name: Optional[str] = None
    standInKey: Optional[str] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


import cherwell_pydantic_api.types as ct


class SaveStoredValueRequest(ApiBaseModel):
    description: Optional[str] = None
    folder: Optional[str] = None
    name: Optional[str] = None
    scope: Optional[str] = None
    scopeOwner: Optional[str] = None
    standInKey: Optional[str] = None
    storedValueType: Optional[StoredValueType] = None
    value: Optional[str] = None


class ActionType(Enum):
    None_ = 'None'
    OneStep = 'OneStep'
    Command = 'Command'
    BuiltIn = 'BuiltIn'
    Category = 'Category'
    SearchGrp = 'SearchGrp'
    Report = 'Report'
    Dashboard = 'Dashboard'
    Calendar = 'Calendar'
    Visualization = 'Visualization'
    Group = 'Group'
    Page = 'Page'
    DocRepository = 'DocRepository'
    PortalCommand = 'PortalCommand'
    ActionCatalog = 'ActionCatalog'
    OneStepForRecord = 'OneStepForRecord'


class LoginEnabledMode(Enum):
    Anonymous = 'Anonymous'
    LoggedIn = 'LoggedIn'
    Both = 'Both'


class LoginVisibilityMode(Enum):
    Anonymous = 'Anonymous'
    LoggedIn = 'LoggedIn'
    Both = 'Both'


import cherwell_pydantic_api.types as ct


class Action(ApiBaseModel):
    actionCommand: Optional[str] = None
    actionType: Optional[ActionType] = None
    alwaysTextAndImage: Optional[bool] = None
    beginGroup: Optional[bool] = None
    childActions: Optional[List[Action]] = None
    dependencies: Optional[List[str]] = None
    displayText: Optional[str] = None
    enabled: Optional[bool] = None
    galleryImage: Optional[str] = None
    helpText: Optional[str] = None
    loginEnabledMode: Optional[LoginEnabledMode] = None
    loginVisibilityMode: Optional[LoginVisibilityMode] = None
    name: Optional[str] = None
    parameters: Optional[Dict[str, str]] = None
    visible: Optional[bool] = None


import cherwell_pydantic_api.types as ct


class Location(ApiBaseModel):
    altitude: Optional[float] = None
    busObId: Optional[ct.BusObID] = None
    busObRecId: Optional[ct.BusObRecID] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None


import cherwell_pydantic_api.types as ct


class SimplePromptValue(ApiBaseModel):
    promptDefId: Optional[str] = None
    promptName: Optional[str] = None
    value: Optional[str] = None


import cherwell_pydantic_api.types as ct


class PromptValue(ApiBaseModel):
    busObId: Optional[ct.BusObID] = None
    collectionStoreEntireRow: Optional[str] = None
    collectionValueField: Optional[str] = None
    fieldId: Optional[str] = None
    listReturnFieldId: Optional[str] = None
    promptId: Optional[str] = None
    value: Optional[CherwellObjectID] = None
    valueIsRecId: Optional[bool] = None


class ListDisplayOption(Enum):
    Auto = 'Auto'
    Text = 'Text'
    Combo = 'Combo'
    GridList = 'GridList'
    SimpleList = 'SimpleList'
    PromptSimpleGrid = 'PromptSimpleGrid'


class PromptType(Enum):
    None_ = 'None'
    Text = 'Text'
    Number = 'Number'
    DateTime = 'DateTime'
    Logical = 'Logical'
    Binary = 'Binary'
    DateOnly = 'DateOnly'
    TimeOnly = 'TimeOnly'
    Json = 'Json'
    JsonArray = 'JsonArray'
    Xml = 'Xml'
    XmlCollection = 'XmlCollection'
    TimeValue = 'TimeValue'


import cherwell_pydantic_api.types as ct


class Prompt(ApiBaseModel):
    allowValuesOnly: Optional[bool] = None
    busObId: Optional[ct.BusObID] = None
    collectionStoreEntireRow: Optional[str] = None
    collectionValueField: Optional[str] = None
    constraintXml: Optional[str] = None
    contents: Optional[str] = None
    default: Optional[str] = None
    fieldId: Optional[str] = None
    isDateRange: Optional[bool] = None
    listDisplayOption: Optional[ListDisplayOption] = None
    listReturnFieldId: Optional[str] = None
    multiLine: Optional[bool] = None
    promptId: Optional[str] = None
    promptType: Optional[PromptType] = None
    promptTypeName: Optional[str] = None
    required: Optional[bool] = None
    text: Optional[str] = None
    value: Optional[CherwellObjectID] = None
    values: Optional[List[str]] = None


import cherwell_pydantic_api.types as ct


class ServiceInfoResponse(ApiBaseModel):
    apiVersion: Optional[str] = None
    csmCulture: Optional[str] = None
    csmVersion: Optional[str] = None
    systemDateTime: Optional[datetime] = None
    timeZone: Optional[CherwellObjectID] = None
    systemUtcOffset: Optional[str] = None


import cherwell_pydantic_api.types as ct


class ManagerFolder(ApiBaseModel):
    association: Optional[str] = None
    childFolders: Optional[List[ManagerFolder]] = None
    childItems: Optional[List[ManagerItem]] = None
    id: Optional[str] = None
    links: Optional[List[CherwellLink]] = None
    localizedScopeName: Optional[str] = None
    name: Optional[str] = None
    parentId: Optional[str] = None
    scope: Optional[str] = None
    scopeOwner: Optional[str] = None


import cherwell_pydantic_api.types as ct


class ViewsResponse(ApiBaseModel):
    views: Optional[List[View]] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


import cherwell_pydantic_api.types as ct


class LogBatchRequest(ApiBaseModel):
    logRequests: Optional[List[LogRequest]] = None


import cherwell_pydantic_api.types as ct


class ManagerData(ApiBaseModel):
    root: Optional[ManagerFolder] = None
    supportedAssociations: Optional[List[CherwellNameValuePair]] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


Action.update_forward_refs()
ManagerFolder.update_forward_refs()
