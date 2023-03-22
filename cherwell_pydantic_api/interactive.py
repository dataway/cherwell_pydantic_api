from typing import Any, Callable, Coroutine, Literal, Optional, TypeVar

from cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject import (
    ReadResponse,
    Summary,
)
from cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core import ServiceInfoResponse
from cherwell_pydantic_api.api import Connection
from cherwell_pydantic_api.bo.registry import BusinessObjectRegistry
from cherwell_pydantic_api.bo.wrapper import BusinessObjectWrapper
from cherwell_pydantic_api.instance import Instance



__all__ = ['Interactive']


_ReturnType = TypeVar("_ReturnType")
_WaiterType = Callable[[Coroutine[Any, Any, _ReturnType]], _ReturnType]


class RestaurantInterface:
    "A restaurant contains a waiter."
    _waiter: _WaiterType


def wait(amethod: Callable[..., Coroutine[Any, Any, _ReturnType]]) -> Callable[..., _ReturnType]:
    """Decorator to convert an async method into a sync method, using the waiter method of the Interactive instance.
    """

    def wrapper(self: RestaurantInterface, *args, **kwargs):
        return self._waiter(amethod(self, *args, **kwargs))
    wrapper.__doc__ = amethod.__doc__
    return wrapper


class ConnectionProxy(RestaurantInterface):
    """A proxy for the Connection object, using the waiter method to make all methods sync."""

    def __init__(self, connection: Connection, waiter: _WaiterType):
        self._connection = connection
        self._waiter = waiter

    def __getattr__(self, name: str) -> Any:
        amethod = getattr(self._connection, name)

        def wrapper(*args, **kwargs):
            return self._waiter(amethod(*args, **kwargs))
        wrapper.__doc__ = amethod.__doc__
        return wrapper

    def __dir__(self) -> list[str]:
        return dir(self._connection)


def create_bo_wrapper_class(waiter: _WaiterType) -> type[BusinessObjectWrapper]:
    class InteractiveBusinessObjectWrapper(BusinessObjectWrapper, RestaurantInterface):
        _waiter = waiter

        @wait
        async def get(self, publicid: str) -> ReadResponse:
            return await super().get(publicid=publicid)

    return InteractiveBusinessObjectWrapper



class Interactive(RestaurantInterface):
    def __init__(self, *, instance_name: Optional[str] = None, waiter: Optional[_WaiterType] = None):
        self.instance = Instance.use(name=instance_name)
        if waiter is None:
            import asyncio
            waiter = asyncio.run
        self._waiter = waiter
        self._connection_proxy = ConnectionProxy(
            self.instance._connection, self._waiter)

    @property
    def connection(self) -> ConnectionProxy:
        return self._connection_proxy

    @wait
    async def authenticate(self):
        await self.instance.authenticate()

    @wait
    async def get_bo_schema(self, busobname: str):
        return await self.instance.get_bo_schema(busobname=busobname)

    @wait
    async def get_bo_summaries(self, type: Literal["All", "Major", "Supporting", "Lookup", "Groups"] = "Major") -> list[Summary]:
        return await self.instance.get_bo_summaries(type=type)

    @wait
    async def get_service_info(self) -> ServiceInfoResponse:
        return await self.instance.get_service_info()

    @property
    def bo(self) -> BusinessObjectRegistry:
        self.instance.bo.set_wrapper_class(
            create_bo_wrapper_class(self._waiter))
        return self.instance.bo
