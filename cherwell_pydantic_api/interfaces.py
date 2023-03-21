from typing import TYPE_CHECKING, Optional



# This interface doesn't actually do anything, but is used for type checking.

if TYPE_CHECKING:
    from cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject import (
        ReadResponse,
        SchemaResponse,
    )
    from cherwell_pydantic_api.settings import InstanceSettingsBase
    from cherwell_pydantic_api.types import BusObID, BusObRecID

    class ApiRequesterInterface:
        async def get_busobid(self, busobname: str) -> Optional[BusObID]:
            ...

        async def get_bo_schema(self, *, busobid: Optional[BusObID] = None, busobname: Optional[str] = None) -> Optional[SchemaResponse]:
            ...

        async def get_bo(self, busobid: BusObID, *, busobrecid: Optional[BusObRecID] = None, publicid: Optional[str] = None) -> ReadResponse:
            ...

        @property
        def settings(self) -> InstanceSettingsBase:
            ...

else:
    class ApiRequesterInterface:
        pass
