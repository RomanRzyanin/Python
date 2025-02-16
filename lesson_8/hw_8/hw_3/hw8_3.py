'''Задача 3. Агрегирование данных из CSV файла
Напишите скрипт, который считывает данные из JSON файла и сохраняет их в CSV
файл. JSON файл содержит данные о продуктах (название, цена, количество на
складе). В CSV файле каждая строка должна соответствовать одному продукту.'''

import os
import read_json as r_j
import save_csv as s_c


def main_func(path, res_file):
    data = r_j.read_json(path)
    s_c.save_csv(data, res_file)


_path = os.getcwd() + '\\zad_3\\products.json'
file = os.getcwd() + '\\zad_3\\products.csv'

if __name__ == '__main__':
    main_func(_path, file)

# print(_path)
# print(r_j.read_json(_path))
