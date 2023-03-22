from typing import Optional, cast

from pydantic import Field, constr

from cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject import (
    FieldDefinition,
    GridDefinition,
    Relationship,
    SchemaResponse,
)
from cherwell_pydantic_api.generated_api_utils import ApiBaseModel
from cherwell_pydantic_api.types import BusObID, BusObIdentifier, RelationshipID



class ValidSchema(ApiBaseModel):
    "Corresponds to the type SchemaResponse, but with stricter types and omitting relationship details"
    busObId: BusObID
    fieldDefinitions: list[FieldDefinition]
    firstRecIdField: Optional[str] = None
    gridDefinitions: Optional[list[GridDefinition]] = None
    name: str
    recIdFields: Optional[str] = None
    stateFieldId: Optional[str] = None
    states: Optional[str] = None
    identifier: BusObIdentifier = Field(description="ASCII lowercase of name, to be used as python identifier")
    relationshipIds: list[RelationshipID]

    @classmethod
    def from_schema_response(cls, schema: SchemaResponse):
        if schema.hasError or not schema.busObId or not schema.name or not schema.fieldDefinitions:
            raise ValueError(f'SchemaResponse not valid: {schema}')
        if schema.relationships:
            relIds = [RelationshipID(r.relationshipId) for r in schema.relationships if r.relationshipId]
            relIds.sort()
        else:
            relIds = []
        return cls(busObId=BusObID(schema.busObId),
                   fieldDefinitions=schema.fieldDefinitions,
                   firstRecIdField=schema.firstRecIdField,
                   gridDefinitions=schema.gridDefinitions,
                   name=schema.name,
                   identifier=BusObIdentifier(schema.name),
                   recIdFields=schema.recIdFields,
                   relationshipIds=relIds,
                   stateFieldId=schema.stateFieldId,
                   states=schema.states,)
