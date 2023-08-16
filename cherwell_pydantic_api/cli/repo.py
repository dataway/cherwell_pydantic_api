# mypy: ignore-errors

from typing import TYPE_CHECKING, Optional

import click



try:
    from cherwell_pydantic_api.bo.modelgen.collector import Collector
    from cherwell_pydantic_api.bo.modelgen.repo import ModelRepo
    _imports_ok = True
except:
    _imports_ok = False

    @click.command(name='repo')
    def repo_group():  # type: ignore
        click.secho(f"UNAVAILABLE - be sure to install cherwell_pydantic_api[modelgen]", fg='red')
if TYPE_CHECKING:
    from cherwell_pydantic_api.bo.modelgen.collector import Collector
    from cherwell_pydantic_api.bo.modelgen.repo import ModelRepo


if _imports_ok:
    from cherwell_pydantic_api.settings import Settings

    from ..instance import Instance
    from .utils import async_command, output_dict


    @click.group(name='repo')
    @click.option('--instance-name', '-I', help='The name of the instance to use. If not specified, the default instance will be used.')
    @click.pass_context
    def repo_group(ctx: click.Context, instance_name: Optional[str] = None):
        "Manage the repository"
        ctx.ensure_object(dict)
        instance = Instance.use(instance_name)
        ctx.obj['instance_name'] = instance_name
        ctx.obj['instance'] = instance
        try:
            repo = ModelRepo()
        except FileNotFoundError:
            if ctx.invoked_subcommand != 'create':
                click.secho(
                    f"No repository found at expected location of '{Settings().repo_dir.absolute()}'", fg='yellow')
            repo = None
        ctx.obj['repo'] = repo


    @repo_group.command()
    @click.pass_context
    def info(ctx: click.Context):
        "Display information about the repository"
        instance = ctx.obj['instance']
        if ctx.obj['repo'] is not None:
            repo_info = ctx.obj['repo'].get_info(instance=instance)
        else:
            repo_info = ModelRepo(permit_missing=True).get_info(instance=instance)
        output_dict(repo_info)


    @repo_group.command()
    @click.pass_context
    def create(ctx: click.Context):
        "Create the repository if it does not exist, and generate an initial collector_settings.json file"
        instance = ctx.obj['instance']
        no_action = True
        if ctx.obj['repo'] is None:
            repo = ModelRepo(create=True)
            repo_info = repo.get_info(instance=instance)
            click.secho(f"Repository created in {repo_info['repo']['settings_path']}", fg='green')  # type: ignore
            no_action = False
        else:
            repo = ctx.obj['repo']

        collector = Collector(instance=instance)
        try:
            collector.load_settings(repo=repo)
        except FileNotFoundError:
            collector.bo_exclude_filter = None
            collector.bo_include_filter = "(?i)ticket$"  # type: ignore
            collector.save_settings(repo=repo)
            click.secho("Collector settings file created", fg='green')
            no_action = False
        if no_action:
            click.echo('Nothing done')


    @repo_group.command()
    @click.pass_context
    @click.option('--verbose', '-v', help='Verbose output from the collector', is_flag=True)
    @async_command
    async def update(ctx: click.Context, verbose: bool = False):
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
