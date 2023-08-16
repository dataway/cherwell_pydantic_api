# Generated by codegen.py
# pyright: reportUnusedImport=false, reportMissingTypeArgument=false

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List, Optional

import cherwell_pydantic_api.types as ct
from cherwell_pydantic_api.generated_api_utils import ApiBaseModel, HttpStatusCode

from . import Core


class FieldValidationError(ApiBaseModel):
    error: Optional[str] = None
    errorCode: Optional[str] = None
    fieldId: Optional[ct.FieldID] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class NotificationTrigger(ApiBaseModel):
    sourceType: Optional[str] = None
    sourceId: Optional[str] = None
    sourceChange: Optional[str] = None
    key: Optional[str] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class DeleteRequest(ApiBaseModel):
    busObId: Optional[ct.BusObID] = None
    busObPublicId: Optional[str] = None
    busObRecId: Optional[ct.BusObRecID] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class DeleteResponse(ApiBaseModel):
    busObId: Optional[ct.BusObID] = None
    busObPublicId: Optional[str] = None
    busObRecId: Optional[ct.BusObRecID] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class FieldTemplateItem(ApiBaseModel):
    dirty: Optional[bool] = None
    displayName: Optional[str] = None
    fieldId: Optional[ct.FieldID] = None
    fullFieldId: Optional[ct.FieldID] = None
    html: Optional[str] = None
    name: Optional[str] = None
    value: Optional[str] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class FieldValuesLookupRequest(ApiBaseModel):
    busbPublicId: Optional[str] = None
    busObId: Optional[ct.BusObID] = None
    busObRecId: Optional[ct.BusObRecID] = None
    fieldId: Optional[ct.FieldID] = None
    fieldName: Optional[str] = None
    fields: Optional[List[FieldTemplateItem]] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class FieldValuesLookupResponse(ApiBaseModel):
    values: Optional[List[str]] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class BusObActivity(ApiBaseModel):
    id: Optional[str] = None
    parentBusObDefId: Optional[str] = None
    parentBusObRecId: Optional[ct.BusObRecID] = None
    historyBusObDefId: Optional[str] = None
    historyBusObRecId: Optional[ct.BusObRecID] = None
    type: Optional[str] = None
    title: Optional[str] = None
    body: Optional[str] = None
    createdBy: Optional[str] = None
    created: Optional[datetime] = None
    modified: Optional[datetime] = None
    modifiedBy: Optional[str] = None


class AttachmentType(Enum):
    Imported = 'Imported'
    Linked = 'Linked'
    URL = 'URL'


class Scope(Enum):
    None_ = 'None'
    Global = 'Global'
    Team = 'Team'
    Persona = 'Persona'
    SecurityGroup = 'SecurityGroup'
    User = 'User'
    UserInPersona = 'UserInPersona'
    OtherUsers = 'OtherUsers'
    Core = 'Core'
    BusIntel = 'BusIntel'
    FromResource = 'FromResource'
    Site = 'Site'
    Custom = 'Custom'
    BusObRecord = 'BusObRecord'


class Type(Enum):
    None_ = 'None'
    File = 'File'
    FileManagerFile = 'FileManagerFile'
    BusOb = 'BusOb'
    History = 'History'
    Other = 'Other'
    Solution = 'Solution'
    UsedAsSolution = 'UsedAsSolution'
    ExternalSolution = 'ExternalSolution'


from enum import Enum

import cherwell_pydantic_api.types as ct


