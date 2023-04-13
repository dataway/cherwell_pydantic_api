from functools import wraps

import click



def async_command(command):
    @wraps(command)
    def wrapper(*args, **kwargs):
        import asyncio
        return asyncio.run(command(*args, **kwargs))
    return wrapper


def output_dict(d: dict, *, prefix: str = '', **kwargs):
    for k, v in d.items():
        if isinstance(v, dict):
            output_dict(v, prefix=f'{prefix}{k}.')
        else:
            click.echo(click.style(f'{prefix}{k}', fg='cyan') + ': ' + click.style(v, fg='green' if v else 'red'), **kwargs)
