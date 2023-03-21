#!/usr/bin/env python3

from typing import TYPE_CHECKING

import traitlets



def ipython_shell():
    import IPython
    import cherwell_pydantic_api
    import logging
    from cherwell_pydantic_api.settings import Settings
    from cherwell_pydantic_api.instance import Instance
    from cherwell_pydantic_api.interactive import Interactive
    from cherwell_pydantic_api.bo.modelgen.repo import ModelRepo
    from cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts import (
        BusinessObject,
        Core,
        Searches,
    )

    logger = logging.getLogger(None)
    logger.setLevel(logging.INFO)

    _cfg = traitlets.config.Config()  # type: ignore
    _cfg.InteractiveShellApp.exec_lines = [
        "repo = ModelRepo(create=True)",
        "cw = Interactive(waiter=IPython.get_ipython().loop_runner)",
        "cw.authenticate()",
        "cw.get_bo_schema(busobname='Ticket')",
    ]
    IPython.start_ipython(config=_cfg, user_ns=locals())

    if TYPE_CHECKING:
        cherwell_pydantic_api  # type: ignore
        Core  # type: ignore
        BusinessObject  # type: ignore
        Searches  # type: ignore
        Settings  # type: ignore
        Instance  # type: ignore
        Interactive  # type: ignore
        ModelRepo  # type: ignore


if __name__ == '__main__':
    ipython_shell()
