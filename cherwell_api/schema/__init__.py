
import sys
import importlib.abc
import importlib.machinery
import types
from typing import Any, Callable, List, Optional, Sequence, Tuple, Union
from marshmallow import Schema, pre_load, post_load, post_dump, fields as marshmallow_fields
import pprint



class TypeHandler(object):
    """docstring for TypeHandler"""
    def __init__(self, schema, marshmallow_fields='fields', cherwell_fields='cherwell_fields'):
        super(TypeHandler, self).__init__()
        self.schema = schema
        self.marshmallow_fields = marshmallow_fields
        self.cherwell_fields = cherwell_fields

    def resolve(self, field):
        bo_type = field['type']
        ftype = self.marshmallow_fields + '.Str'
        args = []
        if bo_type == 'Text':
            ftype = self.marshmallow_fields + '.Str'
        elif bo_type == 'Number':
            if not field['decimalDigits']:
                ftype = self.cherwell_fields + '.Int'
            else:
                ftype = self.cherwell_fields + '.Decimal'
                args.append('places={0[decimalDigits]}'.format(field))
                args.append('as_string=True')
        elif bo_type == 'DateTime':
            if field['hasDate'] and field['hasTime']:
                ftype = self.cherwell_fields + '.DateTime'
            elif field['hasDate']:
                ftype = self.cherwell_fields + '.Date'
            elif field['hasTime']:
                ftype = self.cherwell_fields + '.Time'
        elif bo_type == 'Logical':
                ftype = self.marshmallow_fields + '.Bool'
        if field['required']:
            args.append('required=True')
        return ftype + '(' + ','.join(args) + ')'



class BusinessObjectDict(dict):
    __slots__ = ['busObId', 'busObPublicId', 'busObRecId', 'fieldIds', 'html', 'schema', 'dirty']

    def __init__(self, schema):
        self.schema = schema
        self.busObId = self.busObPublicId = self.busObRecId = None
        self.fieldIds = {}
        self.html = {}
        self.dirty = []

    def set_dirty(self, key):
        if key in self.dirty:
            self.dirty.remove(key)
        self.dirty.append(key)
        return key

    def clear_dirty(self):
        self.dirty = []

    def __setitem__(self, key, value):
        if key not in self or self[key] != value:
            self.set_dirty(key)
        dict.__setitem__(self, key, value)
        if key in self.html:
            del self.html[key]

    def set_html(self, key, html):
        if key not in self.html or self.html[key] != html:
            self.set_dirty(key)
        self.html[key] = html
        dict.__setitem__(self, key, html)

    def save_change(self):
        if not self.dirty:
            return None
        return type(self.schema)(only=self.dirty).dump(self)



class BusinessObjectSchema(Schema):

    def make_empty(self):
        r = BusinessObjectDict(self)
        r.busObId = self._busObId
        r.fieldIds = self._field_name_to_long_id
        return r

    @pre_load(pass_many=True)
    def unpack(self, data, many, **kwargs):
        fields_hash = dict()
        if data is not None:
            for field in data['fields']:
                fields_hash[field['name']] = field['value']
        return fields_hash

    @post_load(pass_many=True, pass_original=True)
    def make_bo_dict(self, data, original, **kwargs):
        r = BusinessObjectDict(self)
        for k, v in data.items():
            r[k] = v
        if original is not None:
            for field in original['fields']:
                r.fieldIds[field['name']] = field['fieldId']
                if field['html'] is not None:
                    r.html[field['name']] = field['html']
            r.busObId = original['busObId']
            r.busObPublicId = original['busObPublicId']
            r.busObRecId = original['busObRecId']
        r.clear_dirty()
        return r


    @post_dump(pass_many=True, pass_original=True)
    def dump_bo_dict(self, data, original, **kwargs):
        fields = []
        r = {'busObId': original.busObId, 'persist': True, 'fields': fields}
        if original.busObRecId is not None:
            r['busObRecId'] = original.busObRecId
        # First enumerate dirty fields in order of setting them
        for field in original.dirty:
            value = data[field]
            f = { 'dirty': True, 'fieldId': original.fieldIds[field] }
            if field in original.html:
                f['html'] = original.html[field]
                f['value'] = original.html[field]
            else:
                f['value'] = value
            f['name'] = field
            fields.append(f)
        # Then add non-dirty fields
        for field, value in data.items():
            if field in original.dirty:
                continue
            f = { 'dirty': False, 'fieldId': original.fieldIds[field] }
            if field in original.html:
                f['html'] = original.html[field]
                f['value'] = original.html[field]
            else:
                f['value'] = value
            f['name'] = field
            fields.append(f)
        return r



