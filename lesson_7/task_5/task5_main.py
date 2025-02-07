from lesson_7.task_5.file import task5_1 as t5_1
import random as r


def many_files(count, expansion):
    for el in expansion:
        t5_1.create_new_files(el, r.randint(1, count))


cnt, *args = input(
    'Введите через пробел число = макс кол-ву файлов каждого расширения и все необходимые расширения: ').split()

if __name__ == '__main__':
    many_files(int(cnt), args)
