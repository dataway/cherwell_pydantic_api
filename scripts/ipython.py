#!/usr/bin/env python3

from typing import TYPE_CHECKING

import IPython
import traitlets



def ipython_shell():
    import cherwell_pydantic_api
    from cherwell_pydantic_api.settings import Settings
    from cherwell_pydantic_api.instance import Instance
    from cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts import (
        BusinessObject,
        Core,
        Searches,
    )

    _cfg = traitlets.config.Config() # type: ignore
    _cfg.InteractiveShellApp.exec_lines = [
        "cw_inst = Instance.use()",
        "await cw_inst.authenticate()",
        "await cw_inst.get_bo_schema(busobname='Ticket')",
    ]
    IPython.start_ipython(config=_cfg, user_ns=locals())
    
    if TYPE_CHECKING:
        cherwell_pydantic_api # type: ignore
        Core # type: ignore
        BusinessObject # type: ignore
        Searches # type: ignore
        Settings # type: ignore
        Instance # type: ignore


if __name__ == '__main__':
    ipython_shell()
