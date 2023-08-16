from collections import defaultdict
from typing import Iterable, Iterator, Mapping, Optional, Union
from weakref import WeakValueDictionary

from pydantic import AnyHttpUrl, BaseModel

from cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject import (
    SchemaResponse,
    Summary,
)
from cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core import ServiceInfoResponse
from cherwell_pydantic_api.bo.valid_schema import ValidRelationship, ValidSchema
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


class BusinessObjectModelRegistryMixin:
    pass


class BusinessObjectRegistry(Mapping[str, BusinessObjectWrapperBase]):
    # There is exactly one BusinessObjectRegistry per Instance.
    # There can be more than one wrapper per BO but only one schema or summary.

    _instance: ApiRequesterInterface
    _wrapper_class: type[BusinessObjectWrapperBase]
    _schemas: dict[BusObID, ValidSchema]
    _summaries: dict[BusObID, Summary]
    _parents: dict[BusObID, BusObID]
    _name_to_id: dict[BusObIdentifier, BusObID]
    _relationships: dict[RelationshipID, ValidRelationship]
    _unresolved_relationships: dict[BusObID, set[RelationshipID]]
    _bo_rels: defaultdict[BusObID, set[RelationshipID]] = defaultdict(set)
    _wrappers: WeakValueDictionary[BusObID, BusinessObjectWrapperBase] = WeakValueDictionary()
    _service_info: Optional[ServiceInfoResponse] = None
    _models: WeakValueDictionary[BusObID, type[BusinessObjectModelRegistryMixin]] = WeakValueDictionary()


    def __init__(self, instance: ApiRequesterInterface, wrapper_class: type[BusinessObjectWrapperBase] = BusinessObjectWrapper):
        self._instance = instance
        self._wrapper_class = wrapper_class
        self._schemas = {}
        self._summaries = {}
        self._parents = {}
        self._name_to_id = {}
        self._relationships = {}
        self._unresolved_relationships = defaultdict(set)
        self._bo_rels = defaultdict(set)
        self._wrappers = WeakValueDictionary()
        self._service_info = None
        self._models = WeakValueDictionary()


    def marshal(self, include_summaries: bool = False) -> Iterable[tuple[str, str]]:
        yield ('instance_name.txt', self._instance.settings.name)
        for busobid, schema in self._schemas.items():
            yield (f'bo.{busobid}.json', schema.model_dump_json(indent=2, exclude_unset=True, exclude_defaults=True))
        for relid, rel in self._relationships.items():
            yield (f'rel.{relid}.json', rel.model_dump_json(indent=2, exclude={'target_schema', 'source_schema', 'fieldDefinitions'}, exclude_unset=True, exclude_defaults=True))
        if include_summaries:
            for busobid, summary in self._summaries.items():
                if busobid in self._schemas:
                    continue
                yield (f'bo_sum.{busobid}.json', summary.model_dump_json(indent=2))
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
            yield ('service_info.json', si_model.model_dump_json(indent=2))


    def get_schema(self, busobid: BusObID) -> ValidSchema:
        return self._schemas[BusObID(busobid)]


    def register(self, schema: SchemaResponse):
        if schema.busObId is None:
            raise ValueError('SchemaResponse.busObId is None')
        if schema.name is None:
            raise ValueError('SchemaResponse.name is None')
        valid_schema = ValidSchema.from_schema_response(schema)
        busobid = valid_schema.busObId
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
            summary = self._summaries.get(busobid)
            if summary is None:
                raise ValueError(
                    f'busObId {busobid} ({valid_schema.name}) has relationships but no summary was registered')
            for rel in schema.relationships:
                valid_rel = ValidRelationship.from_relationship(
                    valid_schema, rel)
                relid = valid_rel.relationshipId
                assert relid in valid_schema.relationshipIds
                valid_rel.source_schema = valid_schema
                valid_schema.relationships[relid] = valid_rel
                if valid_rel.target in self._schemas:
                    valid_rel.target_schema = self.get_schema(valid_rel.target)
                    valid_rel.target_name = valid_rel.target_schema.name
                else:
                    self._unresolved_relationships[valid_rel.target].add(relid)
                    if valid_rel.target in self._summaries:
                        valid_rel.target_name = self._summaries[valid_rel.target].name
                if relid in self._relationships:
                    existing_rel = self._relationships[relid]
                    if existing_rel.source != busobid:
                        if self._parents.get(busobid) == existing_rel.source:
                            # print(f"Skipping child relationship {relid} on {identifier} < {existing_rel.source_schema.identifier}")
                            continue
                    if existing_rel != valid_rel:
                        raise ValueError(
                            f'Relationship {relid} already registered ({existing_rel.source_schema.name} to {existing_rel.target_schema and existing_rel.target_schema.name}) and new relationship is different ({valid_schema.name} to {valid_rel.target_schema and valid_rel.target_schema.name})')
                    if not relid in self._bo_rels[busobid]:
                        # TODO: This occurs in group summaries
                        continue
                        raise ValueError(
                            f"Relationship {relid} is not in busObId {busobid}")
                else:
                    self._relationships[relid] = valid_rel
                    self._bo_rels[busobid].add(relid)
                    self._bo_rels[valid_rel.target].add(relid)

        # Fixup relationships of which this bo is a target
        if self._unresolved_relationships[busobid]:
            for relid in self._unresolved_relationships[busobid]:
                urel = self._relationships[relid]
                urel.target_schema = valid_schema
            del self._unresolved_relationships[busobid]


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
        if summary.groupSummaries:
            for sub_summary in summary.groupSummaries:
                if sub_summary.busObId is None:
                    raise ValueError(
                        'Summary.busObId is None in groupSummaries')
                self.register_summary(sub_summary)
                self._parents[sub_summary.busObId] = busobid


    def register_model(self, busobid: BusObID, model: type[BusinessObjectModelRegistryMixin]):
        self._models[busobid] = model


    def get_model(self, busobid: BusObID) -> type[BusinessObjectModelRegistryMixin]:
        return self._models[busobid]


    def register_service_info(self, service_info: ServiceInfoResponse):
        self._service_info = service_info


    def set_wrapper_class(self, wrapper_class: type[BusinessObjectWrapperBase]):
        if wrapper_class != self._wrapper_class:
            self._wrappers.clear()
        self._wrapper_class = wrapper_class


    def get_wrapper(self, busobid: BusObID) -> BusinessObjectWrapperBase:
        if busobid not in self._wrappers:
            wrapper = self._wrapper_class(
                schema=self._schemas[busobid], instance=self._instance)
            self._wrappers[busobid] = wrapper
            return wrapper
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


    def __iter__(self) -> Iterator[str]:
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
