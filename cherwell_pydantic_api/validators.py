import datetime
from decimal import Decimal, InvalidOperation
from typing import Any, Callable, Optional, Union

from pydantic import validator  # type: ignore



# TODO: Take locale into account


def validator_datetime_impl(value: Union[str, datetime.datetime]) -> Optional[datetime.datetime]:
    if not value:
        return None
    if isinstance(value, datetime.datetime):
        return value
    value = value.replace('/', '.')
    try:
        return datetime.datetime.strptime(value, '%m.%d.%Y %I:%M %p')
    except:
        pass
    try:
        return datetime.datetime.strptime(value, '%m.%d.%Y %I:%M:%S %p')
    except:
        pass
    raise ValueError(f"Invalid datetime: {value!r}")

def validator_datetime(*args: str, **kwargs: Any) -> Callable[[Any, str], Optional[datetime.datetime]]:
    return validator(*args, **kwargs)(validator_datetime_impl) # type: ignore


def validator_date_impl(value: Union[str, datetime.datetime, datetime.date]) -> Optional[datetime.date]:
    if not value:
        return None
    if isinstance(value, datetime.date):
        return value
    if isinstance(value, datetime.datetime):
        return value.date()
    value = value.replace('/', '.')
    return datetime.datetime.strptime(value, '%m.%d.%Y').date()

def validator_date(*args: str, **kwargs: Any) -> Callable[[Any, str], Optional[datetime.date]]:
    return validator(*args, **kwargs)(validator_date_impl) # type: ignore


def validator_time_impl(value: Union[str, datetime.datetime, datetime.time]) -> Optional[datetime.time]:
    # TODO: better handling of invalid values
    if not value:
        return None
    if isinstance(value, datetime.time):
        return value
    if isinstance(value, datetime.datetime):
        return value.time()
    try:
        return datetime.datetime.strptime(value, '%I:%M %p').time()
    except:
        pass
    try:
        return datetime.datetime.strptime(value, '%I:%M:%S %p').time()
    except:
        pass
    return None

def validator_time(*args: str, **kwargs: Any) -> Callable[[Any, str], Optional[datetime.time]]:
    return validator(*args, **kwargs)(validator_time_impl) # type: ignore


def validator_int_impl(value: Any) -> int:
    # TODO: better handling of invalid values
    try:
        if '.' in value:
            value = value.split('.')[0]
        value = value.translate(str.maketrans("',", "__"))
    except:
        pass
    return int(value)

def validator_int(*args: str, **kwargs: Any) -> Callable[[Any, str], int]:
    return validator(*args, **kwargs)(validator_int_impl) # type: ignore


def validator_decimal(*args: str, decimal_places: int, **kwargs: Any) -> Callable[[Any, str], Optional[Decimal]]:
    def v(value: Any) -> Optional[Decimal]:
        if not value:
            return None
        try:
            value = value.translate(str.maketrans("',", "__"))
        except:
            pass
        try:
            return Decimal(value).quantize(Decimal(f'0.{"0" * decimal_places}'))
        except InvalidOperation as e:
            # pydantic expects a ValueError
            raise ValueError from e
    return validator(*args, **kwargs)(v) # type: ignore
