import ast
import linguisticCodeReport.fileshelper as fh
import linguisticCodeReport.listhelper as lh


class Lang(object):
    """ Базовый класс дял языка программирования
        для создания дополнительного класса языка, необходмио
        унаследоваться от этого класса и переопределить методы:
            is_lang_for
            get_defnames_from_file
        и переменные
            __lang_name__ = 'python'
            __lang_extension__ = '.py'
            __definitions__ = {'funcs': ast.FunctionDef, 'vars': ast.ClassDef}
    """
    __lang_name__ = ''
    __lang_extension__ = ''

    def __init__(self, lang_name):
        self.__lang_name__ = lang_name

    def is_lang_for(self, lang_name):
        return lang_name.lower() == self.__lang_name__

    def is_lang_file(self, filename):
        fexten = fh.get_extension(filename)
        return fexten.lower() == self.__lang_extension__

    def get_lang_extension(self):
        return self.__lang_extension__

    def get_lang_filenames_by_path(self, path, tdown=True):
        files = fh.get_filenames_by_path(path, tdown)
        return (file for file in files if self.is_lang_file(file))

    def get_defnames_from_file(self, filename, definitions, encoding='utf-8'):
        return []


class PythonLang(Lang):
    """ Язык Python """
    __lang_name__ = 'python'
    __lang_extension__ = '.py'
    """Вот убей не нашел как определить что """
    __definitions__ = {'funcs': ast.FunctionDef, 'vars': ast.ClassDef}

    @classmethod
    def is_lang_for(cls, lang_name):
        return lang_name.lower() == cls.__lang_name__

    @classmethod
    def get_defnames_from_file(cls, filename, definitions, encoding='utf-8'):
        defnames = []
        with open(filename, 'r', encoding=encoding) as attempt_handler:
            main_file_content = attempt_handler.read()
        try:
            tree = ast.parse(main_file_content)
            for deftype in definitions:
                defnames.append([node.name.lower() for node in ast.walk(tree) if
                                 isinstance(node, cls.__definitions__.get(deftype))])
        except SyntaxError as e:
            print(e)
        return lh.flat(defnames)


class JavaLang(Lang):
    """ Язык Java """
    __lang_name__ = 'java'
    __lang_extension__ = '.java'

    @classmethod
    def is_lang_for(cls, lang_name):
        return lang_name.lower() == cls.__lang_name__

    @classmethod
    def get_defnames_from_file(cls, filename, definitions, encoding='utf-8'):
        """todo необходимо реализовать функцию по получению
        вероятно нужно использовать пакет javalang
        возможно стоит реализовать  функцию получения дерева из файла,
        а отдельной фукнцией пробегать по нему, вероятно они типовые из всех языков
        """
        defnames = []
        return defnames


def get_lang(lang_name):
    """получает экземпляр класса по его текстовому имени"""
    for cls in Lang.__subclasses__():
        if cls.is_lang_for(lang_name):
            return cls(lang_name)
    raise ValueError


def get_available_langs():
    """список всех поддерживаемых языков"""
    langs = set()
    for cls in Lang.__subclasses__():
        langs |= {cls.__lang_name__}
    return langs
