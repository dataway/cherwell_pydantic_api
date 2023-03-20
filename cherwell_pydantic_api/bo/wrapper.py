from pathlib import Path
from cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject import ReadResponse
from cherwell_pydantic_api.bo.interfaces import ApiRequesterInterface
from cherwell_pydantic_api.bo.pydantic_model_generator import PydanticModelGenerator
from cherwell_pydantic_api.bo.valid_schema import ValidSchema



class BusinessObjectWrapper:
    """Wrap the SchemaResponse object to provide a more convenient interface to the business object schema.
    Terminology note: a "Business Object" is a Cherwell term for what I would call a "class" or "type". So each instance
    of BusinessObjectWrapper represents a type of business object."""

    def __init__(self, schema: ValidSchema, instance: ApiRequesterInterface):
        self._schema = schema
        self._instance = instance

    async def get(self, publicid: str) -> ReadResponse:
        return await self._instance.get_bo(self._schema.busObId, publicid=publicid)

    def generate_model_file(self) -> Path:
        generator = PydanticModelGenerator(self._instance.settings)
        return generator.generate_model_file(self._schema)
    