from typing import Iterable, Mapping, Union

from cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject import SchemaResponse
from cherwell_pydantic_api.bo.valid_schema import ValidSchema
from cherwell_pydantic_api.bo.wrapper import BusinessObjectWrapper
from cherwell_pydantic_api.bo.interfaces import ApiRequesterInterface
from cherwell_pydantic_api.types import BusObID



class BusinessObjectRegistry(Mapping[str, BusinessObjectWrapper]):
    def __init__(self, instance: ApiRequesterInterface):
        self._instance = instance
        self._schemas: dict[str, ValidSchema] = {}
        self._name_to_id: dict[str, str] = {}
        self._wrappers: dict[str, BusinessObjectWrapper] = {}


    def register(self, schema: SchemaResponse):
        if schema.busObId is None:
            raise ValueError('SchemaResponse.busObId is None')
        if schema.name is None:
            raise ValueError('SchemaResponse.name is None')
        busobid = schema.busObId.lower()
        name = schema.name.lower()
        if busobid in self._schemas:
            if self._schemas[busobid] != schema:
                raise ValueError(
                    f'SchemaResponse.busObId {schema.busObId} already registered and new schema is different')
            if name in self._name_to_id:
                if self._name_to_id[name] != busobid:
                    raise ValueError(
                        f'SchemaResponse.name {schema.name} already registered and new busObId is different')
            return
        valid_schema = ValidSchema.from_schema_response(schema)
        self._schemas[busobid] = valid_schema
        self._name_to_id[name] = busobid
        self._wrappers[busobid] = BusinessObjectWrapper(
            valid_schema, self._instance)


    def __getitem__(self, item: Union[BusObID, str]) -> BusinessObjectWrapper:
        """Look up a business object wrapper by name or ID."""
        item_lower = item.lower()
        if item_lower in self._schemas:
            return self._wrappers[item_lower]
        if item_lower in self._name_to_id:
            return self._wrappers[self._name_to_id[item_lower]]
        raise KeyError(item)


    def __iter__(self) -> Iterable[str]:
        """Iterate over the names of the registered business objects. (Not the business object IDs)"""
        return iter(self._name_to_id.keys())


    def __len__(self) -> int:
        """Return the number of registered business objects."""
        return len(self._schemas)

    
    def __getattr__(self, attr: Union[BusObID, str]) -> BusinessObjectWrapper:
        try:
            return self.__getitem__(attr)
        except KeyError:
            raise AttributeError(attr)


    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(instance={self._instance.settings.name})'


    def __dir__(self) -> Iterable[str]:
        return [k for k in self._name_to_id.keys()] + [k for k in super().__dir__()]
