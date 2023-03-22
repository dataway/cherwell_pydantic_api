# generated by datamodel-codegen:
#   filename:  csm_api-swagger.json

from __future__ import annotations

from enum import Enum
from typing import List, Optional

import cherwell_pydantic_api.types as ct
from cherwell_pydantic_api.generated_api_utils import ApiBaseModel, HttpStatusCode

from .... import CherwellObjectID
from . import BusinessObject, Core


class SectionField(ApiBaseModel):
    attributes: Optional[List[CherwellObjectID]] = None
    fieldId: Optional[ct.FieldID] = None
    fieldType: Optional[str] = None
    label: Optional[str] = None
    multiline: Optional[bool] = None
    value: Optional[str] = None


import cherwell_pydantic_api.types as ct


class Section(ApiBaseModel):
    sectionFields: Optional[List[SectionField]] = None
    galleryImage: Optional[str] = None
    title: Optional[str] = None
    relationshipId: Optional[ct.RelationshipID] = None
    targetBusObId: Optional[ct.BusObID] = None
    targetBusObRecId: Optional[ct.BusObRecID] = None


import cherwell_pydantic_api.types as ct


class MobileFormResponse(ApiBaseModel):
    actions: Optional[List[Core.Action]] = None
    attachments: Optional[List[BusinessObject.Attachment]] = None
    galleryImage: Optional[str] = None
    locationInformation: Optional[Core.Location] = None
    sections: Optional[List[Section]] = None
    title: Optional[str] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None