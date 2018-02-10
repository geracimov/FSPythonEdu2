import ast
import os


def get_filenames_by_path(path, extension, tdown=True):
    filenames = []
    for dirname, dirs, files in os.walk(path, topdown=tdown):
        filesgen = (file for file in files if file.endswith(extension))
        for file in filesgen:
            filename = join_path_filename(dirname, file)
            filenames.append(filename)
    return filenames


def join_path_filename(path, filename):
    return os.path.join(path, filename)


def get_funcnames_from_file(filename):
    funcnames = []
    with open(filename, 'r', encoding='utf-8') as attempt_handler:
        main_file_content = attempt_handler.read()
    try:
        tree = ast.parse(main_file_content)
        funcnames = [node.name.lower() for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    except SyntaxError as e:
        print(e)
    return funcnames
