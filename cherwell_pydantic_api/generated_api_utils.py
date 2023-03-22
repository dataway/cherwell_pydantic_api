import re
from typing import TYPE_CHECKING, Any, AsyncIterable, Iterable, Literal, Mapping, Optional, Type, Union, get_origin

import httpx
import pydantic



URLType = Union[str, httpx.URL]
HttpStatusCode = httpx.codes
Response = httpx.Response

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
        async def get(self, url: URLType, *, params: Optional[Mapping[str, Any]] = None) -> Response:
            ...

        async def post_body(self, url: URLType, *, content: Union[str, bytes, Iterable[bytes], AsyncIterable[bytes]], content_type: str = 'application/json', params: Optional[Mapping[str, Any]] = None) -> Response:
            ...

        async def post_form(self, url: URLType, *, data: Optional[Mapping[str, Any]] = None, params: Optional[Mapping[str, Any]] = None) -> Response:
            ...

        async def post(self, url: URLType) -> Response:
            ...

        async def put(self, url: URLType, *, params: Optional[Mapping[str, Any]] = None) -> Response:
            ...

        async def delete(self, url: URLType, *, params: Optional[Mapping[str, Any]] = None) -> Response:
            ...
else:
    class GeneratedInterfaceBaseType:
        pass


class GeneratedInterfaceBase(GeneratedInterfaceBaseType):
    """Generated Cherwell API interface"""

    def validate_path_param(self, value: str, type: Type = str):
        if not _re_path_param.match(value):
            raise ValueError(f"Invalid path parameter: {value!r}")
        type_origin = get_origin(type)
        if type_origin is Literal:
            if value.lower() not in [a.lower() for a in type.__args__]:
                raise ValueError(
                    f"Parameter mismatch with literal: {value} not in {type}")


    def parse_response(self, response: Response, rtype: Type) -> Any:
        # If the response type has a `httpStatusCode` field, set it to the actual HTTP status code
        # and don't raise an exception if the HTTP request failed
        try:
            # issubclass can fail especially with types
            is_api = issubclass(rtype, ApiBaseModel)
        except:
            is_api = False

        if is_api:
            status_code = None
            try:
                # The Cherwell server sends the header: "Content-Type: application/json;charset=UTF-8"
                obj = rtype.parse_raw(response.content,
                                      content_type=response.headers.get(
                                          'content-type').split(';', 1)[0],
                                      encoding=response.encoding or 'utf-8')
                if hasattr(obj, 'httpStatusCode'):
                    obj.httpStatusCode = response.status_code  # type: ignore
                    status_code = response.status_code
            except pydantic.ValidationError:
                # Maybe the pydantic validation failed because the HTTP request failed
                if not response.is_success:
                    response.raise_for_status()
                raise
            # HTTP error: if we can respond with a httpStatusCode in the response, do so, otherwise raise an exception
            if not response.is_success:
                if status_code:
                    return obj
                response.raise_for_status()
            # HTTP success and pydantic validation succeeded
            return obj

        # Reach here if the type isn't a pydantic model
        if not response.is_success:
            response.raise_for_status()

        if rtype is str:
            return response.text
        if rtype is bytes:
            return response.content
        if rtype is None:
            return None

        return pydantic.parse_raw_as(rtype,
                                     response.content,
                                     content_type=response.headers.get(
                                         'content-type').split(';', 1)[0],
                                     encoding=response.encoding or 'utf-8')

