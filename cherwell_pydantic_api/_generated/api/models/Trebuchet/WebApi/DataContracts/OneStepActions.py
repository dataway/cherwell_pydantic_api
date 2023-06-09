# generated by datamodel-codegen:
#   filename:  csm_api-swagger.json

from __future__ import annotations

from enum import Enum
from typing import List, Optional

import cherwell_pydantic_api.types as ct
from cherwell_pydantic_api.generated_api_utils import ApiBaseModel, HttpStatusCode

from . import Core


ct  # type: ignore
from enum import Enum


Enum  # type: ignore


class OneStepActionResponse(ApiBaseModel):
    completed: Optional[bool] = None
    currentPrimaryBusObId: Optional[ct.BusObID] = None
    currentPrimaryBusObRecId: Optional[ct.BusObRecID] = None
    hasNewAccessToken: Optional[bool] = None
    newAccessToken: Optional[str] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    hasError: Optional[bool] = None
    httpStatusCode: Optional[HttpStatusCode] = None


import cherwell_pydantic_api.types as ct


ct  # type: ignore
from enum import Enum


Enum  # type: ignore


class OneStepActionRequest(ApiBaseModel):
    acquireLicense: Optional[bool] = None
    busObId: Optional[ct.BusObID] = None
    busObRecId: Optional[ct.BusObRecID] = None
    oneStepActionStandInKey: Optional[str] = None
    promptValues: Optional[List[Core.SimplePromptValue]] = None
