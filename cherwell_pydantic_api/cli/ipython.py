#!/usr/bin/env python3
# pyright: reportUnusedImport=false, reportUnusedFunction=false
# mypy: ignore-errors


from typing import TYPE_CHECKING, Any, Optional

import click



@click.command('ipython', context_settings={'allow_extra_args': True, 'ignore_unknown_options': True}, epilog="Further arguments will be passed to IPython.")
@click.option('--instance-name', '-I', help='The name of the instance to use. If not specified, the default instance will be used.')
@click.option('--quiet', '-q', is_flag=True, help='Suppress most messages')
@click.pass_context
def ipython_shell(ctx: click.Context, instance_name: Optional[str] = None, quiet: bool = False):
    "Start an interactive IPython shell"
    try:
        import IPython
        import traitlets
    except:
        if not quiet:
            click.secho("IPython is not installed", fg='red')
        return

    from cherwell_pydantic_api.bo.modelgen.collector import Collector
    from cherwell_pydantic_api.bo.modelgen.repo import ModelRepo
    from cherwell_pydantic_api.instance import Instance
    from cherwell_pydantic_api.interactive import Interactive
    from cherwell_pydantic_api.settings import Settings

    collector = Collector(Instance.use(instance_name), verbose=True, bo_include_filter=r'(?i)ticket$')
    repo = ModelRepo(create=True)
    try:
        collector.load_settings(repo)
    except:
        pass

    def startup(objs: list[str]) -> Interactive:
        cw = Interactive(instance_name=instance_name,
                         waiter=IPython.get_ipython().loop_runner)  # type: ignore
        if not quiet:
            click.secho('\nWelcome to cherwell_pydantic_api!', fg='cyan')
            click.secho(
                f'Connecting to instance "{cw.instance.settings.name}" at {cw.instance.settings.base_url}...', nl=False, fg='magenta')
        cw.authenticate()
        service_info = cw.get_service_info()
        if not quiet:
            click.secho(' OK', fg='green')
            click.secho(
                f'apiVersion={service_info.apiVersion}, csmVersion={service_info.csmVersion}', fg='cyan')
            click.secho('I have created a ' + click.style('cw', fg='bright_cyan') +
                        ' object for you to use. Type ' + click.style('cw.help', fg='bright_cyan') + ' for details.')
            click.secho('Other useful globals: ' + ', '.join(objs))
        cw.async_wrap(collector=collector)

        class help:
            msg = ["\nGetting started:",
                   "> " + click.style("cw.collector.collect()", fg='cyan') + " - collect some business object IDs; this fills cw.bo",
                   "> " + click.style("[bo for bo in cw.bo.keys()]", fg='cyan') + " - list the business objects collected",
                   "Suppose this list includes 'ticket'. Then:",
                   "> " + click.style("cw.bo.ticket.get('20220707-1452')", fg='cyan') + " - get a ticket by its public ID",
                   ]

            def _ipython_display_(self):
                click.secho('\n'.join(self.msg))

        cw.help = help()
        return cw

    # Create a namespace for the shell
    ns: dict[str, Any] = {}
    for name, obj in locals().items():
        if not (name.startswith('_') or name in ('ctx', 'IPython', 'traitlets', 'quiet', 'ns')):
            ns[name] = obj
    ns['click'] = click
    ns['object_help'] = [k for k in ns.keys() if k not in ('object_help', 'startup')]
    ns['object_help'].sort()
    config = traitlets.config.Config()  # type: ignore
    config.InteractiveShellApp.exec_lines = [  # type: ignore
        "cw = startup(object_help)",
        "del startup",
        "del object_help",
    ]
    if quiet:
        config.InteractiveShellApp.display_banner = False  # type: ignore
    IPython.start_ipython(config=config, user_ns=ns, argv=ctx.args)  # type: ignore



if __name__ == '__main__':
    ipython_shell()
