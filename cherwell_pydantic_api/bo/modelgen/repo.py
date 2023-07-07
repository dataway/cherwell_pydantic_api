# pyright errors abound without the following, because dulwich is not typed
# pyright: strict, reportUnknownMemberType=false
import logging
from pathlib import Path
from typing import Iterable, Literal, Optional, Union

from dulwich import porcelain
from dulwich.errors import NotGitRepository
from dulwich.repo import Repo

from cherwell_pydantic_api.instance import Instance
from cherwell_pydantic_api.settings import Settings



logger = logging.getLogger(__name__)


FileTypeLiteral = Literal['registry', 'model']
FileGenerator = Iterable[tuple[str, str]]


class ModelRepo:
    _repo: Optional[Repo]

    def __init__(self, *, create: bool = False, permit_missing: bool = False):
        is_new = False
        self._repo_dir = Settings().repo_dir.absolute()
        if not self._repo_dir.exists():
            if create:
                self._repo_dir.mkdir(parents=True)
            elif permit_missing:
                self._repo = None
                return
            else:
                raise FileNotFoundError(
                    f'Repo directory {self._repo_dir} does not exist')
        try:
            self._repo = Repo(root=str(self._repo_dir))
        except NotGitRepository:
            if create:
                self._repo = Repo.init(path=str(self._repo_dir))
                is_new = True
            else:
                raise
        if is_new:
            self._repo_dir.joinpath('.gitignore').write_bytes(
                Path(__file__).parent.joinpath('../templates/dot_gitignore').read_bytes())
            self._repo.stage('.gitignore')
            commit = f'cherwell_pydantic_api: initial repo setup'
            author = Settings().repo_author
            self._repo.do_commit(message=commit.encode(),
                                 author=author.encode())


    def prepare_save(self, *, instance_name: Optional[str] = None, instance: Optional[Instance] = None) -> tuple[Instance, Path]:
        if self._repo is None:
            raise ValueError('Repository is missing')
        # ensure repo is clean
        repo_status = porcelain.status(self._repo) # type: ignore
        if repo_status.unstaged or repo_status.untracked or repo_status.staged['add'] or repo_status.staged['delete'] or repo_status.staged['modify']:
            raise ValueError(
                'Repo is not clean, please commit or stash your changes before saving')

        # resolve arguments
        if instance is None:
            if instance_name is None:
                raise ValueError(
                    'Either instance_name or instance must be given')
            instance = Instance.use(instance_name)
        else:
            instance_name = instance.settings.name

        instance_dir = self._repo_dir / instance.settings.get_repo_subpackage()
        if not instance_dir.exists():
            logging.info(
                f'Creating instance directory {instance_dir} for instance {instance_name}')
            instance_dir.mkdir()
        return (instance, instance_dir)


    def save(self, *,
             instance_name: Optional[str] = None,
             instance: Optional[Instance] = None,
             file_type: FileTypeLiteral = 'registry',
             file_generator: FileGenerator,
             commit: bool = True) -> Optional[bytes]:
        if self._repo is None:
            raise ValueError('Repository is missing')
        instance, instance_dir = self.prepare_save(
            instance_name=instance_name, instance=instance)
        file_type_dir = instance_dir / file_type
        if not file_type_dir.exists():
            logging.info(
                f'Creating {file_type} directory {file_type_dir} for instance {instance_name}')
            file_type_dir.mkdir()
        for filename, content in file_generator:
            filepath = file_type_dir / filename
            logging.info(f'Writing file {filepath}')
            filepath.write_text(content)
            self._repo.stage(str(filepath.relative_to(self._repo_dir)))
        if commit:
            return self.commit(instance=instance, file_type=file_type)
        return None


    def commit(self, *, instance: Instance, file_type: FileTypeLiteral) -> Optional[bytes]:
        if self._repo is None:
            raise ValueError('Repository is missing')
        # Check if there are any changes to commit (because dulwich allows empty commits)
        encoding = self._repo.get_config().encoding
        repo_status = porcelain.status(self._repo)  # type: ignore
        if not repo_status.staged['add'] and not repo_status.staged['delete'] and not repo_status.staged['modify']:
            logging.info(
                f'No {file_type} changes to commit for instance {instance.settings.name}')
            return None
        commit = f'cherwell_pydantic_api: update {file_type} for instance {instance.settings.name}'
        author = Settings().repo_author
        branch = instance.settings.get_repo_branch()
        if branch.encode(encoding) not in porcelain.branch_list(self._repo):
            porcelain.branch_create(self._repo, branch.encode(encoding))
        ref = f'refs/heads/{branch}'
        porcelain.update_head(self._repo, ref)  # this is like git checkout
        logging.info(
            f'Committing {file_type} to {branch} for instance {instance.settings.name}')
        return self._repo.do_commit(message=commit.encode(),
                                    author=author.encode(), ref=ref.encode()) # type: ignore


    def save_instance(self, instance: Instance) -> Optional[bytes]:
        return self.save(instance=instance, file_generator=instance.bo.marshal())


    def save_all(self) -> dict[str, Optional[bytes]]:
        r: dict[str, Optional[bytes]] = {}
        for instance in Instance.all_instances():
            r[instance.settings.name] = self.save_instance(instance)
        return r


    def get_info(self, *,
                 instance_name: Optional[str] = None,
                 instance: Optional[Instance] = None) -> dict[str, Union[str, bool, dict[str, Union[str, bool, None]]]]:
        # resolve arguments
        if instance is None:
            if instance_name is None:
                raise ValueError(
                    'Either instance_name or instance must be given')
            instance = Instance.use(instance_name)
        else:
            instance_name = instance.settings.name
        instance_dir = self._repo_dir / instance.settings.get_repo_subpackage()
        r: dict[str, Union[str, bool, dict[str, Union[str, bool, None]]]] = {'instance': {
            'name': instance.settings.name,
            'repo_subpackage': str(instance.settings.get_repo_subpackage()),
            'repo_branch': instance.settings.get_repo_branch()
        },
            'repo': {
                'path': self._repo.path if self._repo else None,
                'settings_path': str(self._repo_dir),
                'instance_path': str(instance_dir),
                'instance_path_exists': instance_dir.exists(),
                'author': Settings().repo_author,
        },
        }
        if self._repo is not None: # type: ignore # could be None if permit_missing is True
            repo_status = porcelain.status(self._repo)  # type: ignore
            r['status'] = {
                'dirty': repo_status.unstaged or repo_status.untracked or repo_status.staged['add'] or repo_status.staged['delete'] or repo_status.staged['modify']
            }
            r['ready'] = True
        else:
            r['ready'] = False
        return r


    @property
    def directory(self) -> str:
        "The absolute path to the repo directory"
        if self._repo is None:
            return str(self._repo_dir)
        return self._repo.path

    @property
    def repo_dir(self) -> Path:
        "The absolute path to the repo directory as a Path object"
        return self._repo_dir
