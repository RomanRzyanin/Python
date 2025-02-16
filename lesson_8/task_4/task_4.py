'''Задание №4
Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка
csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы
функции.
'''

import csv
import json
from pathlib import Path
import string
import random as r


# _path_1 =
# el = Path.cwd()
# print(el)

def add_zero(num):
    # return '0' * (10 - len(num)) + num
    return num.zfill(10)


def func():
    with (
        open('test.csv', 'r', newline='', encoding='utf-8') as cs_f,
        open('task8_21.json', 'w', encoding='utf-8') as js_f
    ):
        reader = csv.reader(cs_f)
        res = []
        cnt = 0

        for item in list(reader)[1:]:
            # if cnt != 0:
            tmp = {'level': item[0],
                   'id': add_zero(item[1]),
                   'name': item[2].title(),
                   'hash': hash(item[2] + item[1])}
            res.append(tmp)
            # else:
            # cnt += 1

        # print(res)
        json.dump(res, js_f, ensure_ascii=False)


if __name__ == '__main__':
    func()
