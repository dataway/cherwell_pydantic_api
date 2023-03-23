
from collections import defaultdict
from typing import Any, Optional, cast

import black
from jinja2 import Environment, PackageLoader, select_autoescape

from cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject import FieldDefinition
from cherwell_pydantic_api.bo.valid_schema import ValidSchema
from cherwell_pydantic_api.settings import InstanceSettingsBase, Settings
from cherwell_pydantic_api.utils import fieldid_parts



class ParsedFieldDefinition(FieldDefinition):
    python_type: str = 'Any'
    python_type_modules: set[str] = set()
    python_type_validator: Optional[str] = None
    pydantic_field_args: dict[str, Any] = {}
    fieldId: str  # override Optional[str] with str

    @property
    def pydantic_field_params(self) -> str:
        return ', '.join([f'{k}={v}' for k, v in self.pydantic_field_args.items()])

    @property
    def fieldid_parts(self) -> dict[str, str]:
        return fieldid_parts(self.fieldId)

    def resolve_type(self):
        if self.type == 'Text':
            self.python_type = 'str'
            if self.maximumSize:
                try:
                    self.pydantic_field_args['max_length'] = int(
                        self.maximumSize)
                except:
                    pass
        elif self.type == 'DateTime':
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
                self.python_type_validator = 'validator_int'
            else:
                self.python_type = 'decimal.Decimal'
                self.python_type_validator = 'validator_decimal'
                self.python_type_modules.add('decimal')
                self.pydantic_field_args['decimal_places'] = self.decimalDigits
                if self.wholeDigits:
                    self.pydantic_field_args['max_digits'] = self.wholeDigits + cast(int, self.decimalDigits)
        elif self.type == 'Logical':
            self.python_type = 'bool'
        else:
            raise ValueError(
                f"Unknown type: {self.type} for field {self.name}")
        if not self.required:
            self.python_type = f"Optional[{self.python_type}]"



class PydanticModelGenerator:
    def __init__(self, instance_settings: InstanceSettingsBase):
        self._instance_settings = instance_settings
        self._jinja_env = Environment(loader=PackageLoader('cherwell_pydantic_api.bo', 'templates'),
                                      autoescape=select_autoescape(['py']), trim_blocks=True, lstrip_blocks=True)

    def generate_base(self) -> str:
        template = self._jinja_env.get_template('base.py.j2')
        base_str = template.render(settings=self._instance_settings)
        base_str = black.format_str(base_str, mode=black.FileMode(preview=True))
        return base_str

    def generate_model(self, schema: ValidSchema) -> str:
        template = self._jinja_env.get_template('model.py.j2')
        fields = [ParsedFieldDefinition(**field.dict())
                  for field in schema.fieldDefinitions]
        modules = set()
        validators = defaultdict(list)
        for field in fields:
            field.resolve_type()
            if field.python_type_modules:
                modules.update(field.python_type_modules)
            if field.python_type_validator:
                validators[field.python_type_validator].append(field)
            assert field.fieldid_parts['BO'] == schema.busObId
        model_str = template.render(schema=schema, fields=fields, modules=modules, validators=validators, settings=self._instance_settings)
        model_str = black.format_str(model_str, mode=black.FileMode(preview=True))
        return model_str
