import collections
import json
import csv
import linguisticCodeReport.fileshelper as fh


class Output:
    __name_output__ = ''

    def __init__(self, name_output):
        self.__name_output__ = name_output

    @classmethod
    def print_output_format(cls, report_data, param):
        None


class OutputJson(Output):
    """Класс вывода в JSON"""
    __name_output__ = 'json'

    @classmethod
    def print_output_format(cls, report_data, param):
        json1 = json.dumps(report_data, ensure_ascii=False)
        return json1


class OutputConsole(Output):
    """Класс вывода в консоль"""
    __name_output__ = 'console'

    @classmethod
    def print_output_format(cls, report_data, param):
        strout = 'total {0} words, {1} unique'.format(len(report_data), len(set(report_data)))
        for word, occurence in collections.Counter(report_data).most_common(param):
            strout = strout + '\n' + word + ': ' + str(occurence)
        return strout


class OutputCsv(Output):
    """Класс вывода в CSV файл"""
    __name_output__ = 'csv'

    @classmethod
    def print_output_format(cls, report_data, param):
        if fh.get_extension(str(param)).lower() != '.csv':
            filename = str(param) + '.csv'
        else:
            filename = str(param)
        w = csv.writer(open(filename, "w"))
        for key, val in report_data.items():
            w.writerow([key, val])


def get_output(output_name):
    """получает экземпляр класса по его текстовому имени"""

    for cls in Output.__subclasses__():
        if cls.__name_output__ == output_name:
            return cls(output_name)
    raise ValueError


def get_available_outputs():
    """список всех поддерживаемых вывовов"""

    outputs = set()
    for cls in Output.__subclasses__():
        outputs |= {cls.__name_output__}
    return outputs


if __name__ == '__main__':
    o = get_output('csv')
    o.print_output_format({'Python': '.py', 'C++': '.cpp', 'Java': '.java'}, 1212)
