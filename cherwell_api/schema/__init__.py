
import sys
import importlib.abc
import importlib.machinery
import types
from typing import Any, Callable, List, Optional, Sequence, Tuple, Union
from marshmallow import Schema, pre_load, fields as marshmallow_fields
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
                ftype = self.marshmallow_fields + '.Decimal'
                args.append('places={0[decimalDigits]}'.format(field))
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



class BusinessObjectSchema(Schema):

    @pre_load(pass_many=True)
    def unpack(self, data, many, **kwargs):
        fields_hash = dict()
        for field in data['fields']:
            fields_hash[field['name']] = field['value']
        return fields_hash


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
                 'from cherwell_api.schema import BusinessObjectSchema',
                 'from cherwell_api.schema import fields as cherwell_fields',
                 '']
        schema = self.connection.get_bo_schema(busObName = busObName, relationships=True)
        self.last_schema = schema
        type_handler = type_handler_class(schema)
        field_id_to_name = dict()
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

