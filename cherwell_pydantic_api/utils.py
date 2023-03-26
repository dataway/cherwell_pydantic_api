from typing import Any, Callable
from cherwell_pydantic_api.types import FieldID



def fieldid_parts(field_id: str) -> dict[str, str]:
    """The fieldId has the format: 'BO:947dfef9ae6b072ca567a444dca79d9f9ea47a112f,FI:9492462c89a8f7785f1537412ca51a2f218293edb0,RE:9492535dfbf4286b49047f45bab2f201737e739a46'
    This method returns a dict with the keys 'BO', 'FI', 'RE', etc. and the values are the corresponding IDs."""
    r = {}
    for part in field_id.split(','):
        k, v = part.split(':', 1)
        assert k in ('BO', 'FI', 'RE')
        r[k.upper()] = FieldID(v)
    return r


def docwraps(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator to copy the docstring from the wrapped function to the wrapper function."""
    def wrapper(wrapper_func: Callable[..., Any]) -> Callable[..., Any]:
        if wrapper_func.__doc__ is None:
            wrapper_func.__doc__ = f"Wraps {func.__qualname__}"
        else:
            wrapper_func.__doc__ += f"\nWraps {func.__qualname__}"
        if func.__doc__ is not None:
            wrapper_func.__doc__ += ":\n" + func.__doc__
        return wrapper_func
    return wrapper
