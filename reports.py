import argparse
import collections
import sys
import linguisticCodeReport.vcsfactory as vh
import linguisticCodeReport.nltkhelper as nh
import linguisticCodeReport.outputfactory as of
import linguisticCodeReport.fileshelper as fh
import linguisticCodeReport.langfactory as lf
import linguisticCodeReport.listhelper as lh


def create_parser():
    _parser = argparse.ArgumentParser()
    _parser.add_argument('--repotype', required=True, choices=vh.get_available_vcss())
    _parser.add_argument('--repourl', required=True)
    _parser.add_argument('--speechparts', nargs='+', required=True, choices=nh.get_available_parts())
    _parser.add_argument('--scope', nargs='+', choices={'funcs', 'vars'}, default='funcs')
    _parser.add_argument('--output', required=True, choices=of.get_available_outputs())
    _parser.add_argument('--lang', required=True, choices=lf.get_available_langs())
    return _parser


def get_report_data_freq_speech_parts(_path, _lang, _speechparts, _scope):
    """Получение данных для отчета по частоте использования частей речи в названиях переменных, функций и пр."""
    lng = lf.get_lang(_lang)
    fncs = []
    for file in lng.get_lang_filenames_by_path(_path):
        fncs.append(lng.get_defnames_from_file(file, _scope))
    sps = nh.get_speech_parts_from_texts(lh.flat(fncs), _speechparts)
    worddict = dict()
    for word, occurence in collections.Counter(sps).most_common(10):
        worddict.update({word: occurence})
    return worddict


def get_report_output_format(_data_report, _output, param):
    """выходной формат для отчета.
        на вход словарь с данными, тип вывода и доп параметр
        на выход результат.    возможно стоило вывод реализовать в самом субклассе Output
    """

    output = of.get_output(_output)
    return output.print_output_format(_data_report, param)


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    # print(namespace)

    local_vcs = vh.get_vcs(namespace.repotype)
    path = local_vcs.clone_repo(namespace.repourl)

    data_report = get_report_data_freq_speech_parts(path, namespace.lang, namespace.speechparts, namespace.scope)

    rof = get_report_output_format(data_report, namespace.output, 3)
    print(rof)

    fh.rm_dir_recursively(path)
