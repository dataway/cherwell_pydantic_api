import datetime
from decimal import Decimal
from typing import Optional



# TODO: Take locale into account


def validator_datetime(value: str) -> Optional[datetime.datetime]:
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


def validator_date(value: str) -> Optional[datetime.date]:
    if not value:
        return None
    value = value.replace('/', '.')
    return datetime.datetime.strptime(value, '%d.%m.%Y').date()


def validator_time(value: str) -> Optional[datetime.time]:
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


def validator_int(value: str) -> int:
    # TODO: better handling of invalid values
    if '.' in value:
        value = value.split('.')[0]
    return int(value.translate(str.maketrans("',", "__")))


def validator_decimal(value: str) -> Decimal:
    return Decimal(value.translate(str.maketrans("',", "__")))
