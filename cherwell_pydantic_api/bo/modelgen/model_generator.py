
from typing import Any, Optional

import black
from jinja2 import Environment, PackageLoader, select_autoescape

from cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject import FieldDefinition
from cherwell_pydantic_api.bo.valid_schema import ValidSchema
from cherwell_pydantic_api.settings import InstanceSettingsBase, Settings



class ParsedFieldDefinition(FieldDefinition):
    python_type: str = 'Any'
    python_type_module: Optional[str] = None
    pydantic_field_args: dict[str, Any] = {}
    fieldId: str  # override Optional[str] with str

    @property
    def pydantic_field_params(self) -> str:
        return ', '.join([f'{k}={v}' for k, v in self.pydantic_field_args.items()])

    @property
    def fieldid_parts(self) -> dict[str, str]:
        """The fieldId has the format: 'BO:947dfef9ae6b072ca567a444dca79d9f9ea47a112f,FI:9492462c89a8f7785f1537412ca51a2f218293edb0,RE:9492535dfbf4286b49047f45bab2f201737e739a46'
        This method returns a dict with the keys 'BO', 'FI', 'RE', etc. and the values are the corresponding IDs."""
        r = {}
        for part in self.fieldId.split(','):
            k, v = part.split(':', 1)
            r[k.upper()] = v.lower()
        return r

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
            self.python_type_module = 'datetime'
            if self.hasDate and self.hasTime:
                self.python_type = 'datetime.datetime'
            elif self.hasDate:
                self.python_type = 'datetime.date'
            elif self.hasTime:
                self.python_type = 'datetime.time'
            else:
                self.python_type = 'datetime.datetime'
        elif self.type == 'Number':
            if self.decimalDigits == 0:
                self.python_type = 'int'
            else:
                self.python_type = 'decimal.Decimal'
                self.python_type_module = 'decimal'
                self.pydantic_field_args['decimal_places'] = self.decimalDigits
                if self.wholeDigits:
                    self.pydantic_field_args['max_digits'] = self.wholeDigits
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

    def generate_model(self, schema: ValidSchema) -> str:
        template = self._jinja_env.get_template('model.py.j2')
        fields = [ParsedFieldDefinition(**field.dict())
                  for field in schema.fieldDefinitions]
        modules = set()
        for field in fields:
            field.resolve_type()
            if field.python_type_module:
                modules.add(field.python_type_module)
            assert field.fieldid_parts['BO'] == schema.busObId
        model_str = template.render(schema=schema, fields=fields, modules=modules, settings=self._instance_settings)
        model_str = black.format_str(model_str, mode=black.FileMode(preview=True))
        return model_str
