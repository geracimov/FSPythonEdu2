import git
import svn
import linguisticCodeReport.fileshelper as fs
from hashlib import sha1


class VCS(object):

    def __init__(self, vcs_type):
        self.vcs_type = vcs_type


class GitVCS(VCS):
    @classmethod
    def is_vcs_for(cls, vcs_type):
        return vcs_type.lower() == 'git'

    @classmethod
    def clone_repo(cls, repo_url, repo_path='', encoding='utf-8'):
        local_path = repo_path
        if local_path == '':
            local_path = fs.join_path_filename('.', sha1(bytes(repo_url, encoding=encoding)).hexdigest())
        print(local_path)
        git.Repo.clone_from(repo_url, local_path)


class SvnVCS(VCS):

    @classmethod
    def is_vcs_for(cls, vcs_type):
        return vcs_type.lower() == 'svn'

    @classmethod
    def clone_repo(cls, repo_url, repo_path='', encoding='utf-8'):
        local_path = repo_path


def get_vcs(vcs_type):
    for cls in VCS.__subclasses__():
        if cls.is_vcs_for(vcs_type):
            return cls(vcs_type)
    raise ValueError
