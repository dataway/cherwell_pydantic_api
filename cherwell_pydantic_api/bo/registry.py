from collections import defaultdict
from typing import Iterable, Mapping, Optional, Union, cast

from pydantic import AnyHttpUrl, BaseModel

from cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject import (
    Relationship,
    SchemaResponse,
    Summary,
)
from cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core import ServiceInfoResponse
from cherwell_pydantic_api.bo.valid_schema import ValidSchema
from cherwell_pydantic_api.bo.wrapper import BusinessObjectWrapper, BusinessObjectWrapperBase
from cherwell_pydantic_api.interfaces import ApiRequesterInterface
from cherwell_pydantic_api.types import BusObID, BusObIdentifier, RelationshipID


# Registry of business object schemas.
# It appears that the API returns schema fields in the same order, but not the relationships.



class ServiceInfoModel(BaseModel):
    apiVersion: Optional[str] = None
    csmCulture: Optional[str] = None
    csmVersion: Optional[str] = None
    base_url: Optional[AnyHttpUrl] = None



class BusinessObjectRegistry(Mapping[str, BusinessObjectWrapperBase]):
    # There can be more than one wrapper per BO but only one schema or summary.

    def __init__(self, instance: ApiRequesterInterface, wrapper_class: type[BusinessObjectWrapperBase] = BusinessObjectWrapper):
        self._instance = instance
        self._wrapper_class = wrapper_class
        self._schemas: dict[BusObID, ValidSchema] = {}
        self._summaries: dict[BusObID, Summary] = {}
        self._name_to_id: dict[BusObIdentifier, BusObID] = {}
        self._relationships: dict[RelationshipID, Relationship] = {}
        self._bo_rels: defaultdict[BusObID,
                                   set[RelationshipID]] = defaultdict(set)
        self._wrappers: dict[BusObID, wrapper_class] = {}
        self._service_info: Optional[ServiceInfoResponse] = None


    def marshal(self, include_summaries: bool = False) -> Iterable[tuple[str, str]]:
        yield ('instance_name.txt', self._instance.settings.name)
        for busobid, schema in self._schemas.items():
            yield (f'bo.{busobid}.json', schema.json(indent=2, exclude={'relationships'}, sort_keys=True))
        # TODO: include relationships
        if include_summaries:
            for busobid, summary in self._summaries.items():
                if busobid in self._schemas:
                    continue
                yield (f'bo_sum.{busobid}.json', summary.json(indent=2, sort_keys=True))
        names_csv = [
            f"{name};{self._name_to_id[name]}\n" for name in self._name_to_id.keys()]
        names_csv.sort()
        yield ('names.csv', ''.join(names_csv))
        if self._service_info:
            si_model = ServiceInfoModel(
                apiVersion=self._service_info.apiVersion,
                csmCulture=self._service_info.csmCulture,
                csmVersion=self._service_info.csmVersion,
                base_url=self._instance.settings.base_url,
            )
            yield ('service_info.json', si_model.json(indent=2, sort_keys=True))


    def get_schema(self, busobid: BusObID) -> ValidSchema:
        return self._schemas[BusObID(busobid)]


    def register(self, schema: SchemaResponse):
        if schema.busObId is None:
            raise ValueError('SchemaResponse.busObId is None')
        if schema.name is None:
            raise ValueError('SchemaResponse.name is None')
        busobid = BusObID(schema.busObId)
        valid_schema = ValidSchema.from_schema_response(schema)
        identifier = valid_schema.identifier
        if busobid in self._schemas:
            if self._schemas[busobid] != valid_schema:
                raise ValueError(
                    f'SchemaResponse busObId {busobid} already registered and new schema is different')
            if identifier in self._name_to_id:
                if self._name_to_id[identifier] != busobid:
                    raise ValueError(
                        f'SchemaResponse identifier {identifier} already registered and new busObId is different')
        else:
            self._schemas[busobid] = valid_schema
            self._name_to_id[identifier] = busobid

        # Register relationships
        if schema.relationships:
            for rel in schema.relationships:
                assert rel.relationshipId is not None
                relid = RelationshipID(rel.relationshipId)
                assert relid in valid_schema.relationshipIds
                if relid in self._relationships:
                    if self._relationships[relid] != rel:
                        raise ValueError(
                            f'Relationship {relid} already registered and new relationship is different')
                    if not relid in self._bo_rels[busobid]:
                        raise ValueError(
                            f"Relationship {relid} is not in busObId {busobid}")
                else:
                    self._relationships[relid] = rel
                    self._bo_rels[busobid].add(relid)


    def register_summary(self, summary: Summary):
        # TODO: decide if this is needed, if so make it more useful
        if summary.busObId is None:
            raise ValueError('Summary.busObId is None')
        if summary.name is None:
            raise ValueError('Summary.name is None')
        busobid = BusObID(summary.busObId)
        identifier = BusObIdentifier(summary.name)
        if identifier in self._name_to_id:
            if self._name_to_id[identifier] != busobid:
                raise ValueError(
                    f'Summary name {summary.name} already registered and new busObId is different')
        else:
            self._name_to_id[identifier] = busobid
        if busobid in self._summaries:
            if self._summaries[busobid] != summary:
                raise ValueError(
                    f'Summary busObId {summary.busObId} already registered and new summary is different')
            return
        self._summaries[busobid] = summary


    def register_service_info(self, service_info: ServiceInfoResponse):
        self._service_info = service_info


    def set_wrapper_class(self, wrapper_class: type[BusinessObjectWrapperBase]):
        if wrapper_class != self._wrapper_class:
            self._wrappers.clear()
        self._wrapper_class = wrapper_class


    def get_wrapper(self, busobid: BusObID) -> BusinessObjectWrapperBase:
        if busobid not in self._wrappers:
            self._wrappers[busobid] = self._wrapper_class(
                schema=self._schemas[busobid], instance=self._instance)
        return self._wrappers[busobid]


    def __getitem__(self, item: Union[BusObID, BusObIdentifier, str]) -> BusinessObjectWrapperBase:
        """Look up a business object wrapper by identifer or ID."""
        try:
            busobid = BusObID(item)
        except ValueError:
            busobid = False
        if not busobid or busobid not in self._schemas:
            busobname = BusObIdentifier(item)
            busobid = self._name_to_id[busobname]
        return self.get_wrapper(busobid)


    def __iter__(self) -> Iterable[str]:
        """Iterate over the names of the registered business objects. Don't include summaries. (Not the business object IDs)"""
        return iter([k for k, v in self._name_to_id.items() if v in self._schemas])


    def __len__(self) -> int:
        """Return the number of registered business objects. Don't include summaries."""
        return len(self._schemas)


    def __getattr__(self, attr: Union[BusObIdentifier, str]) -> BusinessObjectWrapperBase:
        try:
            return self.__getitem__(attr)
        except KeyError:
            raise AttributeError(attr)


    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}[{len(self._schemas)}] (instance={self._instance.settings.name})>'


    def __dir__(self) -> Iterable[str]:
        return [k for k in self.__iter__()] + [k for k in super().__dir__()]
