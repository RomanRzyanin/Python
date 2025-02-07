'''Задание №4
✔ Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.
'''

'''Преобразование текстовых строк в байтовые строки с использованием кодировок:
text_string = "Hello, world!"

# Преобразование в байтовую строку с кодировкой UTF-8
byte_string_utf8 = text_string.encode('utf-8')

# Преобразование в байтовую строку с кодировкой ASCII
byte_string_ascii = text_string.encode('ascii')'''

__all__ = ['create_new_files']

import random as r


def create_new_files(expansion, cnt=42, min_n=6, max_n=30, min_b=256, max_b=4096):
    for _ in range(cnt):
        name = ''.join((chr(r.randint(97, 122)) for _ in range(r.randint(min_n, max_n))))
        with open('D:\\GeekBrains\\2nd_year\\Python\\lesson_7\\task_4\\files\\' + name + '.' + expansion, 'wb') as f:
            text = ''.join((chr(r.randint(0, 1122)) for _ in range(r.randint(min_b, max_b))))
            f.write(text.encode('utf-8'))


#create_new_files('bin')


