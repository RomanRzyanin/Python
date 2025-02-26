'''Задание №4
Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой
функции.'''
from functools import wraps


def count_func(cnt):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            count = 0
            res = None
            for _ in range(cnt):
                res = func(*args, **kwargs)
                count += 1
            return res, count

        return wrapper

    return decorator


#@count_func(10)
def factorial():
    '''Факториал числа n'''
    return 'Hello, world!'


#print(factorial())

print(count_func(10)(factorial)())