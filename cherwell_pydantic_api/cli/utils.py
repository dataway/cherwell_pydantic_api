from functools import wraps
from typing import Any, Callable, Coroutine

import click



def async_command(command: Callable[..., Coroutine[Any, Any, Any]]) -> Callable[..., Callable[..., Any]]:
    @wraps(command)
    def wrapper(*args: Any, **kwargs: Any):
        import asyncio
        return asyncio.run(command(*args, **kwargs))
    return wrapper


def output_dict(d: dict[str, Any], *, prefix: str = '', **kwargs: Any) -> None:
    for k, v in d.items():
        if isinstance(v, dict):
            output_dict(v, prefix=f'{prefix}{k}.')  # type: ignore
        else:
            click.echo(click.style(f'{prefix}{k}', fg='cyan') + ': ' +
                       click.style(v, fg='green' if v else 'red'), **kwargs)
