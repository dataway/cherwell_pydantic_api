import re
from typing import Optional

from pydantic import AnyHttpUrl, BaseSettings, DirectoryPath, Field, SecretStr, validator



class InstanceSettingsBase(BaseSettings):
    name: str = Field(default='_unset')
    base_url: Optional[AnyHttpUrl] = Field(default=None)
    client_id: SecretStr = Field(default='')
    username: str = Field(default='')
    password: SecretStr = Field(default='')
    timeout: float = Field(default=0.0)


class InstanceSettings(InstanceSettingsBase):
    pass


class Settings(InstanceSettingsBase):
    name: str = 'default'
    inst: dict[str, InstanceSettings] = Field(default={})
    model_dir: DirectoryPath = Field(default='models')
    
    _re_inst_name = re.compile(r'^[a-z][a-z0-9]+$')

    def get_instance(self, instance_name: Optional[str] = None) -> Optional[InstanceSettingsBase]:
        """Return the instance settings for the given instance, or the default settings if instance_name is None or 'default'"""
        if instance_name is None or instance_name == self.name:
            return self
        return self.inst.get(instance_name, None)
    
    @validator('inst')
    def validate_inst(cls, v):
        for inst_name, inst in v.items():
            if not cls._re_inst_name.match(inst_name) or inst_name == 'default':
                raise ValueError(f"Invalid instance name: {inst_name}")
        return v
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._fixup()

    def _fixup(self):
        """After instantiation, propagate the default values to the instances."""
        for inst_name, inst in self.inst.items():
            if inst.name != '_unset':
                raise ValueError("Don't specify the instance name in the instance settings")
            inst.name = inst_name
            if not inst.base_url:
                inst.base_url = self.base_url
            if not inst.client_id:
                inst.client_id = self.client_id
            if not inst.username:
                inst.username = self.username
            if not inst.password:
                inst.password = self.password
            if not inst.timeout:
                inst.timeout = self.timeout


    class Config:
        env_file = ['cherwell.env']
        env_file_encoding = 'utf-8'
        env_prefix = 'cherwell_'
        env_nested_delimiter = '__'



if __name__ == '__main__':
    print(Settings().dict())
