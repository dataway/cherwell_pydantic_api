"""Module for the welcoming initial setup CLI"""
# pyright: reportUnusedImport=false

import time
from pathlib import Path
from typing import Optional

import click
import httpx
try:
    import readline
except:
    pass


def api_detect(urls: list[str]) -> tuple[Optional[str], str, float, bool]:
    "Try to detect the Cherwell API at the given URLs"
    for url in urls:
        try:
            click.secho(
                f"Trying to detect Cherwell API at {url}...", fg='cyan')
            t1 = time.time()
            verify = True
            try:
                response = httpx.get(
                    f"{url}/api/V1/serviceinfo", verify=verify, timeout=(5.0, 60.0, 5.0, 1.0))
            except httpx.ConnectError:
                verify = False
                response = httpx.get(
                    f"{url}/api/V1/serviceinfo", verify=verify, timeout=(5.0, 60.0, 5.0, 1.0))
            t2 = time.time()
            if response.is_success:
                service_info = response.json()
                return (url, service_info.get('apiVersion', 'unknown'), t2 - t1, verify)
            click.secho(
                f"HTTP Error: {response.status_code} {response.reason_phrase}", fg='red')
        except Exception as e:
            click.secho(f"Error: {e}", fg='red')
    return (None, '', 0.0, False)


def initial_setup(envpath: Path) -> None:
    "Create a new cherwell.env file from user input"
    envdict: dict[str, str] = {}
    click.secho("""Enter the API base URL of your Cherwell instance, e.g. https://myinstance.cherwellsoftware.com/CherwellAPI
You can also just enter the hostname or IP address and I will attempt to guess the rest.
If you have multiple instances, set up the development instance first. You can add your production instance later.\n""", fg='green')
    while True:
        api_base_url: Optional[str] = click.prompt('API base URL or host', type=str)
        if not api_base_url:
            continue
        if not api_base_url.startswith('http'):
            urls = [f"https://{api_base_url}/CherwellAPI",
                    f"http://{api_base_url}/CherwellAPI"]
        else:
            urls = [api_base_url]
        api_base_url, api_version, duration, verify = api_detect(urls)
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
        envdict['cherwell_timeout'] = f"{duration * 2}"
    if not verify:
        click.secho(
            f"Warning: SSL certificate verification failed. Connection will be set up with verify=False", fg='red', bg='yellow')
        envdict['cherwell_verify'] = 'off'
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
        click.secho(f"{envpath} created successfully.\n", fg='green')
        click.secho("If you are a first-time user, I recommend the Getting Started JupyterLab notebook.", bg='green', fg='black')
        click.secho("Run it with", nl=False, bg='green', fg='black')
        click.secho(" cwcli getting-started", fg='cyan')

