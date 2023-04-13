from typing import Optional

import click

from cherwell_pydantic_api.bo.modelgen.collector import Collector
from cherwell_pydantic_api.bo.modelgen.repo import ModelRepo
from cherwell_pydantic_api.settings import Settings

from ..instance import Instance
from .utils import async_command, output_dict



@click.group(name='repo')
@click.option('--instance-name', '-I', help='The name of the instance to use. If not specified, the default instance will be used.')
@click.pass_context
def repo_group(ctx, instance_name: Optional[str] = None):
    "Manage the repository"
    ctx.ensure_object(dict)
    instance = Instance.use(instance_name)
    ctx.obj['instance_name'] = instance_name
    ctx.obj['instance'] = instance
    try:
        repo = ModelRepo()
    except FileNotFoundError:
        click.secho(
            f"No repository found at expected location of '{Settings().repo_dir.absolute()}'", fg='yellow')
        repo = None
    ctx.obj['repo'] = repo


@repo_group.command()
@click.pass_context
def info(ctx):
    "Display information about the repository"
    instance = ctx.obj['instance']
    if ctx.obj['repo'] is not None:
        repo_info = ctx.obj['repo'].get_info(instance=instance)
    else:
        repo_info = ModelRepo(permit_missing=True).get_info(instance=instance)
    output_dict(repo_info)


@repo_group.command()
@click.pass_context
@click.option('--verbose', '-v', help='Verbose output from the collector', is_flag=True)
@async_command
async def update(ctx, verbose: bool = False):
    "Connect to the Cherwell API and update the repository"
    repo = ctx.obj['repo']
    if repo is None:
        return 1
    instance = ctx.obj['instance']
    collector = Collector(instance=instance, verbose=verbose)
    collector.load_settings(repo=repo)
    await instance.authenticate()
    click.echo('Authentication OK')
    await collector.collect()
    if verbose:
        click.secho('Updating registry: ', nl=False, fg='cyan')
    r = repo.save_instance(instance=instance)
    if verbose:
        click.secho(r, fg='green')
        click.secho('Generating models:', nl=False, fg='cyan')
    r = collector.save_models(repo=repo)
    if verbose:
        click.secho(r, fg='green')
    await instance.logout()
    click.echo('Logout OK')
