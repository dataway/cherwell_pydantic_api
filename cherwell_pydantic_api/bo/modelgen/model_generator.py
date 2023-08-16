from collections import defaultdict
from typing import Any, Optional, cast

import black
from jinja2 import Environment, PackageLoader, select_autoescape

from cherwell_pydantic_api.bo.valid_schema import ValidFieldDefinition, ValidSchema
from cherwell_pydantic_api.instance import Instance
from cherwell_pydantic_api.types import FieldIdentifier, ShortFieldID
from cherwell_pydantic_api.utils import fieldid_parts



class ParsedFieldDefinition(ValidFieldDefinition):
    python_type: str = 'Any'
    python_default: str = 'None'
    python_type_modules: set[str] = set()
    python_type_validator: Optional[str] = None
    python_validator_params: Any = None
    pydantic_field_args: dict[str, Any] = {}

    @property
    def pydantic_field_params(self) -> str:
        return ', '.join([f'{k}={v}' for k, v in self.pydantic_field_args.items()])

    def resolve_type(self):
        if self.type == 'Text':
            self.python_type = 'str'
            self.python_default = "''"
            if self.maximumSize:
                try:
                    self.pydantic_field_args['max_length'] = int(
                        self.maximumSize)
                except:
                    pass
        elif self.type == 'DateTime':
            self.python_default = "datetime.datetime(1, 1, 1)"
            self.python_type_modules.add('datetime')
            if self.hasDate and self.hasTime:
                self.python_type = 'datetime.datetime'
                self.python_type_validator = 'validator_datetime'
            elif self.hasDate:
                self.python_type = 'datetime.date'
                self.python_type_validator = 'validator_date'
            elif self.hasTime:
                self.python_type = 'datetime.time'
                self.python_type_validator = 'validator_time'
            else:
                self.python_type = 'datetime.datetime'
                self.python_type_validator = 'validator_datetime'
        elif self.type == 'Number':
            if self.decimalDigits == 0:
                self.python_type = 'int'
                self.python_default = "0"
                self.python_type_validator = 'validator_int'
            else:
                self.python_type = 'decimal.Decimal'
                self.python_default = "decimal.Decimal()"
                self.python_type_validator = 'validator_decimal'
                self.python_validator_params = self.decimalDigits
                self.python_type_modules.add('decimal')
                self.pydantic_field_args['decimal_places'] = self.decimalDigits
                if self.wholeDigits:
                    self.pydantic_field_args['max_digits'] = self.wholeDigits + \
                        cast(int, self.decimalDigits)
        elif self.type == 'Logical':
            self.python_type = 'bool'
            self.python_default = "False"
        else:
            raise ValueError(
                f"Unknown type: {self.type} for field {self.name}")
        if not self.required or (self.details and 'Conditionally Required' in self.details):
            # Pydantic v2 requires this workaround per https://github.com/pydantic/pydantic/issues/6955
            if self.python_type in ('decimal.Decimal',):
                self.python_type = f"Annotated[{self.python_type}, Field({self.pydantic_field_params})]"
                self.pydantic_field_args = {}
            self.python_type = f"Optional[{self.python_type}]"
            self.python_default = 'None'



class PydanticModelGenerator:
    def __init__(self, instance: Instance):
        self._instance = instance
        self._jinja_env = Environment(loader=PackageLoader('cherwell_pydantic_api.bo', 'templates'),
                                      autoescape=select_autoescape(['py']), trim_blocks=True, lstrip_blocks=True)
        self._jinja_env.filters['repr'] = repr  # type: ignore

    def generate_base(self) -> str:
        template = self._jinja_env.get_template('base.py.j2')
        base_str = template.render(settings=self._instance.settings)
        base_str = black.format_str(
            base_str, mode=black.FileMode(preview=True))
        return base_str

    def generate_model(self, schema: ValidSchema) -> str:
        template = self._jinja_env.get_template('model.py.j2')
        modules: set[str] = set()
        validators: dict[tuple[str, ...], list[ParsedFieldDefinition]] = defaultdict(list)
        statefield: Optional[str] = None
        firstrecfield: Optional[str] = None
        fields: list[ParsedFieldDefinition] = []
        all_fields: list[ParsedFieldDefinition] = []
        parent_schema_fields: dict[ShortFieldID, ValidFieldDefinition] = {}
        if schema.parentSchema:
            parent_schema_fields = {field.short_field_id: field for field in schema.parentSchema.fieldDefinitions}
        for valid_field in schema.fieldDefinitions:
            field = ParsedFieldDefinition(**valid_field.model_dump())
            field.resolve_type()
            if field.short_field_id == schema.stateFieldId:
                statefield = FieldIdentifier(field.name)
            if field.short_field_id == schema.firstRecIdField:
                firstrecfield = FieldIdentifier(field.name)
            if field.python_type_validator:
                validators[(field.python_type_validator, field.python_validator_params)].append(field)
            assert fieldid_parts(field.fieldId)['BO'] == schema.busObId
            if field.python_type_modules:
                modules.update(field.python_type_modules)
            all_fields.append(field)
            if valid_field.short_field_id in parent_schema_fields:
                continue
                # parent_field = parent_fields[valid_field.short_field_id]
                # TODO: Unclear which aspects of the field are allowed to differ from the parent. For now, don't check anything.
                # The following list of attributes were observed to differ
                # mismatches = {k: (v, getattr(parent_field, k))
                #              for k, v in vars(valid_field).items()
                #              if v != getattr(parent_field, k) and k not in (
                #                 'fieldId', 'details', 'autoFill', 'readOnly', 'validated', 'category',
                #                 'displayName', 'description', 'required', 'calculated')}
                # if mismatches:
                #    raise ValueError(
                #        f"Field {field.name} of {schema.identifier} has mismatches with parent: {mismatches}")
            fields.append(field)
        model_str = template.render(schema=schema, fields=fields, all_fields=all_fields,
                                    modules=modules, validators=validators, settings=self._instance.settings,
                                    statefield=statefield, firstrecfield=firstrecfield)
        model_str = black.format_str(
            model_str, mode=black.FileMode(preview=True))
        return model_str