class Attachment(ApiBaseModel):
    attachedBusObId: Optional[ct.BusObID] = None
    attachedBusObRecId: Optional[ct.BusObRecID] = None
    attachmentFileId: Optional[str] = None
    attachmentFileName: Optional[str] = None
    attachmentFileType: Optional[str] = None
    attachmentId: Optional[str] = None
    attachmentType: Optional[AttachmentType] = None
    busObId: Optional[ct.BusObID] = None
    busObRecId: Optional[ct.BusObRecID] = None
    comment: Optional[str] = None
    created: Optional[datetime] = None
    displayText: Optional[str] = None
    links: Optional[List[Core.CherwellLink]] = None
    owner: Optional[str] = None
    scope: Optional[Scope] = None
    scopeOwner: Optional[str] = None
    type: Optional[Type] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class AttachmentsRequest(ApiBaseModel):
    attachmentId: Optional[str] = None
    attachmentTypes: Optional[List[AttachmentType]] = None
    busObId: Optional[ct.BusObID] = None
    busObName: Optional[str] = None
    busObPublicId: Optional[str] = None
    busObRecId: Optional[ct.BusObRecID] = None
    includeLinks: Optional[bool] = None
    types: Optional[List[Type]] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class ReadRequest(ApiBaseModel):
    busObId: Optional[ct.BusObID] = None
    busObPublicId: Optional[str] = None
    busObRecId: Optional[ct.BusObRecID] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class BarcodeLookupResponse(ApiBaseModel):
    busObId: Optional[ct.BusObID] = None
    busObRecId: Optional[ct.BusObRecID] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class FieldDefinition(ApiBaseModel):
    autoFill: Optional[bool] = None
    calculated: Optional[bool] = None
    category: Optional[str] = None
    decimalDigits: Optional[int] = None
    description: Optional[str] = None
    details: Optional[str] = None
    displayName: Optional[str] = None
    enabled: Optional[bool] = None
    fieldId: Optional[ct.FieldID] = None
    hasDate: Optional[bool] = None
    hasTime: Optional[bool] = None
    isFullTextSearchable: Optional[bool] = None
    maximumSize: Optional[str] = None
    name: Optional[str] = None
    readOnly: Optional[bool] = None
    required: Optional[bool] = None
    type: Optional[str] = None
    typeLocalized: Optional[str] = None
    validated: Optional[bool] = None
    wholeDigits: Optional[int] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class GridDefinition(ApiBaseModel):
    gridId: Optional[str] = None
    name: Optional[str] = None
    displayName: Optional[str] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class Relationship(ApiBaseModel):
    cardinality: Optional[str] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    fieldDefinitions: Optional[List[FieldDefinition]] = None
    relationshipId: Optional[ct.RelationshipID] = None
    target: Optional[str] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class Summary(ApiBaseModel):
    firstRecIdField: Optional[str] = None
    groupSummaries: Optional[List[Summary]] = None
    recIdFields: Optional[str] = None
    stateFieldId: Optional[ct.FieldID] = None
    states: Optional[str] = None
    busObId: Optional[ct.BusObID] = None
    displayName: Optional[str] = None
    group: Optional[bool] = None
    lookup: Optional[bool] = None
    major: Optional[bool] = None
    name: Optional[str] = None
    supporting: Optional[bool] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class TemplateRequest(ApiBaseModel):
    busObId: Optional[ct.BusObID] = None
    fieldNames: Optional[List[str]] = None
    fieldIds: Optional[List[str]] = None
    includeAll: Optional[bool] = None
    includeRequired: Optional[bool] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class TemplateResponse(ApiBaseModel):
    fields: Optional[List[FieldTemplateItem]] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class ViewSummary(ApiBaseModel):
    groupSummaries: Optional[List[ViewSummary]] = None
    image: Optional[str] = None
    isPartOfView: Optional[bool] = None
    busObId: Optional[ct.BusObID] = None
    displayName: Optional[str] = None
    group: Optional[bool] = None
    lookup: Optional[bool] = None
    major: Optional[bool] = None
    name: Optional[str] = None
    supporting: Optional[bool] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class SaveBusObAttachmentRequest(ApiBaseModel):
    attachBusObId: Optional[ct.BusObID] = None
    attachBusObName: Optional[str] = None
    attachBusObPublicId: Optional[str] = None
    attachBusObRecId: Optional[ct.BusObRecID] = None
    busObId: Optional[ct.BusObID] = None
    busObName: Optional[str] = None
    busObPublicId: Optional[str] = None
    busObRecId: Optional[ct.BusObRecID] = None
    comment: Optional[str] = None
    includeLinks: Optional[bool] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class SaveLinkAttachmentRequest(ApiBaseModel):
    busObId: Optional[ct.BusObID] = None
    busObName: Optional[str] = None
    busObPublicId: Optional[str] = None
    busObRecId: Optional[ct.BusObRecID] = None
    comment: Optional[str] = None
    displayText: Optional[str] = None
    includeLinks: Optional[bool] = None
    uncFilePath: Optional[str] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class SaveUrlAttachmentRequest(ApiBaseModel):
    busObId: Optional[ct.BusObID] = None
    busObName: Optional[str] = None
    busObPublicId: Optional[str] = None
    busObRecId: Optional[ct.BusObRecID] = None
    comment: Optional[str] = None
    displayText: Optional[str] = None
    includeLinks: Optional[bool] = None
    url: Optional[str] = None


