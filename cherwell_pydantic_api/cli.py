#!/usr/bin/env python
"""Basic CLI for cherwell_pydantic_api package"""


from cgi import print_form
import sys

from cherwell_pydantic_api import api
if sys.version_info < (3, 9):
    sys.stderr.write("Python 3.9 or higher is required.")
    sys.exit(1)
try:
    import cherwell_pydantic_api
except ImportError:
    sys.stderr.write(
        "cherwell_pydantic_api is not installed properly. Please check the documentation.")
    sys.exit(1)
try:
    import click
except ImportError:
    sys.stderr.write("""cherwell_pydantic_api must be installed with the modelgen option.

To fix this, run pip or poetry as follows:
    pip install cherwell_pydantic_api[modelgen]
    poetry add -E modelgen cherwell_pydantic_api

""")
    sys.exit(1)
from pathlib import Path
from getpass import getpass
import httpx
import time
try:
    import readline
except:
    pass


def api_detect(urls):
    for url in urls:
        try:
            click.secho(
                f"Trying to detect Cherwell API at {url}...", fg='cyan')
            t1 = time.time()
            response = httpx.get(
                f"{url}/api/V1/serviceinfo", verify=False, timeout=(5.0, 60.0, 5.0, 1.0))
            t2 = time.time()
            if response.is_success:
                service_info = response.json()
                return (url, service_info.get('apiVersion', 'unknown'), t2 - t1)
            click.secho(
                f"HTTP Error: {response.status_code} {response.reason_phrase}", fg='red')
        except Exception as e:
            click.secho(f"Error: {e}", fg='red')
    return (None, None, 0.0)


def initial_setup(envpath: Path):
    envdict = {}
    click.secho("""Enter the API base URL of your Cherwell instance, e.g. https://myinstance.cherwellsoftware.com/CherwellAPI
You can also just enter the hostname or IP address and I will attempt to guess the rest.
If you have multiple instances, set up the development instance first. You can add your production instance later.\n""", fg='green')
    while True:
        api_base_url = click.prompt('API base URL or host', type=str)
        if not api_base_url:
            continue
        if not api_base_url.startswith('http'):
            urls = [f"https://{api_base_url}/CherwellAPI",
                    f"http://{api_base_url}/CherwellAPI"]
        else:
            urls = [api_base_url]
        api_base_url, api_version, duration = api_detect(urls)
        if api_base_url is not None:
            break
        click.secho(
            f"No API found. Please check your URL and network connectivity.", fg='red')
    click.secho(
        f"Success! Cherwell API version {api_version} found at {api_base_url}", bg='green', fg='black')
    envdict['cherwell_base_url'] = api_base_url
    duration = round(duration, 1)
    if duration > 5.0:
        click.secho(f"Warning: The API took {duration} seconds to respond. I will configure a timeout of {duration*2} seconds.", fg='yellow')
        envdict['cherwell_timeout'] = duration * 2
    click.echo(f"""
You can now enter your client ID, username and password. You can also leave these blank and configure them later,
however you won't be able to use the API until you do. Contact your Cherwell administrator if you don't have these details.
""")
    envdict['cherwell_client_id'] = click.prompt(
        'Client ID', type=str, default='')
    envdict['cherwell_username'] = click.prompt(
        'Username', type=str, default='')
    envdict['cherwell_password'] = click.prompt(
        'Password', type=str, default='')

    click.echo('Would you like to create the file ', nl=False)
    click.secho(f"{envpath}", fg='cyan', nl=False)
    click.echo(' with the above settings?')
    if click.confirm('Create file?', default=None):
        envpath.write_text(''.join([f"{k}={v}\n" for k, v in envdict.items()]))
        click.secho(f"{envpath} created successfully:", fg='green')



def cli():
    envpath = Path.cwd().joinpath('cherwell.env')
    if not envpath.exists():
        click.secho(
            f"\nNo cherwell.env file found in the current path, {Path.cwd()}.\nYou can now create one, or press Ctrl+C to abort.\n", fg='yellow')
        initial_setup(envpath)


if __name__ == '__main__':
    cli()
