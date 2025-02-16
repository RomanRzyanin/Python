'''Задача 4. Агрегирование данных из CSV файла
Напишите скрипт, который считывает данные из CSV файла, содержащего
информацию о продажах (название продукта, количество, цена за единицу), и
подсчитывает общую выручку для каждого продукта. Итог должен быть сохранён в
новом CSV файле.
Пример: Из файла sales.csv нужно создать файл total_sales.csv, где для каждого
продукта будет указана общая выручка.'''

import os
import read_csv as r_c
import edit_data as e_d
import save_csv as s_c


def main_func(path, file):
    f_data = r_c.read_csv(path)
    edit_data = e_d.edit_data(f_data)
    s_c.save_csv(edit_data, file)


_path = os.getcwd() + '\\zad_4\\sales.csv'
file = os.getcwd() + '\\zad_4\\total_sales.csv'

if __name__ == '__main__':
    main_func(_path, file)


#
# data = r_c.read_csv(_path)
# print(data)
#print(e_d.edit_data(data)[0])
