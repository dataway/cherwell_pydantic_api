from marshmallow import fields
import datetime
import re


def from_cw_datetime(value):
    value = value.replace('/', '.')
    try:
        return datetime.datetime.strptime(value, '%d.%m.%Y %H:%M')
    except:
        pass
    return datetime.datetime.strptime(value, '%d.%m.%Y %H:%M:%S')

def from_cw_date(value):
    value = value.replace('/', '.')
    return datetime.datetime.strptime(value, '%d.%m.%Y').date()

def to_cw_datetime(value):
    return value.strftime('%d/%m/%Y %H:%M')

def to_cw_date(value):
    return value.strftime('%d/%m/%Y')



class DateTime(fields.DateTime):
    DESERIALIZATION_FUNCS = fields.DateTime.DESERIALIZATION_FUNCS.copy()
    DESERIALIZATION_FUNCS['cherwell'] = from_cw_datetime
    SERIALIZATION_FUNCS = fields.DateTime.SERIALIZATION_FUNCS.copy()
    SERIALIZATION_FUNCS['cherwell'] = to_cw_datetime
    DEFAULT_FORMAT = 'cherwell'

    def _deserialize(self, value, attr, data, **kwargs):
        if not value:
            return None
        return fields.DateTime._deserialize(self, value, attr, data, **kwargs)


class Date(DateTime):
    DESERIALIZATION_FUNCS = fields.Date.DESERIALIZATION_FUNCS.copy()
    DESERIALIZATION_FUNCS['cherwell'] = from_cw_date
    SERIALIZATION_FUNCS = fields.Date.SERIALIZATION_FUNCS.copy()
    SERIALIZATION_FUNCS['cherwell'] = to_cw_date
    DEFAULT_FORMAT = 'cherwell'
    OBJ_TYPE = 'date'


class Time(fields.Time):
    def _deserialize(self, value, attr, data, **kwargs):
        if not value:
            return None
        return fields.Time._deserialize(self, value, attr, data, **kwargs)


class Int(fields.Int):
    _map = str.maketrans("',", "__")
    def _deserialize(self, value, attr, data, **kwargs):
        if not value:
            return None
        value = value.translate(self._map)
        return fields.Int._deserialize(self, value, attr, data, **kwargs)


class Decimal(fields.Decimal):
    _map = str.maketrans("',", "__")
    def _deserialize(self, value, attr, data, **kwargs):
        if not value:
            return None
        value = value.translate(self._map)
        return fields.Int._deserialize(self, value, attr, data, **kwargs)
