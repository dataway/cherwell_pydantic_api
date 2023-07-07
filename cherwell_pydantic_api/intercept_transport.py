# pyright: reportPrivateUsage=false
import json
import time
from pathlib import Path
from types import TracebackType
from typing import Any, Optional, Type, TypeVar

import httpx
from httpx._models import Request, Response



A = TypeVar("A", bound="InterceptTransport")


def json_default(obj: Any):
    if isinstance(obj, (bytes, bytearray)):
        return obj.decode(errors="ignore")
    if isinstance(obj, httpx.URL):
        return str(obj)
    if isinstance(obj, httpx.Headers):
        return dict(obj)
    return str(obj)


class InterceptTransport(httpx.AsyncBaseTransport):
    _client: httpx.AsyncClient
    _original_transport: httpx.AsyncBaseTransport

    def __init__(self, client: httpx.AsyncClient, path: Path):
        self._client = client
        self._path = path.absolute()
        assert self._path.is_dir()
        # Monkey patch the client's transport with this one
        self._original_transport = client._transport
        client._transport = self

    async def __aenter__(self: A) -> A:
        return await self._original_transport.__aenter__() # type: ignore

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]] = None,
        exc_value: Optional[BaseException] = None,
        traceback: Optional[TracebackType] = None,
    ) -> None:
        await self._original_transport.__aexit__(exc_type, exc_value, traceback)

    async def handle_async_request(self, request: Request) -> Response:
        ts = time.monotonic()
        fname = self._path / f"req_{ts}_{request.url.host}.json"
        with fname.open("w") as f:
            data: dict[str, Any] = {'req': {k: v for k, v in vars(request).items() if k not in ('extensions', 'stream')}, 'ts1': ts}
            try:
                response = await self._original_transport.handle_async_request(request)
                await response.aread()
                data['ts2'] = time.monotonic()
                data['resp'] = {k: v for k, v in vars(response).items() if k not in ('stream',)}
            except Exception as exc:
                data['exc'] = exc
                raise exc
            try:
                js = json.dumps(data, indent=2, default=json_default)
            except Exception as exc:
                js = f"{'error': 'Could not serialize request', 'exc': '{exc}'}"
            f.write(js)
        return response

    async def aclose(self) -> None:
        await self._original_transport.aclose()
