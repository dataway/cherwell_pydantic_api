from marshmallow import fields
import datetime


def from_cw_datetime(value):
    try:
        return datetime.datetime.strptime(value, '%d.%m.%Y %H:%M')
    except:
        print("Parse error datetime: {0}".format(value.strip()))

def from_cw_date(value):
    try:
        return datetime.datetime.strptime(value, '%d.%m.%Y').date()
    except:
        print("Parse error date: {0}".format(value))


class DateTime(fields.DateTime):
    DESERIALIZATION_FUNCS = fields.DateTime.DESERIALIZATION_FUNCS.copy()
    DESERIALIZATION_FUNCS['cherwell'] = from_cw_datetime
    DEFAULT_FORMAT = 'cherwell'

    def _deserialize(self, value, attr, data, **kwargs):
        if not value:
            return None
        return fields.DateTime._deserialize(self, value, attr, data, **kwargs)


class Date(DateTime):
    DESERIALIZATION_FUNCS = fields.Date.DESERIALIZATION_FUNCS.copy()
    DESERIALIZATION_FUNCS['cherwell'] = from_cw_date
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
