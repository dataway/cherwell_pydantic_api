# generated by datamodel-codegen:
#   filename:  csm_api-swagger.json

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List, Optional

import cherwell_pydantic_api.types as ct
from cherwell_pydantic_api.generated_api_utils import ApiBaseModel

from . import BusinessObject


ct  # type: ignore
from enum import Enum


Enum  # type: ignore


class User(ApiBaseModel):
    accountLocked: Optional[bool] = None
    createDateTime: Optional[datetime] = None
    displayName: Optional[str] = None
    error: Optional[str] = None
    errorCode: Optional[str] = None
    fields: Optional[List[BusinessObject.FieldTemplateItem]] = None
    hasError: Optional[bool] = None
    lastPasswordResetDate: Optional[datetime] = None
    lastResetDateTime: Optional[datetime] = None
    ldapRequired: Optional[bool] = None
    passwordNeverExpires: Optional[bool] = None
    publicId: Optional[str] = None
    recordId: Optional[str] = None
    securityGroupId: Optional[str] = None
    shortDisplayName: Optional[str] = None
    userCannotChangePassword: Optional[bool] = None
    userMustResetPasswordAtNextLogin: Optional[bool] = None


import cherwell_pydantic_api.types as ct
from cherwell_pydantic_api.generated_api_utils import HttpStatusCode


ct  # type: ignore
from enum import Enum


Enum  # type: ignore


class UserV2(ApiBaseModel):
    accountLocked: Optional[bool] = None
    createDateTime: Optional[datetime] = None
    displayName: Optional[str] = None
    fields: Optional[List[BusinessObject.FieldTemplateItem]] = None
    lastPasswordResetDate: Optional[datetime] = None
    lastResetDateTime: Optional[datetime] = None
    ldapRequired: Optional[bool] = None
    passwordNeverExpires: Optional[bool] = None
    publicId: Optional[str] = None
    recordId: Optional[str] = None
    securityGroupId: Optional[str] = None
    shortDisplayName: Optional[str] = None
    userCannotChangePassword: Optional[bool] = None
    userMustResetPasswordAtNextLogin: Optional[bool] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


import cherwell_pydantic_api.types as ct


ct  # type: ignore
from enum import Enum


Enum  # type: ignore


class UserBatchDeleteRequest(ApiBaseModel):
    stopOnError: Optional[bool] = None
    userRecordIds: Optional[List[str]] = None


import cherwell_pydantic_api.types as ct


ct  # type: ignore
from enum import Enum


Enum  # type: ignore


class UserDeleteResponse(ApiBaseModel):
    error: Optional[str] = None
    errorCode: Optional[str] = None
    hasError: Optional[bool] = None
    users: Optional[List[User]] = None


import cherwell_pydantic_api.types as ct


ct  # type: ignore
from enum import Enum


Enum  # type: ignore


class UserDeleteV2Response(ApiBaseModel):
    userRecordId: Optional[str] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


import cherwell_pydantic_api.types as ct


ct  # type: ignore
from enum import Enum


Enum  # type: ignore


class UserListResponse(ApiBaseModel):
    users: Optional[List[UserV2]] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


import cherwell_pydantic_api.types as ct


ct  # type: ignore
from enum import Enum


Enum  # type: ignore


class UserReadRequest(ApiBaseModel):
    loginId: Optional[str] = None
    publicId: Optional[str] = None


import cherwell_pydantic_api.types as ct


ct  # type: ignore
from enum import Enum


Enum  # type: ignore


class UserReadResponse(ApiBaseModel):
    error: Optional[str] = None
    errorCode: Optional[str] = None
    hasError: Optional[bool] = None
    users: Optional[List[User]] = None


import cherwell_pydantic_api.types as ct


ct  # type: ignore
from enum import Enum


Enum  # type: ignore


class UserSaveRequest(ApiBaseModel):
    accountLocked: Optional[bool] = None
    busObId: Optional[ct.BusObID] = None
    busObPublicId: Optional[str] = None
    busObRecId: Optional[ct.BusObRecID] = None
    displayName: Optional[str] = None
    error: Optional[str] = None
    errorCode: Optional[str] = None
    hasError: Optional[bool] = None
    ldapRequired: Optional[bool] = None
    loginId: Optional[str] = None
    nextPasswordResetDate: Optional[datetime] = None
    password: Optional[str] = None
    passwordNeverExpires: Optional[bool] = None
    securityGroupId: Optional[str] = None
    userCannotChangePassword: Optional[bool] = None
    userInfoFields: Optional[List[BusinessObject.FieldTemplateItem]] = None
    userMustChangePasswordAtNextLogin: Optional[bool] = None
    windowsUserId: Optional[str] = None


