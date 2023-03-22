from cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject import ReadResponse
from cherwell_pydantic_api.bo.valid_schema import ValidSchema
from cherwell_pydantic_api.interfaces import ApiRequesterInterface
from cherwell_pydantic_api.types import BusObID, BusObIdentifier


class BusinessObjectWrapperBase:
    """Base class for BusinessObjectWrapper. A subclass is passed to the BusinessObjectRegistry constructor."""

    def __init__(self, *, schema: ValidSchema, instance: ApiRequesterInterface):
        pass


class BusinessObjectWrapper(BusinessObjectWrapperBase):
    """Wrap the Cherwell API SchemaResponse object to provide a more convenient interface to the business object schema.
    It is generally created by the BusinessObjectRegistry class.
    This is mainly intended for exploratory use e.g. in a Jupyter notebook or IPython.
    """

    def __init__(self, *, schema: ValidSchema, instance: ApiRequesterInterface):
        self._schema = schema
        self._instance = instance

    async def get(self, publicid: str) -> ReadResponse:
        "Get a business object by public ID."
        return await self._instance.get_bo(self._schema.busObId, publicid=publicid)

    @property
    def busobid(self) -> BusObID:
        "The business object ID."
        return self._schema.busObId

    @property
    def name(self) -> str:
        "The business object name, as reported by Cherwell."
        return self._schema.name

    @property
    def identifier(self) -> BusObIdentifier:
        "The business object identifier used by cherwell-pydantic-api. This will be a valid Python identifier."
        return self._schema.identifier

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} (BO type: {self._schema.name}, instance: {self._instance}, BusObId: {self._schema.busObId})>"