class CacheScope(Enum):
    Tenant = 'Tenant'
    User = 'User'
    Session = 'Session'


from enum import Enum

import cherwell_pydantic_api.types as ct


class SaveRequest(ApiBaseModel):
    busObId: Optional[ct.BusObID] = None
    busObPublicId: Optional[str] = None
    busObRecId: Optional[ct.BusObRecID] = None
    cacheKey: Optional[str] = None
    cacheScope: Optional[CacheScope] = None
    fields: Optional[List[FieldTemplateItem]] = None
    persist: Optional[bool] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class RelatedSaveRequest(ApiBaseModel):
    parentBusObId: Optional[ct.BusObID] = None
    parentBusObPublicId: Optional[str] = None
    parentBusObRecId: Optional[ct.BusObRecID] = None
    relationshipId: Optional[ct.RelationshipID] = None
    busObId: Optional[ct.BusObID] = None
    busObPublicId: Optional[str] = None
    busObRecId: Optional[ct.BusObRecID] = None
    cacheKey: Optional[str] = None
    cacheScope: Optional[CacheScope] = None
    fields: Optional[List[FieldTemplateItem]] = None
    persist: Optional[bool] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class RelatedSaveResponse(ApiBaseModel):
    parentBusObId: Optional[ct.BusObID] = None
    parentBusObPublicId: Optional[str] = None
    parentBusObRecId: Optional[ct.BusObRecID] = None
    relationshipId: Optional[ct.RelationshipID] = None
    busObPublicId: Optional[str] = None
    busObRecId: Optional[ct.BusObRecID] = None
    cacheKey: Optional[str] = None
    fieldValidationErrors: Optional[List[FieldValidationError]] = None
    notificationTriggers: Optional[List[NotificationTrigger]] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class SaveResponse(ApiBaseModel):
    busObPublicId: Optional[str] = None
    busObRecId: Optional[ct.BusObRecID] = None
    cacheKey: Optional[str] = None
    fieldValidationErrors: Optional[List[FieldValidationError]] = None
    notificationTriggers: Optional[List[NotificationTrigger]] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class BatchDeleteRequest(ApiBaseModel):
    deleteRequests: Optional[List[DeleteRequest]] = None
    stopOnError: Optional[bool] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class BatchDeleteResponse(ApiBaseModel):
    responses: Optional[List[DeleteResponse]] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class ReadResponse(ApiBaseModel):
    busObId: Optional[ct.BusObID] = None
    busObPublicId: Optional[str] = None
    busObRecId: Optional[ct.BusObRecID] = None
    fields: Optional[List[FieldTemplateItem]] = None
    links: Optional[List[Core.CherwellLink]] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class AttachmentsResponse(ApiBaseModel):
    attachments: Optional[List[Attachment]] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class BatchReadRequest(ApiBaseModel):
    readRequests: Optional[List[ReadRequest]] = None
    stopOnError: Optional[bool] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class BatchReadResponse(ApiBaseModel):
    responses: Optional[List[ReadResponse]] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class SchemaResponse(ApiBaseModel):
    busObId: Optional[ct.BusObID] = None
    fieldDefinitions: Optional[List[FieldDefinition]] = None
    firstRecIdField: Optional[str] = None
    gridDefinitions: Optional[List[GridDefinition]] = None
    name: Optional[str] = None
    recIdFields: Optional[str] = None
    relationships: Optional[List[Relationship]] = None
    stateFieldId: Optional[ct.FieldID] = None
    states: Optional[str] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class BusObsForViewResponse(ApiBaseModel):
    summaries: Optional[List[ViewSummary]] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class BatchSaveRequest(ApiBaseModel):
    saveRequests: Optional[List[SaveRequest]] = None
    stopOnError: Optional[bool] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class BatchSaveResponse(ApiBaseModel):
    responses: Optional[List[SaveResponse]] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


Summary.model_rebuild()
ViewSummary.model_rebuild()
