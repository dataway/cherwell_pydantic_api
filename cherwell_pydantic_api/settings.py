import keyword
import re
from pathlib import Path
from typing import Any, ClassVar, Optional, Union

from pydantic import AnyHttpUrl, Field, SecretStr, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict



class InstanceSettingsBase(BaseSettings):
    name: str = Field(default='_unset')
    base_url: Optional[AnyHttpUrl] = Field(default=None)
    client_id: SecretStr = Field(default=SecretStr(''))
    username: str = Field(default='')
    password: SecretStr = Field(default=SecretStr(''))
    timeout: float = Field(default=5.0)
    verify: Union[str, bool] = Field(default='on')
    subpackage: Optional[Path] = Field(default=None,
                                       description='Subpackage name, corresponds to subdirectory name within repo_dir, if unset default to instance name')
    repo_branch: Optional[str] = Field(default=None,
                                       description='Branch to use for this instance, if unset default to main')
    intercept_path: Optional[Path] = Field(default=None,
                                           description='If set, intercept HTTP requests and responses and save to files here (internal use)')

    @field_validator('verify')
    @classmethod
    def validate_verify(cls, v: str) -> Union[str, bool]:
        if v.lower() in ('off', 'false', 'no'):
            return False
        if v.lower() in ('', 'on', 'true', 'yes'):
            return True
        return v

    def get_repo_subpackage(self) -> Path:
        if self.subpackage:
            return self.subpackage
        return Path(self.name)

    def get_repo_branch(self) -> str:
        return self.repo_branch if self.repo_branch else 'main'


class InstanceSettings(InstanceSettingsBase):
    pass


class Settings(InstanceSettingsBase):
    name: str = Field(default='default')
    inst: dict[str, InstanceSettings] = Field(default={})
    repo_dir: Path = Field(default=Path('repo'))
    repo_author: str = 'cherwell_pydantic_api <noreply@cherwell-pydantic-api.nonexistent.anthonyuk.dev>'
    suppress_banner: bool = Field(default=False, description='Suppress the CLI welcome banner')

    _re_inst_name: ClassVar[re.Pattern[str]] = re.compile(r'^[a-z][a-z0-9]+$')

    def get_instance(self, instance_name: Optional[str] = None) -> Optional[InstanceSettingsBase]:
        """Return the instance settings for the given instance, or the default settings if instance_name is None or 'default'"""
        if instance_name is None or instance_name == self.name:
            return self
        return self.inst.get(instance_name, None)

    @field_validator('inst')
    @classmethod
    def validate_inst(cls, v: dict[str, InstanceSettings]) -> dict[str, InstanceSettings]:
        for inst_name in v:
            if not cls._re_inst_name.match(inst_name) or inst_name == 'default' or keyword.iskeyword(inst_name):
                raise ValueError(f"Invalid instance name: {inst_name}")
        return v

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self._fixup()

    def _fixup(self):
        # TODO: Use pydantic's built-in support for this
        """After instantiation, propagate the default values to the instances."""
        for inst_name, inst in self.inst.items():
            if inst.name != '_unset':
                raise ValueError(
                    "Don't specify the instance name in the instance settings")
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
    model_config = SettingsConfigDict(
        env_file=['cherwell.env'], env_file_encoding='utf-8', env_prefix='cherwell_', env_nested_delimiter='__')



if __name__ == '__main__':
    print(Settings().model_dump())
