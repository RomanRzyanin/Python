'''Задача 2. Объединение данных из нескольких JSON файлов
Напишите скрипт, который объединяет данные из нескольких JSON файлов в
один. Каждый файл содержит список словарей, описывающих сотрудников
компании (имя, фамилия, возраст, должность). Итоговый JSON файл должен
содержать объединённые списки сотрудников из всех файлов.'''

import os
import find_json_files as f_j_f
import read_json as r_j
import save_json as s_j


def func(path):
    list_files = f_j_f.find_json_files(_path_1)
    result_data = r_j.read_json_files(list_files, _path_1)
    s_j.save_json(result_data, path + 'result_info.json')
    print(result_data)


_path = os.getcwd() + '\\zad_2\\'

if __name__ == '__main__':
    func(_path)
