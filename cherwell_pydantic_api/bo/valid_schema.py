from typing import Optional

from pydantic import Field

from cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject import (
    FieldDefinition,
    GridDefinition,
    Relationship,
    SchemaResponse,
)
from cherwell_pydantic_api.generated_api_utils import ApiBaseModel
from cherwell_pydantic_api.types import BusObID, BusObIdentifier, FieldID, FieldIdentifier, RelationshipID
from cherwell_pydantic_api.utils import fieldid_parts



class ValidFieldDefinition(FieldDefinition):
    fieldId: FieldID
    name: str
    type: str
    short_field_id: FieldID = Field(description="Just the field ID, without 'BO:..,FI:...'")
    identifier: FieldIdentifier

    def __init__(self, **data):
        data['short_field_id'] = fieldid_parts(data['fieldId'])['FI']
        data['identifier'] = FieldIdentifier(data['name'])
        super().__init__(**data)


class ValidSchema(ApiBaseModel):
    "Corresponds to the type SchemaResponse, but with stricter types and omitting relationship details"
    busObId: BusObID
    fieldDefinitions: list[ValidFieldDefinition]
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
                   fieldDefinitions=[ValidFieldDefinition(**field.dict()) for field in schema.fieldDefinitions],
                   firstRecIdField=schema.firstRecIdField,
                   gridDefinitions=schema.gridDefinitions,
                   name=schema.name,
                   identifier=BusObIdentifier(schema.name),
                   recIdFields=schema.recIdFields,
                   relationshipIds=relIds,
                   stateFieldId=schema.stateFieldId,
                   states=schema.states,)


class ValidRelationship(ApiBaseModel):
    "Corresponds to the type Relationship, but with stricter types and links to source and target ValidSchema objects"
    relationshipId: RelationshipID
    cardinality: str
    description: Optional[str] = None
    displayName: Optional[str] = None
    fieldDefinitions: list[ValidFieldDefinition]
    target: BusObID
    target_schema: Optional[ValidSchema] = None
    source: BusObID
    source_schema: ValidSchema

    @classmethod
    def from_relationship(cls, source_schema: ValidSchema, relationship: Relationship):
        if not relationship.relationshipId or not relationship.cardinality or not relationship.target or not relationship.fieldDefinitions:
            raise ValueError(f'Relationship not valid: {relationship}')
        return cls(relationshipId=RelationshipID(relationship.relationshipId),
                   cardinality=relationship.cardinality,
                   description=relationship.description,
                   displayName=relationship.displayName,
                   fieldDefinitions=[ValidFieldDefinition(**field.dict()) for field in relationship.fieldDefinitions],
                   target=BusObID(relationship.target),
                   source=source_schema.busObId,
                   source_schema=source_schema,
                   )


