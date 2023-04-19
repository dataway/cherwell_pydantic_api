import types
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
_Waiter = _WaiterType[Any]


class RestaurantInterface:
    "A restaurant contains a waiter."
    _waiter: _Waiter

    @property
    def waiter(self) -> _Waiter:
        return self._waiter


def wait(amethod: Callable[..., Coroutine[Any, Any, _ReturnType]]) -> Callable[..., _ReturnType]:
    """Decorator to convert an async method into a sync method, using the waiter method of the Interactive instance.
    """

    @wraps(amethod)
    def wrapper(self: RestaurantInterface, *args: Any, **kwargs: Any) -> _ReturnType:
        return self.waiter(amethod(self, *args, **kwargs))
    return wrapper


class WaiterProxy(RestaurantInterface):
    """A proxy around an object with async methods that uses the waiter method to make all public methods sync."""

    def __init__(self, async_obj: object, waiter: _Waiter):
        self._async_obj = async_obj
        self._waiter = waiter
        self.__doc__ = async_obj.__doc__
        self.__wrapped__ = async_obj

    def __getattr__(self, name: str) -> Any:
        if name.startswith('_'):
            raise AttributeError(name)
        amethod = getattr(self._async_obj, name)
        if not callable(amethod):
            return amethod

        @wraps(amethod)
        def wrapper(*args: Any, **kwargs: Any):
            r = amethod(*args, **kwargs)
            if isinstance(r, types.CoroutineType):
                return self._waiter(r) # type: ignore
            return r
        return wrapper

    def __setattr__(self, name: str, value: Any) -> None:
        if not name.startswith('_') and hasattr(self._async_obj, name):
            setattr(self._async_obj, name, value)
        else:
            super().__setattr__(name, value)

    def __delattr__(self, name: str) -> None:
        if not name.startswith('_') and hasattr(self._async_obj, name):
            delattr(self._async_obj, name)
        else:
            super().__delattr__(name)

    def __dir__(self) -> list[str]:
        return dir(self._async_obj)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._async_obj!r})"


@wraps(BusinessObjectWrapper)
def create_bo_wrapper_class(waiter: _Waiter) -> type[BusinessObjectWrapper]:
    class InteractiveBusinessObjectWrapper(BusinessObjectWrapper, RestaurantInterface):
        _waiter = waiter

        @wait
        async def get(self, publicid: str) -> ReadResponse: # type: ignore
            return await super().get(publicid=publicid)

    return InteractiveBusinessObjectWrapper



class Interactive(RestaurantInterface):
    """A wrapper around various cherwell_pydantic_api objects, using the waiter method to make all methods sync (no await needed).
    Each instance of Interactive wraps a specific Instance and indirectly the Connection object.
    It also wraps the BusinessObjectRegistry, so that all BusinessObjectWrapper objects created by it can be accessed with using await.
    """

    def __init__(self, *, instance_name: Optional[str] = None, waiter: Optional[_Waiter] = None):
        self._instance = Instance.use(name=instance_name)
        if waiter is None:
            import asyncio
            waiter = asyncio.run
        self._waiter = waiter
        self._instance_proxy = WaiterProxy(self._instance, self._waiter)
        self._connection_proxy = WaiterProxy(
            self._instance.connection, self._waiter)
        self.help: Any = ''

    @property
    def connection(self) -> WaiterProxy:
        "WaiterProxy wrapper around the Connection object."
        return self._connection_proxy

    @property
    def instance(self) -> WaiterProxy:
        "WaiterProxy wrapper around the Instance object."
        return self._instance_proxy

    def async_wrap(self, **kwargs: object) -> "Interactive":
        "Wrap the given objects with WaiterProxy and add them as attributes to the Interactive instance."
        # TODO: restrict attribute name
        for attr, obj in kwargs.items():
            setattr(self, attr, WaiterProxy(obj, self._waiter))
        return self

    @wait
    async def authenticate(self):
        await self._instance.authenticate()

    @wait
    async def get_bo_schema(self, busobname: str):
        return await self._instance.get_bo_schema(busobname=busobname)

    @wait
    async def get_bo_summaries(self, type: BusinessObjectType = "All") -> list[Summary]:
        return await self._instance.get_bo_summaries(type=type)

    @wait
    async def get_service_info(self) -> ServiceInfoResponse:
        return await self._instance.get_service_info()

    @property
    def bo(self) -> BusinessObjectRegistry:
        self._instance.bo.set_wrapper_class(
            create_bo_wrapper_class(self._waiter))
        return self._instance.bo

    def __repr__(self):
        return f"{self.__class__.__name__}(instance={self._instance!r})"
