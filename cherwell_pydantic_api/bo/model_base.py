import datetime
from decimal import Decimal
from typing import Any, ClassVar, Literal, Optional, Type, TypeVar, Union, cast

from pydantic import BaseModel, PrivateAttr, ValidationError
from pydantic_changedetect.changedetect import ChangeDetectionMixin

from cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject import (
    FieldTemplateItem,
    ReadResponse,
    SaveRequest,
)
from cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core import CherwellLink
from cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Searches import (
    FilterInfo,
    SearchResultsRequest,
)
from cherwell_pydantic_api.bo.registry import BusinessObjectModelRegistryMixin
from cherwell_pydantic_api.instance import Instance
from cherwell_pydantic_api.types import (
    BusObID,
    BusObRecID,
    CherwellAPIError,
    FieldID,
    FieldIdentifier,
    RelationshipID,
    SaveBusinessObjectError,
    ShortFieldID,
)



BusObModel_T = TypeVar("BusObModel_T", bound="BusinessObjectModelBase")
SearchOp = tuple[Literal["eq", "gt", "lt", "contains", "startswith"],
                 Union[str, int, Decimal, datetime.datetime, datetime.date, datetime.time]]
SearchParam = Union[SearchOp, str, int, Decimal, datetime.datetime, datetime.date, datetime.time]
BusinessObjectApiDataSource = Literal['new', 'save', 'load', 'search']


class BusinessObjectApiData(BaseModel):
    "Holds all the per-record data needed between API calls"
    source: BusinessObjectApiDataSource = 'new'
    busObRecId: Optional[BusObRecID] = None
    busObPublicId: Optional[str] = None
    fields: list[FieldTemplateItem] = []
    links: list[CherwellLink] = []
    cacheKey: Optional[str] = None


class BusinessObjectRelationship(BaseModel):
    target_busobid: BusObID
    target_class_name: Optional[str] = None
    oneToMany: bool
    description: str
    displayName: str
    target: Optional[Type["BusinessObjectModelBase"]] = None

    def __init__(self, target_busobid: Union[str, BusObID], oneToMany: bool, description: str, displayName: str, target_class_name: Optional[str] = None):
        super().__init__(target_busobid=BusObID(target_busobid), target_class_name=target_class_name,
                         oneToMany=oneToMany, description=description, displayName=displayName)


