# mypy: ignore-errors
from typing import Optional

import click

from ..instance import Instance
from .utils import async_command



@click.command
@click.option('--instance-name', '-I', help='The name of the instance to use. If not specified, the default instance will be used.')
@async_command
async def check(instance_name: Optional[str] = None):
    "Check the connectivity to the Cherwell API."
    instance = Instance.use(instance_name)
    service_info = await instance.get_service_info()
    click.echo(f"OK: instance {instance.settings.name} at {instance.settings.base_url}")
    click.echo(service_info)
    await instance.authenticate()
    click.echo('Authentication OK')
    await instance.logout()
    click.echo('Logout OK')
