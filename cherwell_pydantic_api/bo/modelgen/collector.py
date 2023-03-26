import re
from typing import Optional, Pattern, Union, cast

from async_lru import alru_cache

from cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject import (
    SchemaResponse,
    Summary,
)
from cherwell_pydantic_api.bo.modelgen.model_generator import PydanticModelGenerator
from cherwell_pydantic_api.bo.modelgen.repo import FileGenerator, ModelRepo
from cherwell_pydantic_api.instance import Instance
from cherwell_pydantic_api.types import BusinessObjectType, BusObID
from cherwell_pydantic_api.utils import docwraps



try:
    import click
except ImportError:
    click = None


FilterType = Union[Pattern, str, None]


def compile_filter(filter: FilterType) -> Optional[Pattern]:
    if filter is None:
        return None
    if isinstance(filter, str):
        return re.compile(filter)
    return filter


class CollectorItem:
    "Contains a Business Object summary, and a verdict on whether to generate a model for it."

    __slots__ = ['summary', 'verdict', 'bo_type', 'schema']

    def __init__(self,
                 bo_type: BusinessObjectType,
                 summary: Summary,
                 verdict: Optional[bool] = None,
                 schema: Optional[SchemaResponse] = None):
        assert summary.busObId is not None
        self.summary = summary
        self.verdict = verdict
        self.bo_type = bo_type
        self.schema = schema

    @property
    def busobid(self) -> BusObID:
        return self.summary.busObId  # type: ignore

    @property
    def name(self) -> str:
        return self.summary.name  # type: ignore



class Collector:
    "Collects Business Object summaries and schemas from a Cherwell instance, in order to filter them and generate models."

    def __init__(self, instance: Instance, *, bo_include_filter: FilterType = None, bo_exclude_filter: FilterType = None, verbose: bool = False):
        self._instance = instance
        self._bo_include_filter = compile_filter(bo_include_filter)
        self._bo_exclude_filter = compile_filter(bo_exclude_filter)
        self.items: list[CollectorItem] = []
        self.verbose = verbose


    @property
    def bo_include_filter(self) -> Optional[Pattern]:
        return self._bo_include_filter

    @bo_include_filter.setter
    def bo_include_filter(self, value: FilterType):
        self._bo_include_filter = compile_filter(value)

    @property
    def bo_exclude_filter(self) -> Optional[Pattern]:
        return self._bo_exclude_filter

    @bo_exclude_filter.setter
    def bo_exclude_filter(self, value: FilterType):
        self._bo_exclude_filter = compile_filter(value)


    def filter_bo(self, type: str, summary: Summary) -> bool:
        if self._bo_exclude_filter is not None:
            if self._bo_exclude_filter.match(summary.name):
                return False
        if self._bo_include_filter is not None:
            if self._bo_include_filter.match(summary.name):
                return True
        return False


    def verbose_report(self, item: CollectorItem):
        icon = "[**]" if item.verdict else "[  ]"
        if item.schema:
            fields = len(
                item.schema.fieldDefinitions) if item.schema.fieldDefinitions else 0
            rels = len(item.schema.relationships) if item.schema.relationships else 0
        else:
            fields = rels = '?'
        report = f" {item.bo_type[:3]:3} {item.name:30} {fields:>4} {rels:>4}  {item.busobid:24}"
        if click:
            click.secho(icon, nl=False,
                        bg='green' if item.verdict else 'red', fg='white')
            click.secho(report, fg='cyan')
        else:
            print(icon, report)


    @alru_cache
    @docwraps(Instance.get_bo_summaries)
    async def get_bo_summaries(self, bo_type: BusinessObjectType) -> list[Summary]:
        return await self._instance.get_bo_summaries(bo_type)


    @alru_cache(maxsize=1024)
    @docwraps(Instance.get_bo_schema)
    async def get_bo_schema(self, busobid: BusObID) -> Optional[SchemaResponse]:
        return await self._instance.get_bo_schema(busobid=busobid)


    async def select(self) -> list[CollectorItem]:
        "Get all the business object summaries from Cherwell and filter them."
        items = []
        for bo_type in cast(list[BusinessObjectType], ['Major', 'Supporting', 'Lookup', 'Groups']):
            for bo_summary in await self.get_bo_summaries(bo_type):
                verdict = self.filter_bo(bo_type, bo_summary)
                item = CollectorItem(
                    bo_type=bo_type, summary=bo_summary, verdict=verdict)
                items.append(item)
        return items


    async def collect(self) -> list[CollectorItem]:
        items = await self.select()
        for item in items:
            if item.verdict:
                schema = await self.get_bo_schema(item.summary.busObId)
            else:
                schema = None
            item.schema = schema
            if self.verbose:
                self.verbose_report(item)
        self.items = items
        return items


    def generate_models(self) -> FileGenerator:
        yield ('__init__.py', '### autogenerated by cherwell_pydantic_api ###\n')
        model_generator = PydanticModelGenerator(self._instance.settings)
        yield ('__base.py', model_generator.generate_base())
        for item in self.items:
            schema = self._instance.bo.get_schema(item.busobid)
            yield (f"{schema.identifier}.py", model_generator.generate_model(schema))


    def save_models(self, repo: ModelRepo):
        return repo.save(instance=self._instance, file_type='model', file_generator=self.generate_models())


    def clear_caches(self):
        self.get_bo_summaries.cache_clear()
        self.get_bo_schema.cache_clear()


    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._instance}, bo_include_filter={self._bo_include_filter}, bo_exclude_filter={self._bo_exclude_filter})"