# TODO: pyright complaints about ChangeDetectionMixin._copy_and_set_values; check
# pyright: reportIncompatibleMethodOverride=false
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
        statefieldid: Optional[ShortFieldID] = None
        firstrecidfield: Optional[ShortFieldID] = None
        recidfields: Optional[ShortFieldID] = None
        statefield: Optional[str] = None
        firstrecfield: Optional[str] = None
        states: Optional[list[str]] = None
        relationships: Optional[dict[RelationshipID, BusinessObjectRelationship]] = None


    @classmethod
    def get_instance(cls) -> Instance:
        """Get the instance object that this model is associated with."""
        return Instance.use(cls._instance_name)


    @classmethod
    def from_api_response(cls: Type[BusObModel_T], response: ReadResponse, source: BusinessObjectApiDataSource) -> BusObModel_T:
        assert response.fields is not None
        assert response.busObId == cls.get_busobid()
        assert all([f.name is not None for f in response.fields])
        api_data = BusinessObjectApiData(source=source, busObRecId=response.busObRecId,
                                         busObPublicId=response.busObPublicId, fields=response.fields, links=response.links or [])
        vals: dict[str, Any] = {
            FieldIdentifier(cast(str, f.name)): f.value for f in response.fields}
        try:
            ob = cls(**vals)
        except ValidationError as e:
            if source != 'search':
                raise
            # Mitigate the Cherwell API returning invalid data for searches: delete bad fields and try again
            for error in e.errors():
                if len(error['loc']) != 1 or error['loc'][0] not in vals:
                    raise
                del vals[error['loc'][0]]  # type: ignore
            ob = cls(**vals)
        ob._api_data = api_data
        return ob


    @classmethod
    async def from_api(cls: Type[BusObModel_T], publicid: Optional[str] = None, *, busobrecid: Optional[BusObRecID] = None) -> Optional[BusObModel_T]:
        "Get a Business Object from the Cherwell API."
        response = await cls.get_instance().get_bo(busobid=cls.get_busobid(), publicid=publicid, busobrecid=busobrecid)
        if response.hasError:
            raise CherwellAPIError(f"from_api[{cls.__name__}]", errorMessage=response.errorMessage,
                                   errorCode=response.errorCode, httpStatusCode=response.httpStatusCode)
        return cls.from_api_response(response, 'load')
    get = from_api # type: ignore[pydantic-field]


    @classmethod
    def get_busobid(cls) -> BusObID:
        return cls._ModelData.busobid


    @classmethod
    def get_fieldid(cls, fieldname: str) -> FieldID:
        field = cls.model_fields[fieldname]
        if not isinstance(field.json_schema_extra, dict) or 'cw_fi' not in field.json_schema_extra:
            raise ValueError(f"Field {fieldname} has no cw_fi, is it a pydantic_cherwell_api model?")
        return field.json_schema_extra['cw_fi']


    def get_busobrecid(self) -> BusObRecID:
        """Get the BusObRecID of the Business Object. Raises ValueError if BusObRecID is not set."""
        if self._api_data.busObRecId is None:
            raise ValueError("BusObRecID is not set")
        return self._api_data.busObRecId


    def _prepare_changes_for_save(self) -> list[FieldTemplateItem]:
        if not self._api_data.fields:
            r: list[FieldTemplateItem] = []
            for fname in self.model_fields.keys():
                v = getattr(self, fname)
                if v:
                    r.append(FieldTemplateItem(dirty=True, value=str(v), fieldId=self.get_fieldid(fname)))
            return r

        for fld in self._api_data.fields:
            if fld.name in self.model_self_changed_fields:
                fld.value = str(getattr(self, fld.name))
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
                setattr(self, self._ModelData.firstrecfield, response.busObRecId)  # type: ignore
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
        # HACK: Enable validate_assignment for the duration of the update
        save_validate_assignment = self.model_config.get('validate_assignment', False)
        self.model_config['validate_assignment'] = True
        for f in response.fields:
            assert f.name
            setattr(self, FieldIdentifier(f.name), f.value)
        self.reset_changed()
        self.model_config['validate_assignment'] = save_validate_assignment
        return self


    @classmethod
    def _get_relationships(cls) -> dict[RelationshipID, BusinessObjectRelationship]:
        if not hasattr(cls, '_ModelData') or not hasattr(cls._ModelData, 'relationships') or not cls._ModelData.relationships:
            raise KeyError(f"Business object {cls.__name__} (busobid={cls._ModelData.busobid}) has no relationships")
        return cls._ModelData.relationships

    @classmethod
    def get_relationship(cls, relationship_id: str) -> BusinessObjectRelationship:
        "Get the relationship definition for the specified relationship ID. Raises KeyError if not found."
        relationship_id = RelationshipID(relationship_id)
        rel = cls._get_relationships()[relationship_id]
        if rel.target is None:
            try:
                rel.target = cls.get_instance().bo.get_model(rel.target_busobid)  # type: ignore
            except KeyError:
                pass
        return rel

    @classmethod
    def relationships_to(cls, *,
                         target_busobid: Optional[str] = None,
                         target: Union[Type["BusinessObjectModelBase"], "BusinessObjectModelBase", None] = None
                         ) -> dict[RelationshipID, BusinessObjectRelationship]:
        "Find relationships linking to the specified target model."
        if target_busobid is None:
            if target is None:
                raise ValueError("Must specify either target or target_busobid")
            target_busobid = target._ModelData.busobid
        else:
            target_busobid = BusObID(target_busobid)
        rels = cls._get_relationships()
        r = {relid: cls.get_relationship(relid)
             for relid, rel in rels.items()
             if rel.target_busobid == target_busobid}
        return r

    @classmethod
    def resolve_relationship(cls, *,
                             target_busobid: Optional[str] = None,
                             target: Union[Type["BusinessObjectModelBase"], "BusinessObjectModelBase", None] = None,
                             keyword: Optional[str] = None) -> RelationshipID:
        """Find the relationship linking to the specified target model.
        If multiple relationships are found, the keyword parameter can be used to resolve the relationship by searching the displayName field (case-insensitive)."""
        rels = cls.relationships_to(target_busobid=target_busobid, target=target)
        if len(rels) == 0:
            raise ValueError(f"No relationships found from {cls.__name__} to {target_busobid=} {target=}")
        if keyword is None:
            if len(rels) == 1:
                return next(iter(rels.keys()))
            raise ValueError(
                f"Multiple relationships found from {cls.__name__} to {target_busobid=} {target=}. Specify a keyword to resolve the relationship.")
        keyword = keyword.lower()
        matching_rels = {relid: rel for relid, rel in rels.items() if keyword in rel.displayName.lower()}
        if len(matching_rels) == 0:
            raise ValueError(
                f"No relationships found from {cls.__name__} to {target_busobid=} {target=} with keyword '{keyword}'.")
        if len(matching_rels) > 1:
            raise ValueError(
                f"Multiple relationships found from {cls.__name__} to {target_busobid=} {target=} with keyword '{keyword}'. Specify a more specific keyword to resolve the relationship.")
        return next(iter(matching_rels.keys()))


    async def link_related(self, target: "BusinessObjectModelBase", relationship_id: Optional[RelationshipID] = None,
                           *, keyword: Optional[str] = None):
        if relationship_id is None:
            relationship_id = self.resolve_relationship(target=target, keyword=keyword)
        response = await self.get_instance().connection.LinkRelatedBusinessObjectByRecIdV2(
            parentbusobid=self.get_busobid(),
            parentbusobrecid=self.get_busobrecid(),
            relationshipid=relationship_id,
            busobid=target.get_busobid(),
            busobrecid=target.get_busobrecid())
        if response.hasError:
            raise CherwellAPIError(f"link_related[{type(self).__name__}]", errorMessage=response.errorMessage,
                                   errorCode=response.errorCode, httpStatusCode=response.httpStatusCode)
        return response


    async def attach_file(self, filename: str, filedata: bytes, description: Optional[str] = None):
        response = await self.get_instance().connection.UploadBusinessObjectAttachmentByIdAndRecIdV1(
            body=filedata,
            filename=filename,
            busobid=self.get_busobid(),
            busobrecid=self.get_busobrecid(),
            offset=0,
            totalsize=len(filedata),
            displaytext=description)
        return response


    @classmethod
    async def search(cls: Type[BusObModel_T], **kwargs: SearchParam) -> list[BusObModel_T]:
        # see: https://help.cherwell.com/bundle/cherwell_rest_api_950_help_only/page/oxy_ex-1/content/system_administration/rest_api/csm_rest_searches.html
        # The Cherwell API is buggy and can return invalid field data. This is worked-around in from_api_response().
        arg_values: dict[str, Any] = {}
        arg_ops: dict[str, str] = {}
        for fieldname, param in kwargs.items():
            if isinstance(param, tuple):
                op = param[0]
                value = param[1]
            else:
                op = 'eq'
                value = param
            arg_ops[fieldname] = op
            arg_values[fieldname] = value
        search_model: BusObModel_T = cls.model_validate(arg_values, strict=True)
        filter: list[FilterInfo] = []
        busobid = cls.get_busobid()
        for fieldname in search_model.model_fields_set:
            fieldId = cls.get_fieldid(fieldname)
            filter.append(FilterInfo(fieldId=FieldID(f"BO:{busobid},FI:{fieldId}"),
                          operator=arg_ops[fieldname], value=getattr(search_model, fieldname)))
        request = SearchResultsRequest(busObId=cls.get_busobid(), filters=filter,
                                       includeAllFields=True, includeSchema=False, pageSize=100000)
        response = await cls.get_instance().connection.GetSearchResultsAdHocV1(request)
        if response.hasError:
            raise CherwellAPIError(f"search[{cls.__name__}]", errorMessage=response.errorMessage,
                                   errorCode=response.errorCode, httpStatusCode=response.httpStatusCode)
        assert response.businessObjects is not None
        return [cls.from_api_response(r, 'search') for r in response.businessObjects]



BusinessObjectModelData = BusinessObjectModelBase._ModelData  # type: ignore
