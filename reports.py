import linguisticCodeReport.vschelper as vh

if __name__ == '__main__':
    local_vcs = vh.get_vcs('git')
    print(local_vcs.__class__.__name__)
    local_vcs.clone_repo('https://github.com/geracimov/PythonEdu.git')
