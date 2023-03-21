import re
from typing import TYPE_CHECKING, Any, AsyncIterable, Iterable, Mapping, Optional, Union

import httpx
import pydantic



URLType = Union[str, httpx.URL]
CherwellObjectID = dict[str, Any]
HttpStatusCode = httpx.codes

_re_path_param = re.compile(r'^[a-zA-Z0-9_-]+$')


class ApiBaseModel(pydantic.BaseModel):
    """Base class of all generated API models."""

    # Methods to improve IPython experience

    def __dir__(self):
        return [arg[0] for arg in self.__repr_args__()]

    def _repr_pretty_(self, p, cycle):
        if cycle:
            p.text(f"{self.__class__.__name__}(...)")
        else:
            p.begin_group(2, f"{self.__class__.__name__}(")
            first = True
            for name, value in self.__repr_args__():
                if not first:
                    p.text(',')
                    p.breakable(' ')
                first = False
                if name is not None:
                    p.text(f"{name}=")
                p.pretty(value)
            p.end_group(2, ')')


# This interface is only for type checking.
if TYPE_CHECKING:
    class GeneratedInterfaceBaseType:
        async def get(self, url: URLType, *, params: Optional[Mapping[str, Any]] = None) -> Any:
            ...

        async def post_body(self, url: URLType, *, content: Union[str, bytes, Iterable[bytes], AsyncIterable[bytes]], content_type: str = 'application/json', params: Optional[Mapping[str, Any]] = None) -> Any:
            ...

        async def post_form(self, url: URLType, *, data: Optional[Mapping[str, Any]] = None, params: Optional[Mapping[str, Any]] = None) -> Any:
            ...

        async def post(self, url: URLType) -> Any:
            ...

        async def put(self, url: URLType, *, params: Optional[Mapping[str, Any]] = None) -> Any:
            ...

        async def delete(self, url: URLType, *, params: Optional[Mapping[str, Any]] = None) -> Any:
            ...
else:
    class GeneratedInterfaceBaseType:
        pass


class GeneratedInterfaceBase(GeneratedInterfaceBaseType):
    """Generated Cherwell API interface"""

    def validate_path_param(self, value: str):
        if not _re_path_param.match(value):
            raise ValueError(f"Invalid path parameter: {value!r}")
