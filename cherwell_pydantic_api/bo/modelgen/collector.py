import re
from functools import cached_property
from typing import Optional, Pattern, Union, cast

from async_lru import alru_cache
from pydantic import BaseModel

from cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject import (
    SchemaResponse,
    Summary,
)
from cherwell_pydantic_api.bo.modelgen.model_generator import PydanticModelGenerator
from cherwell_pydantic_api.bo.modelgen.repo import FileGenerator, ModelRepo
from cherwell_pydantic_api.bo.valid_schema import ValidSchema
from cherwell_pydantic_api.instance import Instance
from cherwell_pydantic_api.types import BusinessObjectType, BusObID
from cherwell_pydantic_api.utils import docwraps



try:
    import click
except ImportError:
    click = None  # type: ignore


FilterType = Union[Pattern[str], str, None]


def compile_filter(filter: FilterType) -> Optional[Pattern[str]]:
    if filter is None:
        return None
    if isinstance(filter, str):
        if filter == '':
            return None
        return re.compile(filter)
    return filter


class CollectorItem:
    "Contains a Business Object summary, and a verdict on whether to generate a model for it."

    def __init__(self,
                 bo_type: BusinessObjectType,
                 summary: Summary,
                 verdict: Optional[bool] = None,
                 schema: Optional[SchemaResponse] = None,
                 parent_item: Optional["CollectorItem"] = None):
        assert summary.busObId is not None
        self.summary = summary
        self.verdict = verdict
        self.bo_type = bo_type
        self.schema = schema
        self._children: set["CollectorItem"] = set()
        self.parent_item = parent_item
        if parent_item is not None:
            parent_item._children.add(self)

    @property
    def busobid(self) -> BusObID:
        return self.summary.busObId  # type: ignore  # asserted not None in __init__

    @property
    def name(self) -> str:
        return self.summary.name  # type: ignore

    @cached_property
    def valid_schema(self) -> Optional[ValidSchema]:
        if self.schema is None:
            return None
        return ValidSchema.from_schema_response(self.schema)


    def to_dict(self) -> dict[str, Union[str, int, None]]:
        "Convert to dictionary e.g. for DataFrame use"
        return {'name': self.name,
                'busobid': self.busobid,
                'verdict': self.verdict,
                'bo_type': self.bo_type,
                'num_fields': len(self.schema.fieldDefinitions) if (self.schema and self.schema.fieldDefinitions) else None,
                'displayName': self.summary.displayName,
                'lookup': self.summary.lookup,
                'major': self.summary.major,
                'supporting': self.summary.supporting,
                'parent_name': self.parent_item.name if self.parent_item else None,
                }


class CollectorSettings(BaseModel):
    # mypy wants to see Pattern[str] but Pydantic requires Pattern
    bo_include_filter: Optional[Pattern] = None  # type: ignore
    bo_exclude_filter: Optional[Pattern] = None  # type: ignore


