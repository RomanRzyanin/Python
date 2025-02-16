'''Задание №5
Напишите функцию, которая ищет json файлы в указанной
директории и сохраняет их содержимое в виде
одноимённых pickle файлов.
'''

import pickle
import json
from pathlib import Path
from os import listdir

_path_1 = Path.cwd()

def find_json(path = _path_1):
    for el in listdir(path):
        if el.endswith('.json'):
            new_name = el[:el.rfind('.')] + '.pickle'
            with open(path / el, 'r', encoding='utf-8') as in_f, \
                open (path / new_name, 'wb') as out_f:
                pickle.dump(json.load(in_f), out_f)


if __name__ == '__main__':
    find_json()
