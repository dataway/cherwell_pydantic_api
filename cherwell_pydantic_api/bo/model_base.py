from typing import Any, ClassVar, Literal, Optional, Type, TypeVar, Union, cast

from pydantic import BaseModel, PrivateAttr
from pydantic_changedetect.changedetect import ChangeDetectionMixin

from cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject import (
    FieldTemplateItem,
    ReadResponse,
    SaveRequest,
)
from cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core import CherwellLink
from cherwell_pydantic_api.bo.registry import BusinessObjectModelRegistryMixin
from cherwell_pydantic_api.instance import Instance
from cherwell_pydantic_api.types import (
    BusObID,
    BusObRecID,
    CherwellAPIError,
    FieldID,
    RelationshipID,
    SaveBusinessObjectError,
)



BusObModel_T = TypeVar("BusObModel_T", bound="BusinessObjectModelBase")


class BusinessObjectApiData(BaseModel):
    "Holds all the per-record data needed between API calls"
    source: Literal['new', 'save', 'load'] = 'new'
    busObRecId: Optional[BusObRecID] = None
    busObPublicId: Optional[str] = None
    fields: list[FieldTemplateItem] = []
    links: list[CherwellLink] = []
    cacheKey: Optional[str] = None


class BusinessObjectRelationship(BaseModel):
    target: BusObID
    oneToMany: bool
    description: str
    displayName: str

    def __init__(self, target: Union[str, BusObID], oneToMany: bool, description: str, displayName: str):
        super().__init__(target=BusObID(target), oneToMany=oneToMany, description=description, displayName=displayName)


class BusinessObjectModelBase(ChangeDetectionMixin, BaseModel, BusinessObjectModelRegistryMixin):
    _instance_name: ClassVar[str]
    _api_data: BusinessObjectApiData = PrivateAttr(
        default_factory=BusinessObjectApiData)

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
        statefield: Optional[str]
        firstrecfield: Optional[str]
        states: Optional[list[str]]
        relationships: Optional[dict[RelationshipID, BusinessObjectRelationship]]


    @classmethod
    def get_instance(cls) -> Instance:
        """Get the instance object that this model is associated with."""
        return Instance.use(cls._instance_name)


    @classmethod
    def from_api_response(cls: Type[BusObModel_T], response: ReadResponse) -> BusObModel_T:
        assert response.fields is not None
        assert response.busObId == cls._ModelData.busobid
        assert all([f.name is not None for f in response.fields])
        api_data = BusinessObjectApiData(source='load', busObRecId=response.busObRecId,
                                         busObPublicId=response.busObPublicId, fields=response.fields, links=response.links or [])
        vals: dict[str, Any] = {
            cast(str, f.name): f.value for f in response.fields}
        return cls(_api_data=api_data, **vals)


    @classmethod
    async def from_api(cls: Type[BusObModel_T], publicid: Optional[str] = None, *, busobrecid: Optional[BusObRecID] = None) -> Optional[BusObModel_T]:
        "Get a Business Object from the Cherwell API."
        response = await cls.get_instance().get_bo(busobid=cls._ModelData.busobid, publicid=publicid, busobrecid=busobrecid)
        if response is None:
            raise ValueError("No response from Cherwell API")
        if response.hasError:
            raise CherwellAPIError(f"from_api[{cls.__name__}]", errorMessage=response.errorMessage,
                                   errorCode=response.errorCode, httpStatusCode=response.httpStatusCode)
        return cls.from_api_response(response)
    get = from_api


    def _prepare_changes_for_save(self) -> list[FieldTemplateItem]:
        if not self._api_data.fields:
            r: list[FieldTemplateItem] = []
            for fname, field in self.__fields__.items():
                v = getattr(self, fname)
                if v:
                    r.append(FieldTemplateItem(
                        dirty=True, value=v,
                        fieldId=field.field_info.extra['cw_fi']
                    ))
            return r

        for fld in self._api_data.fields:
            if fld.name in self.__self_changed_fields__:
                fld.value = getattr(self, fld.name)
                fld.dirty = True
        return self._api_data.fields


    async def save(self, persist: bool = True) -> BusObRecID:
        """Save the Business Object to the Cherwell API. Returns the BusObRecID.
        Only fields that have changed will be saved.

        If a new business object is saved (i.e. it has not been loaded from the API), the BusObRecID and busObPublicId will be set on the model.
        However further fields will not be loaded from the API. It is recommended to call the `update` method after saving a new business object.
        """
        save_req = SaveRequest(busObId=self._ModelData.busobid, busObPublicId=self._api_data.busObPublicId,
                               busObRecId=self._api_data.busObRecId, cacheKey=self._api_data.cacheKey, fields=self._prepare_changes_for_save(), persist=persist)
        response = await self.get_instance().connection.SaveBusinessObjectV1(save_req)
        if self._api_data.source == 'new':
            if response.busObRecId is not None:
                self._api_data.source = 'save'
                self._api_data.busObRecId = response.busObRecId
                setattr(self, self._ModelData.firstrecfield, # type: ignore
                        response.busObRecId)
                self._api_data.busObPublicId = response.busObPublicId
                self._api_data.cacheKey = response.cacheKey
        if response.hasError:
            raise SaveBusinessObjectError(errorCode=response.errorCode, errorMessage=response.errorMessage,
                                          httpStatusCode=response.httpStatusCode, SaveResponse=response)
        assert response.busObRecId is not None
        self._api_data.cacheKey = response.cacheKey
        self.reset_changed()
        return response.busObRecId


    async def update(self):
        "Get a Business Object from the Cherwell API and update the existing model with the current values. Any changes made to the model will be discarded."
        response = await self.get_instance().get_bo(busobid=self._ModelData.busobid, busobrecid=self._api_data.busObRecId)
        if response is None:
            raise ValueError("No response from Cherwell API")
        if response.hasError:
            raise CherwellAPIError(f"update[{type(self).__name__}]", errorMessage=response.errorMessage,
                                   errorCode=response.errorCode, httpStatusCode=response.httpStatusCode)
        assert response.fields is not None
        assert response.busObId == self._ModelData.busobid
        assert response.busObRecId == self._api_data.busObRecId
        assert all([f.name is not None for f in response.fields])
        self._api_data.source = 'load'
        self._api_data.busObPublicId = response.busObPublicId
        self._api_data.fields = response.fields
        self._api_data.links = response.links or []
        self._api_data.cacheKey = None
        for f in response.fields:
            setattr(self, f.name, f.value)
        self.reset_changed()
        return self
