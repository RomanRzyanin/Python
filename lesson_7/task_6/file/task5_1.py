'''Задание №5
✔ Доработаем предыдущую задачу.
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи.
'''

__all__ = ['create_new_files']

import random as r


def create_new_files(expansion, cnt=42, min_n=6, max_n=30, min_b=256, max_b=4096):
    for _ in range(cnt):
        name = ''.join((chr(r.randint(97, 122)) for _ in range(r.randint(min_n, max_n))))
        with open('D:\\GeekBrains\\2nd_year\\Python\\lesson_7\\task_5\\files\\' + name + '.' + expansion, 'wb') as f:
            text = ''.join((chr(r.randint(0, 1122)) for _ in range(r.randint(min_b, max_b))))
            f.write(text.encode('utf-8'))