import cherwell_pydantic_api.types as ct


ct  # type: ignore
from enum import Enum


Enum  # type: ignore


class UserSaveResponse(ApiBaseModel):
    busObPublicId: Optional[str] = None
    busObRecId: Optional[ct.BusObRecID] = None
    error: Optional[str] = None
    errorCode: Optional[str] = None
    hasError: Optional[bool] = None


import cherwell_pydantic_api.types as ct


ct  # type: ignore
from enum import Enum


Enum  # type: ignore


class UserSaveV2Request(ApiBaseModel):
    accountLocked: Optional[bool] = None
    allCultures: Optional[bool] = None
    busObId: Optional[ct.BusObID] = None
    busObPublicId: Optional[str] = None
    busObRecId: Optional[ct.BusObRecID] = None
    displayName: Optional[str] = None
    ldapRequired: Optional[bool] = None
    loginId: Optional[str] = None
    nextPasswordResetDate: Optional[datetime] = None
    password: Optional[str] = None
    passwordNeverExpires: Optional[bool] = None
    securityGroupId: Optional[str] = None
    specificCulture: Optional[str] = None
    userCannotChangePassword: Optional[bool] = None
    userInfoFields: Optional[List[BusinessObject.FieldTemplateItem]] = None
    userMustChangePasswordAtNextLogin: Optional[bool] = None
    windowsUserId: Optional[str] = None


import cherwell_pydantic_api.types as ct


ct  # type: ignore
from enum import Enum


Enum  # type: ignore


class UserSaveV2Response(ApiBaseModel):
    busObPublicId: Optional[str] = None
    busObRecId: Optional[ct.BusObRecID] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


import cherwell_pydantic_api.types as ct


ct  # type: ignore
from enum import Enum


Enum  # type: ignore


class UserReadV2Response(ApiBaseModel):
    users: Optional[List[UserV2]] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


import cherwell_pydantic_api.types as ct


ct  # type: ignore
from enum import Enum


Enum  # type: ignore


class UserBatchDeleteResponse(ApiBaseModel):
    responses: Optional[List[UserDeleteResponse]] = None


import cherwell_pydantic_api.types as ct


ct  # type: ignore
from enum import Enum


Enum  # type: ignore


class UserBatchDeleteV2Response(ApiBaseModel):
    responses: Optional[List[UserDeleteV2Response]] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


import cherwell_pydantic_api.types as ct


ct  # type: ignore
from enum import Enum


Enum  # type: ignore


class UserBatchReadRequest(ApiBaseModel):
    readRequests: Optional[List[UserReadRequest]] = None
    stopOnError: Optional[bool] = None


import cherwell_pydantic_api.types as ct


ct  # type: ignore
from enum import Enum


Enum  # type: ignore


class UserBatchReadResponse(ApiBaseModel):
    responses: Optional[List[UserReadV2Response]] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


import cherwell_pydantic_api.types as ct


ct  # type: ignore
from enum import Enum


Enum  # type: ignore


class UserBatchSaveRequest(ApiBaseModel):
    saveRequests: Optional[List[UserSaveRequest]] = None
    stopOnError: Optional[bool] = None


import cherwell_pydantic_api.types as ct


ct  # type: ignore
from enum import Enum


Enum  # type: ignore


class UserBatchSaveResponse(ApiBaseModel):
    responses: Optional[List[UserSaveResponse]] = None


import cherwell_pydantic_api.types as ct


ct  # type: ignore
from enum import Enum


Enum  # type: ignore


class UserBatchSaveV2Request(ApiBaseModel):
    saveRequests: Optional[List[UserSaveV2Request]] = None
    stopOnError: Optional[bool] = None


import cherwell_pydantic_api.types as ct


ct  # type: ignore
from enum import Enum


Enum  # type: ignore


class UserBatchSaveV2Response(ApiBaseModel):
    responses: Optional[List[UserSaveV2Response]] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None
