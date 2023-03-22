
from typing import ClassVar, Literal, Optional

from cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject import (
    ReadResponse,
    SchemaResponse,
    Summary,
)
from cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core import ServiceInfoResponse
from cherwell_pydantic_api.api import Connection
from cherwell_pydantic_api.bo.registry import BusinessObjectRegistry
from cherwell_pydantic_api.interfaces import ApiRequesterInterface
from cherwell_pydantic_api.settings import InstanceSettingsBase, Settings
from cherwell_pydantic_api.types import BusObID, BusObRecID



class Instance(ApiRequesterInterface):
    _instances: ClassVar[dict[str, "Instance"]] = {}

    def __init__(self, instance_settings: InstanceSettingsBase):
        """Internal use only. Use Instance.use() instead."""
        # Take into account that the settings might change under our nose
        self._settings = instance_settings.copy()
        self.bo = BusinessObjectRegistry(self)
        self._connection = Connection(instance_settings)


    @property
    def settings(self) -> InstanceSettingsBase:
        return self._settings


    async def authenticate(self):
        return await self._connection.authenticate()


    async def get_busobid(self, busobname: str) -> Optional[BusObID]:
        return await self._connection.get_busobid(busobname)


    async def get_bo_schema(self, *, busobid: Optional[BusObID] = None, busobname: Optional[str] = None) -> Optional[SchemaResponse]:
        if busobid is None:
            if busobname is None:
                raise TypeError(
                    'get_bo_schema() missing 1 required argument: busobid or busobname')
            busobid = await self.get_busobid(busobname)
            if busobid is None:
                return None
        response = await self._connection.GetBusinessObjectSchemaV1(busobId=busobid, includerelationships=True)
        if not response.hasError:
            self.bo.register(response)
        return response


    async def get_bo_summaries(self, type: Literal["All", "Major", "Supporting", "Lookup", "Groups"] = "Major") -> list[Summary]:
        response = await self._connection.get_bo_summaries(type)
        for summary in response:
            self.bo.register_summary(summary)
        return response


    async def get_bo(self, busobid: BusObID, *, busobrecid: Optional[BusObRecID] = None, publicid: Optional[str] = None) -> ReadResponse:
        if busobrecid is None:
            if publicid is None:
                raise TypeError(
                    'get_bo() missing 1 required argument: busobrecid or publicid')
            return await self._connection.GetBusinessObjectByPublicIdV1(busobid=busobid, publicid=publicid)
        return await self._connection.GetBusinessObjectByRecIdV1(busobid=busobid, busobrecid=busobrecid)


    async def get_service_info(self) -> ServiceInfoResponse:
        response = await self._connection.GetServiceInfoV1()
        self.bo.register_service_info(response)
        return response
    

    @classmethod
    def use(cls, name: Optional[str] = None, *, instance_settings: Optional[InstanceSettingsBase] = None) -> "Instance":
        """Instantiate an Instance object for the given instance name, or return an existing Instance object if one already exists."""
        settings = Settings()
        if instance_settings is None:
            instance_settings = settings.get_instance(name)
        if instance_settings is None:
            raise ValueError(f"Instance {name} not found in settings")
        name = instance_settings.name
        if name not in cls._instances:
            cls._instances[name] = cls(instance_settings)
        return cls._instances[name]