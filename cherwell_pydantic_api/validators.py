import datetime
from decimal import Decimal
from typing import Any, Callable, Optional

from pydantic import validator  # type: ignore



# TODO: Take locale into account


def validator_datetime_impl(value: str) -> Optional[datetime.datetime]:
    if not value:
        return None
    value = value.replace('/', '.')
    try:
        return datetime.datetime.strptime(value, '%d.%m.%Y %H:%M')
    except:
        pass
    try:
        return datetime.datetime.strptime(value, '%d.%m.%Y %H:%M:%S')
    except:
        pass
    raise ValueError(f"Invalid datetime: {value!r}")

def validator_datetime(*args: str, **kwargs: Any) -> Callable[[Any, str], Optional[datetime.datetime]]:
    return validator(*args, **kwargs)(validator_datetime_impl) # type: ignore


def validator_date_impl(value: str) -> Optional[datetime.date]:
    if not value:
        return None
    value = value.replace('/', '.')
    return datetime.datetime.strptime(value, '%d.%m.%Y').date()

def validator_date(*args: str, **kwargs: Any) -> Callable[[Any, str], Optional[datetime.date]]:
    return validator(*args, **kwargs)(validator_date_impl) # type: ignore


def validator_time_impl(value: str) -> Optional[datetime.time]:
    # TODO: better handling of invalid values
    if not value:
        return None
    try:
        return datetime.datetime.strptime(value, '%H:%M').time()
    except:
        pass
    try:
        return datetime.datetime.strptime(value, '%H:%M:%S').time()
    except:
        pass
    return None

def validator_time(*args: str, **kwargs: Any) -> Callable[[Any, str], Optional[datetime.time]]:
    return validator(*args, **kwargs)(validator_time_impl) # type: ignore


def validator_int_impl(value: str) -> int:
    # TODO: better handling of invalid values
    if '.' in value:
        value = value.split('.')[0]
    return int(value.translate(str.maketrans("',", "__")))

def validator_int(*args: str, **kwargs: Any) -> Callable[[Any, str], int]:
    return validator(*args, **kwargs)(validator_int_impl) # type: ignore


def validator_decimal_impl(value: str) -> Decimal:
    return Decimal(value.translate(str.maketrans("',", "__")))

def validator_decimal(*args: str, **kwargs: Any) -> Callable[[Any, str], Decimal]:
    return validator(*args, **kwargs)(validator_decimal_impl) # type: ignore
