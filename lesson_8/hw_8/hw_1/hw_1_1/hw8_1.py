'''Задание 1. Работа с основными данными
Напишите функцию, которая получает на вход директорию и рекурсивно обходит
её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и
pickle. Для дочерних объектов указывайте родительскую директорию. Для
каждого объекта укажите файл это или директория. Для файлов сохраните его
размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных
файлов и директорий. Соберите из созданных на уроке и в рамках домашнего
задания функций пакет для работы с файлами разных форматов.'''

import scan_dir
import save_to_pickle
import save_to_csv
import save_to_json



def main_func(directory):
    data = scan_dir.scan_dir(directory)
    #print(data)

    save_to_json.save_to_json(data, 'directory_info.json')
    save_to_csv.save_to_csv(data, 'directory_info.csv')
    save_to_pickle.save_to_pickle(data, 'directory_info.pkl')


#if __name__ == '__main__':
main_func('D:/GeekBrain/2nd_year/Python/lesson_8')