class BusinessObjectBuilder(object):
    """docstring for BusinessObjectBuilder"""
    def __init__(self, connection, path, type_handler_class=TypeHandler):
        super(BusinessObjectBuilder, self).__init__()
        self.connection = connection
        self.path = path
        self.type_handler_class = type_handler_class


    def build_object(self, busObName, type_handler_class=None):
        if type_handler_class is None:
            type_handler_class = self.type_handler_class
        lines = ['# Auto-generated file. Do not edit!',
                 '###################################',
                 '',
                 'from marshmallow import fields',
                 'from {0} import BusinessObjectSchema'.format(__name__),
                 'from {0} import fields as cherwell_fields'.format(__name__),
                 '']
        schema = self.connection.get_bo_schema(busObName = busObName, relationships=True)
        self.last_schema = schema
        type_handler = type_handler_class(schema)
        field_id_to_name = dict()
        field_name_to_long_id = dict()
        lines.append(
r"""class {0[name]}Schema(BusinessObjectSchema):
    _busObId = '{0[busObId]}'
    _stateFieldId = '{0[stateFieldId]}'""".format(schema))
        for field in schema['fieldDefinitions']:
            mtype = type_handler.resolve(field)
            description = field['description'].replace('\n', '').strip()
            if description:
                lines.append('    #{0}'.format(description))
            lines.append('    {0[name]} = {1}'.format(field, mtype))
            field_name_to_long_id[field['name']] = field['fieldId']
            field_id_parts = dict()
            for field_id_part in field['fieldId'].split(','):
                k, v = field_id_part.split(':', 1)
                field_id_parts[k] = v
            if field_id_parts.get('BO', '') == schema['busObId']:
                field_id_to_name[field_id_parts.get('FI', '')] = field['name']
        if schema['states'] is not None:
            lines.append('    _states = ' + repr(schema['states'].split(',')))

        if field_id_to_name:
            lines.append('    _first_rec_id_field = {0}'.format(field_id_to_name[schema['firstRecIdField']]))
            if 'stateFieldId' in schema and schema['stateFieldId'] in field_id_to_name:
                lines.append('    _state_field = {0}'.format(field_id_to_name[schema['stateFieldId']]))
            lines.append('    _field_id_to_name = ' + pprint.pformat(field_id_to_name, indent=8, width=160))
        lines.append('    _field_name_to_long_id = ' + pprint.pformat(field_name_to_long_id, indent=8, width=160))
        lines.append('')
        for relationship in schema['relationships']:
            pass

        lines.append('r"""')
        lines.append(pprint.pformat(schema, width=240))
        lines.append('r"""')
        f = open('{0}/{1}.py'.format(self.path, busObName), 'w')
        for line in lines:
            f.write(line + '\n')
        f.close()
        return lines



class CherwellSchemaMetaPathFinder(importlib.abc.MetaPathFinder):
    """docstring for CherwellSchemaMetaPathFinder"""
    def __init__(self):
        super(CherwellSchemaMetaPathFinder, self).__init__()
        self.schemas = dict()
        
    @classmethod
    def find_spec(cls, fullname: str, path: Optional[Sequence[str]], target: Optional[types.ModuleType] = ...) -> Optional[object]:
        if fullname.startswith(cls.__module__ + '.'):
            print("fullname: {0}".format(fullname))
            schema = fullname[len(cls.__module__) + 1:]
            if '.' in schema:
                schema, ob = schema.split('.')
            else:
                ob = None
            print("find_spec: {0}.{1}, {2}, {3}".format(schema, ob, path, target))
            bob = meta_path_finder.schemas.get(schema, None)
            if bob is None:
                return None
            if ob is None:
                spec = importlib.machinery.ModuleSpec(fullname, None, is_package=True)
                print("spec:{0}".format(spec))
                return spec
            bob.build_object(ob)
            loader = importlib.machinery.SourceFileLoader(fullname, '{0}/{1}.py'.format(bob.path, ob))
            spec = importlib.machinery.ModuleSpec(fullname, loader)
            return spec
        return None

    def register_schema(self, name, bob):
        self.schemas[name] = bob


def _append_meta_path():
    for m in sys.meta_path:
        if isinstance(m, CherwellSchemaMetaPathFinder):
            return m
    m = CherwellSchemaMetaPathFinder()
    sys.meta_path.append(m)
    return m

meta_path_finder = _append_meta_path()

