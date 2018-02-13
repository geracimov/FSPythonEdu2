import os
import shutil


def join_path_filename(path, filename):
    return os.path.join(path, filename)


def get_filenames_by_path(path, tdown=True):
    filenames = []
    for dirname, dirs, files in os.walk(path, topdown=tdown):
        for file in files:
            filename = os.path.join(dirname, file)
            filenames.append(filename)
    return filenames


def get_extension(filename):
    fname, fexten = os.path.splitext(filename)
    return fexten


def rm_dir_recursively(path):
    shutil.rmtree(path, ignore_errors=True)
