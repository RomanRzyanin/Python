'''Задание №3
Напишите декоратор, который сохраняет в json файл
параметры декорируемой функции и результат, который она
возвращает. При повторном вызове файл должен
расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ
json словаря.
Для декорирования напишите функцию, которая может
принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой
функции.
'''

import json
import os


def save_json(file):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            data = {
                'function_name': func.__name__,
                'args': args,
                'kwargs': kwargs,
                'result': result
            }

            if os.path.exists(file):
                with open(file, 'r') as f_read:
                    js_data = json.load(f_read)

                js_data.append(data)

                with open(file, 'w') as f_write:
                    json.dump(js_data, f_write, indent=2)

            else:
                with open(file, 'w') as f_write:
                    json.dump([data], f_write, indent=2)

            return result

        return wrapper

    return decorator


@save_json('test.json')
def my_func(a, b, c=3, d=5):
    return a + b * c + d


my_func(1, 2, c=3, d=56)
my_func(4, 5, c=6, d=34)
# print(my_func.__name__)
