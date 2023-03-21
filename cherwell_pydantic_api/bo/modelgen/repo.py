import logging
from pathlib import Path
from typing import Optional

from dulwich import porcelain
from dulwich.errors import NotGitRepository
from dulwich.repo import Repo

from cherwell_pydantic_api.instance import Instance
from cherwell_pydantic_api.settings import Settings



logger = logging.getLogger(__name__)



class ModelRepo:
    def __init__(self, create: bool = False):
        is_new = False
        self._repo_dir = Settings().repo_dir.absolute()
        if not self._repo_dir.exists():
            if create:
                self._repo_dir.mkdir(parents=True)
            else:
                raise ValueError(
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


    def save(self, *, instance_name: Optional[str] = None, instance: Optional[Instance] = None, commit: bool = True):
        # ensure repo is clean
        repo_status = porcelain.status(self._repo)  # type: ignore
        if repo_status.unstaged or repo_status.untracked or repo_status.staged['add'] or repo_status.staged['delete'] or repo_status.staged['modify']:
            raise ValueError(
                'Repo is not clean, please commit or stash your changes before saving')

        # resolve arguments
        if instance is None:
            if instance_name is None:
                raise ValueError(
                    'Either instance_name or instance must be given')
            instance = Instance._instances[instance_name]
        else:
            instance_name = instance.settings.name

        instance_dir = self._repo_dir / instance.settings.get_repo_subdir()
        if not instance_dir.exists():
            logging.info(
                f'Creating instance directory {instance_dir} for instance {instance_name}')
            instance_dir.mkdir()
        registry_dir = instance_dir / 'registry'
        if not registry_dir.exists():
            logging.info(
                f'Creating registry directory {registry_dir} for instance {instance_name}')
            registry_dir.mkdir()
        for filename, content in instance.bo.marshal():
            filepath = registry_dir / filename
            logging.info(f'Writing file {filepath}')
            filepath.write_text(content)
            self._repo.stage(str(filepath.relative_to(self._repo_dir)))
        if commit:
            self.commit(instance=instance)


    def commit(self, *, instance: Instance) -> Optional[bytes]:
        # Check if there are any changes to commit (because dulwich allows empty commits)
        repo_status = porcelain.status(self._repo)  # type: ignore
        if not repo_status.staged['add'] and not repo_status.staged['delete'] and not repo_status.staged['modify']:
            logging.info(
                f'No changes to commit for instance {instance.settings.name}')
            return None
        commit = f'cherwell_pydantic_api: update instance {instance.settings.name}'
        author = Settings().repo_author
        branch = instance.settings.get_repo_branch()
        ref = f'refs/heads/{branch}'
        porcelain.update_head(self._repo, ref)  # this is like git checkout
        logging.info(
            f'Committing to {branch} for instance {instance.settings.name}')
        return self._repo.do_commit(message=commit.encode(),
                                    author=author.encode(), ref=ref.encode())


    def save_all(self):
        for instance in Instance._instances.values():
            self.save(instance=instance)
