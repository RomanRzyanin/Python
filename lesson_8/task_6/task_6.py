'''Задание №6
Напишите функцию, которая преобразует pickle файл
хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи
4 этого семинара.
Функция должна извлекать ключи словаря для заголовков
столбца из переданного файла.
'''

import json
import csv
import pickle
from pathlib import Path

_path_1 = Path.cwd()


def converter():
    with open('task8_21.pickle', 'rb') as f_p, \
            open('test.csv', 'w', newline='', encoding='utf-8') as f_cs:
        data = pickle.load(f_p)
        print(data)
        writer = csv.DictWriter(f_cs, fieldnames=data[0].keys())
        writer.writeheader()
        # for el in data:
        #     writer.writerow(el)
        writer.writerows(data)


if __name__ == '__main__':
    converter()
