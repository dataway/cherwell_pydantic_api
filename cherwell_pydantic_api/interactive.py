from functools import wraps
from typing import Any, Callable, Coroutine, Optional, TypeVar

from cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject import (
    ReadResponse,
    Summary,
)
from cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.Core import ServiceInfoResponse
from cherwell_pydantic_api.bo.registry import BusinessObjectRegistry
from cherwell_pydantic_api.bo.wrapper import BusinessObjectWrapper
from cherwell_pydantic_api.instance import Instance
from cherwell_pydantic_api.types import BusinessObjectType



__all__ = ['Interactive']


_ReturnType = TypeVar("_ReturnType")
_WaiterType = Callable[[Coroutine[Any, Any, _ReturnType]], _ReturnType]


class RestaurantInterface:
    "A restaurant contains a waiter."
    _waiter: _WaiterType


def wait(amethod: Callable[..., Coroutine[Any, Any, _ReturnType]]) -> Callable[..., _ReturnType]:
    """Decorator to convert an async method into a sync method, using the waiter method of the Interactive instance.
    """

    @wraps(amethod)
    def wrapper(self: RestaurantInterface, *args, **kwargs):
        return self._waiter(amethod(self, *args, **kwargs))
    return wrapper


class WaiterProxy(RestaurantInterface):
    """A proxy around an object with async methods that uses the waiter method to make all methods sync."""

    def __init__(self, async_obj: object, waiter: _WaiterType):
        self._async_obj = async_obj
        self._waiter = waiter

    def __getattr__(self, name: str) -> Any:
        amethod = getattr(self._async_obj, name)

        @wraps(amethod)
        def wrapper(*args, **kwargs):
            return self._waiter(amethod(*args, **kwargs))
        return wrapper

    def __dir__(self) -> list[str]:
        return dir(self._async_obj)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._async_obj!r})"


@wraps(BusinessObjectWrapper)
def create_bo_wrapper_class(waiter: _WaiterType) -> type[BusinessObjectWrapper]:
    class InteractiveBusinessObjectWrapper(BusinessObjectWrapper, RestaurantInterface):
        _waiter = waiter

        @wait
        async def get(self, publicid: str) -> ReadResponse:
            return await super().get(publicid=publicid)

    return InteractiveBusinessObjectWrapper



class Interactive(RestaurantInterface):
    """A wrapper around various cherwell_pydantic_api objects, using the waiter method to make all methods sync (no await needed).
    Each instance of Interactive wraps a specific Instance and indirectly the Connection object.
    It also wraps the BusinessObjectRegistry, so that all BusinessObjectWrapper objects created by it can be accessed with using await.
    """
    def __init__(self, *, instance_name: Optional[str] = None, waiter: Optional[_WaiterType] = None):
        self.instance = Instance.use(name=instance_name)
        if waiter is None:
            import asyncio
            waiter = asyncio.run
        self._waiter = waiter
        self._connection_proxy = WaiterProxy(
            self.instance._connection, self._waiter)

    @property
    def connection(self) -> WaiterProxy:
        return self._connection_proxy

    def async_wrap(self, **kwargs) -> "Interactive":
        "Wrap the given objects with WaiterProxy and add them as attributes to the Interactive instance."
        # TODO: restrict attribute name
        for attr, obj in kwargs.items():
            setattr(self, attr, WaiterProxy(obj, self._waiter))
        return self

    @wait
    async def authenticate(self):
        await self.instance.authenticate()

    @wait
    async def get_bo_schema(self, busobname: str):
        return await self.instance.get_bo_schema(busobname=busobname)

    @wait
    async def get_bo_summaries(self, type: BusinessObjectType = "All") -> list[Summary]:
        return await self.instance.get_bo_summaries(type=type)

    @wait
    async def get_service_info(self) -> ServiceInfoResponse:
        return await self.instance.get_service_info()

    @property
    def bo(self) -> BusinessObjectRegistry:
        self.instance.bo.set_wrapper_class(
            create_bo_wrapper_class(self._waiter))
        return self.instance.bo

    def __repr__(self):
        return f"{self.__class__.__name__}(instance={self.instance!r})"
