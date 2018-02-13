import git
import svn
import linguisticCodeReport.fileshelper as fs
from hashlib import sha1


class VCS(object):
    __vcs_name__ = ''

    def __init__(self, vcs_type):
        self.vcs_type = vcs_type

    def clone_repo(self, repo_url, repo_path, encoding):
        None


class GitVCS(VCS):
    __vcs_name__ = 'git'

    @classmethod
    def is_vcs_for(cls, vcs_type):
        return vcs_type.lower() == cls.__vcs_name__

    @classmethod
    def clone_repo(cls, repo_url, repo_path='', encoding='utf-8'):
        local_path = repo_path
        if local_path == '':
            local_path = fs.join_path_filename('.', sha1(bytes(repo_url, encoding=encoding)).hexdigest())
        git.Repo.clone_from(repo_url, local_path)
        return local_path

class SvnVCS(VCS):
    __vcs_name__ = 'svn'

    @classmethod
    def is_vcs_for(cls, vcs_type):
        return vcs_type.lower() == cls.__vcs_name__

    @classmethod
    def clone_repo(cls, repo_url, repo_path='', encoding='utf-8'):
        """todo clone repo for SVN"""
        None


def get_vcs(vcs_type):
    """получает экземпляр класса по его текстовому имени"""

    for cls in VCS.__subclasses__():
        if cls.is_vcs_for(vcs_type):
            return cls(vcs_type)
    raise ValueError


def get_available_vcss():
    """список всех поддерживаемых систем контроля версий"""

    vcss = set()
    for cls in VCS.__subclasses__():
        vcss |= {cls.__vcs_name__}
    return vcss
