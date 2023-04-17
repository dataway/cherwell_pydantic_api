from typing import ClassVar, Optional, Type, TypeVar, cast

from pydantic import BaseModel
from pydantic_changedetect.changedetect import ChangeDetectionMixin

from cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject import ReadResponse
from cherwell_pydantic_api.bo.registry import BusinessObjectModelRegistryMixin
from cherwell_pydantic_api.instance import Instance
from cherwell_pydantic_api.types import BusObID, BusObRecID, CherwellAPIError, FieldID



BusObModel_T = TypeVar("BusObModel_T", bound="BusinessObjectModelBase")


class BusinessObjectModelBase(ChangeDetectionMixin, BaseModel, BusinessObjectModelRegistryMixin):
    _instance_name: ClassVar[str]

    def __init_subclass__(cls) -> None:
        # Check that _ModelData and _ModelData.busobid exist - this is not the case for intermediate classes
        if hasattr(cls, "_ModelData") and hasattr(cls._ModelData, "busobid"):
            # Register model classes in the instance's business object registry.
            cls.get_instance().bo.register_model(cls._ModelData.busobid, cls)
        return super().__init_subclass__()


    class _ModelData:
        busobid: BusObID
        statefieldid: Optional[FieldID]
        firstrecidfield: Optional[FieldID]
        recidfields: Optional[FieldID]


    @classmethod
    def get_instance(cls) -> Instance:
        """Get the instance object that this model is associated with."""
        return Instance.use(cls._instance_name)


    @classmethod
    def from_api_response(cls: Type[BusObModel_T], response: ReadResponse) -> BusObModel_T:
        assert response.fields is not None
        assert response.busObId == cls._ModelData.busobid
        assert all([f.name is not None for f in response.fields])
        vals = {cast(str, f.name): f.value for f in response.fields}
        return cls(**vals)


    @classmethod
    async def from_api(cls: Type[BusObModel_T], publicid: Optional[str] = None, *, busobrecid: Optional[BusObRecID] = None) -> Optional[BusObModel_T]:
        response = await cls.get_instance().get_bo(busobid=cls._ModelData.busobid, publicid=publicid, busobrecid=busobrecid)
        if response is None:
            raise ValueError("No response from Cherwell API")
        if response.hasError:
            raise CherwellAPIError(f"get_bo[{cls.__name__}]", errorMessage=response.errorMessage,
                                   errorCode=response.errorCode, httpStatusCode=response.httpStatusCode)
        return cls.from_api_response(response)
