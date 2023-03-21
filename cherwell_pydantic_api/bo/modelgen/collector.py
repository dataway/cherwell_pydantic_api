

import re
from typing import Optional, Pattern, Union
from cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject import SchemaResponse, Summary
from cherwell_pydantic_api.bo.modelgen.model_generator import PydanticModelGenerator
from cherwell_pydantic_api.bo.modelgen.repo import ModelRepo, FileGenerator
from cherwell_pydantic_api.instance import Instance
from cherwell_pydantic_api.types import BusObID
try:
    import click
except ImportError:
    click = None


FilterType = Union[Pattern, str, None]


def compile_filter(filter: FilterType) -> Optional[Pattern]:
    if filter is None:
        return None
    if isinstance(filter, str):
        return re.compile(filter, re.IGNORECASE)
    return filter


class Collector:
    def __init__(self, instance: Instance, *, bo_include_filter: FilterType = None, bo_exclude_filter: FilterType = None, verbose: bool = False):
        self._instance = instance
        self._bo_include_filter = compile_filter(bo_include_filter)
        self._bo_exclude_filter = compile_filter(bo_exclude_filter)
        self.busobids: list[BusObID] = []
        self.verbose = verbose


    def filter_bo(self, type: str, summary: Summary) -> bool:
        if self._bo_exclude_filter is not None:
            if self._bo_exclude_filter.match(summary.name):
                return False
        if self._bo_include_filter is not None:
            if self._bo_include_filter.match(summary.name):
                return True
        return False


    def verbose_report(self, verdict: bool, type: str, summary: Summary, schema: Optional[SchemaResponse]):
        icon = "[ \u2611 ]" if verdict else "[   ]"
        if schema:
            fields = len(schema.fieldDefinitions) if schema.fieldDefinitions else 0
            rels = len(schema.relationships) if schema.relationships else 0
        else:
            fields = rels = 0
        report = f" {type:10} {summary.name:40} {fields:4} {rels:4} {summary.busObId:24}"
        if click:
            click.secho(icon, nl=False, bg='green' if verdict else 'red', fg='white')
            click.secho(report, fg='cyan')
        else:
            print(icon, report)
            
            
    async def collect(self) -> list[str]:
        bo_names = []
        for bo_type in ['Major', 'Supporting', 'Lookup', 'Groups']:
            for bo_summary in await self._instance.get_bo_summaries(type=bo_type):  # type: ignore
                verdict = self.filter_bo(bo_type, bo_summary)
                if verdict:
                    assert bo_summary.busObId is not None
                    bo_names.append(bo_summary.name)
                    self.busobids.append(bo_summary.busObId)
                    schema = await self._instance.get_bo_schema(busobid=bo_summary.busObId)
                else:
                    schema = None
                if self.verbose:
                    self.verbose_report(verdict, bo_type, bo_summary, schema)
        return bo_names


    def generate_models(self) -> FileGenerator:
        yield ('__init__.py', '### autogenerated by cherwell_pydantic_api ###\n')
        model_generator = PydanticModelGenerator(self._instance.settings)
        for busobid in self.busobids:
            schema = self._instance.bo.get_schema(busobid)
            yield (f"{schema.name.lower()}.py", model_generator.generate_model(schema))


    def save_models(self, repo: ModelRepo):
        return repo.save(instance=self._instance, file_type='model', file_generator=self.generate_models())

