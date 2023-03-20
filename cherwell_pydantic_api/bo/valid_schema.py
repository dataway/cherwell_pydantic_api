from typing import List, Optional

from cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject import (
    FieldDefinition,
    GridDefinition,
    Relationship,
    SchemaResponse,
)
from cherwell_pydantic_api.generated_api_utils import ApiBaseModel
from cherwell_pydantic_api.types import BusObID



class ValidSchema(ApiBaseModel):
    busObId: BusObID
    fieldDefinitions: List[FieldDefinition]
    firstRecIdField: Optional[str] = None
    gridDefinitions: Optional[List[GridDefinition]] = None
    name: str
    recIdFields: Optional[str] = None
    relationships: Optional[List[Relationship]] = None
    stateFieldId: Optional[str] = None
    states: Optional[str] = None

    @classmethod
    def from_schema_response(cls, schema: SchemaResponse):
        if schema.hasError or not schema.busObId or not schema.name or not schema.fieldDefinitions:
            raise ValueError(f'SchemaResponse not valid: {schema}')
        return cls(busObId=schema.busObId,
                   fieldDefinitions=schema.fieldDefinitions,
                   firstRecIdField=schema.firstRecIdField,
                   gridDefinitions=schema.gridDefinitions,
                   name=schema.name,
                   recIdFields=schema.recIdFields,
                   relationships=schema.relationships,
                   stateFieldId=schema.stateFieldId,
                   states=schema.states,)