class Collector:
    "Collects Business Object summaries and schemas from a Cherwell instance, in order to filter them and generate models."

    def __init__(self, instance: Instance, *, bo_include_filter: FilterType = None, bo_exclude_filter: FilterType = None, verbose: bool = False):
        self._instance = instance
        self._bo_include_filter = compile_filter(bo_include_filter)
        self._bo_exclude_filter = compile_filter(bo_exclude_filter)
        self.items: list[CollectorItem] = []
        self.verbose = verbose


    @property
    def bo_include_filter(self) -> Optional[Pattern[str]]:
        return self._bo_include_filter

    @bo_include_filter.setter
    def bo_include_filter(self, value: FilterType):
        self._bo_include_filter = compile_filter(value)

    @property
    def bo_exclude_filter(self) -> Optional[Pattern[str]]:
        return self._bo_exclude_filter

    @bo_exclude_filter.setter
    def bo_exclude_filter(self, value: FilterType):
        self._bo_exclude_filter = compile_filter(value)


    def filter_bo(self, type: str, summary: Summary) -> bool:
        if summary.name is None:
            return False
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
            fields: Union[str, int] = len(
                item.schema.fieldDefinitions) if item.schema.fieldDefinitions else 0
            rels: Union[str, int] = len(
                item.schema.relationships) if item.schema.relationships else 0
        else:
            fields = rels = '?'
        report = f" {item.bo_type[:3]:3} {item.name:30} {fields:>4} {rels:>4}  {item.busobid:24}"
        if click:
            click.secho(icon, nl=False,
                        bg='green' if item.verdict else 'red', fg='white')
            click.secho(report, fg='cyan')
        else:
            print(icon, report)


    @alru_cache()
    @docwraps(Instance.get_bo_summaries)
    async def get_bo_summaries(self, bo_type: BusinessObjectType) -> list[Summary]:
        return await self._instance.get_bo_summaries(bo_type)


    @alru_cache(maxsize=1024)
    @docwraps(Instance.get_bo_schema)
    async def get_bo_schema(self, busobid: BusObID) -> Optional[SchemaResponse]:
        return await self._instance.get_bo_schema(busobid=busobid)


    async def select(self) -> list[CollectorItem]:
        "Get all the business object summaries from Cherwell and filter them."
        items: list[CollectorItem] = []
        for bo_type in cast(list[BusinessObjectType], ['Major', 'Supporting', 'Lookup', 'Groups']):
            for bo_summary in await self.get_bo_summaries(bo_type):
                verdict = self.filter_bo(bo_type, bo_summary)
                item = CollectorItem(bo_type=bo_type, summary=bo_summary, verdict=verdict)
                items.append(item)
                # Add group members. There is only one level of groups according to Cherwell docs.
                if bo_summary.groupSummaries:
                    for group_summary in bo_summary.groupSummaries:
                        verdict = self.filter_bo(bo_type, group_summary)
                        # If a child group is included, then the parent is included too.
                        if verdict and not item.verdict:
                            item.verdict = True
                        sub_item = CollectorItem(bo_type=bo_type, summary=group_summary,
                                                 verdict=verdict, parent_item=item)
                        items.append(sub_item)
        return items


    async def collect(self) -> list[CollectorItem]:
        "Get all the business object summaries from Cherwell, filter them, and fetch the schemas of matching business objects."
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
        model_generator = PydanticModelGenerator(self._instance)
        yield ('__base.py', model_generator.generate_base())
        for item in self.items:
            if not item.verdict:
                continue
            schema = self._instance.bo.get_schema(item.busobid)
            if item.parent_item:
                schema.parentSchema = self._instance.bo.get_schema(item.parent_item.busobid)
            else:
                schema.parentSchema = None
            yield (f"{schema.identifier}.py", model_generator.generate_model(schema))


    def save_models(self, repo: ModelRepo):
        return repo.save(instance=self._instance, file_type='model', file_generator=self.generate_models())


    def generate_settings(self) -> FileGenerator:
        collector_settings = CollectorSettings(
            bo_include_filter=self.bo_include_filter, bo_exclude_filter=self.bo_exclude_filter)
        yield ('collector_settings.json', collector_settings.model_dump_json(indent=2, round_trip=True))


    def save_settings(self, repo: ModelRepo):
        return repo.save(instance=self._instance, file_type='registry', file_generator=self.generate_settings())


    def load_settings(self, repo: ModelRepo):
        filepath = repo.repo_dir / self._instance.settings.get_repo_subpackage() / 'registry/collector_settings.json'
        collector_settings = CollectorSettings.model_validate_json(filepath.read_text())

        self.bo_include_filter = collector_settings.bo_include_filter  # type: ignore
        self.bo_exclude_filter = collector_settings.bo_exclude_filter  # type: ignore


    def clear_caches(self):
        self.get_bo_summaries.cache_clear()
        self.get_bo_schema.cache_clear()


    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._instance}, bo_include_filter={self._bo_include_filter}, bo_exclude_filter={self._bo_exclude_filter})"
