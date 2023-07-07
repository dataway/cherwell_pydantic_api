#!/usr/bin/env python
# pyright: reportUnusedImport=false, reportGeneralTypeIssues=false

import sys
from pathlib import Path

from click import Context



if sys.version_info < (3, 9):
    sys.stderr.write("Python 3.9 or higher is required.")
    sys.exit(1)
try:
    import cherwell_pydantic_api
    from cherwell_pydantic_api.settings import Settings
except ImportError as e:
    sys.stderr.write(
        "cherwell_pydantic_api is not installed properly as a package. Please check the documentation.")
    sys.stderr.write(f"Error: {e}")
    sys.exit(1)
try:
    import click
except ImportError:
    sys.stderr.write("""To use the CLI, click must be installed.
One way of achieving this is to install cherwell_pydantic_api with the modelgen or all extra.
But you can also install click separately.

To fix this, run pip or poetry as follows:
    pip install cherwell_pydantic_api[modelgen]
or
    pip install cherwell_pydantic_api[all]
or
    poetry add -E modelgen cherwell_pydantic_api
or
    poetry add -E all cherwell_pydantic_api

""")
    sys.exit(1)


def check_envpath(offer_setup: bool = True) -> Path:
    envpath = Path.cwd().joinpath('cherwell.env')
    if not envpath.exists():
        click.secho(
            f"\nNo cherwell.env file found in the current path, {Path.cwd()}.\nYou can now create one, or press Ctrl+C to abort.\n", fg='yellow')
        from .welcome import initial_setup
        initial_setup(envpath)
    return envpath


def welcome_banner():
    click.echo()
    lines = ['Welcome to cherwell_pydantic_api!', '', 'For more information, please visit:',
             '', 'https://github.com/dataway/cherwell_pydantic_api']
    width = max([len(line) for line in lines])
    hash = '\u2592'
    style = {'fg': 'white', 'bg': 'blue'}
    click.secho(hash * (width + 6), **style)
    for line in lines:
        click.secho(
            f"{hash}  {line}{' ' * (width - len(line))}  {hash}", **style)
    click.secho(hash * (width + 6), **style)
    click.echo()



def cli_welcome():
    "Check for existing env file and offer to create one if not found. Return 0 if successful, 1 if aborted."
    try:
        settings = Settings()
    except:
        settings = None
    if settings is None or not settings.suppress_banner:
        welcome_banner()

    try:
        envpath = check_envpath()
    except click.exceptions.Abort:
        click.secho("\nAborted.\n", fg='red')
        return 1
    if settings is None or not settings.suppress_banner:
        click.secho(
            f"\nFound existing cherwell.env file at {envpath}\n", fg='green')
    return 0


@click.group
def root():
    "cherwell_pydantic_api CLI"
    pass


@root.command(context_settings=dict(ignore_unknown_options=True, allow_extra_args=True))
@click.pass_context
def getting_started(ctx: Context):
    "Launch the Getting Started notebook in JupyterLab"
    try:
        import jupyterlab.labapp  # type: ignore
    except:
        click.secho(
            "To use the JupyterLab interface, you must install cherwell_pydantic_api[all].\n", fg='red')
        return
    import os.path
    nb = os.path.dirname(__file__) + '/../examples/GettingStarted.ipynb'
    jupyterlab.labapp.main(ctx.args + [nb]) # type: ignore


def cli_normal():
    from . import check
    root.add_command(check.check)
    from . import ipython
    root.add_command(ipython.ipython_shell)
    from . import repo
    root.add_command(repo.repo_group)
    root()


def cli():
    "Main CLI entry point."
    if len(sys.argv) == 1:  # No CLI arguments
        r = cli_welcome()
        if r != 0:
            return r
    return cli_normal()


if __name__ == '__main__':
    cli()
