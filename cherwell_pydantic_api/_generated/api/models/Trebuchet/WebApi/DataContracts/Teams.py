# Generated by codegen.py
# pyright: reportUnusedImport=false, reportMissingTypeArgument=false

from __future__ import annotations

from enum import Enum
from typing import List, Optional

import cherwell_pydantic_api.types as ct
from cherwell_pydantic_api.generated_api_utils import ApiBaseModel

from . import BusinessObject


class AddUserToTeamRequest(ApiBaseModel):
    teamId: Optional[str] = None
    userIsTeamManager: Optional[bool] = None
    userRecordId: Optional[str] = None


from enum import Enum

import cherwell_pydantic_api.types as ct
from cherwell_pydantic_api.generated_api_utils import HttpStatusCode


class AddUserToTeamResponse(ApiBaseModel):
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class Team(ApiBaseModel):
    teamId: Optional[str] = None
    teamName: Optional[str] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class TeamsV2Response(ApiBaseModel):
    teams: Optional[List[Team]] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


class TeamType(Enum):
    User = 'User'
    CustomerWorkgroup = 'CustomerWorkgroup'


from enum import Enum

import cherwell_pydantic_api.types as ct


class TeamResponse(ApiBaseModel):
    description: Optional[str] = None
    emailAlias: Optional[str] = None
    fields: Optional[List[BusinessObject.FieldTemplateItem]] = None
    image: Optional[str] = None
    name: Optional[str] = None
    teamId: Optional[str] = None
    teamType: Optional[TeamType] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class RemoveUserFromTeamResponse(ApiBaseModel):
    teamId: Optional[str] = None
    userRecordId: Optional[str] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class RemoveCustomerFromWorkgroupResponse(ApiBaseModel):
    workgroupId: Optional[str] = None
    customerRecordId: Optional[str] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class TeamSaveRequest(ApiBaseModel):
    description: Optional[str] = None
    emailAlias: Optional[str] = None
    image: Optional[str] = None
    teamId: Optional[str] = None
    teamName: Optional[str] = None
    teamType: Optional[TeamType] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class TeamSaveResponse(ApiBaseModel):
    teamId: Optional[str] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class SaveTeamMemberRequest(ApiBaseModel):
    isTeamManager: Optional[bool] = None
    setAsDefaultTeam: Optional[bool] = None
    teamId: Optional[str] = None
    userRecId: Optional[str] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class SaveTeamMemberResponse(ApiBaseModel):
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class SaveWorkgroupMemberRequest(ApiBaseModel):
    customerRecordId: Optional[str] = None
    workgroupId: Optional[str] = None
    customerIsWorkgroupManager: Optional[bool] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class SaveWorkgroupMemberResponse(ApiBaseModel):
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class AddUserToTeamByBatchRequest(ApiBaseModel):
    addUserToTeamRequests: Optional[List[AddUserToTeamRequest]] = None
    stopOnError: Optional[bool] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class AddUserToTeamByBatchResponse(ApiBaseModel):
    responses: Optional[List[AddUserToTeamResponse]] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


from enum import Enum

import cherwell_pydantic_api.types as ct


class TeamsResponse(ApiBaseModel):
    error: Optional[str] = None
    errorCode: Optional[str] = None
    hasError: Optional[bool] = None
    teams: Optional[List[Team]] = None
