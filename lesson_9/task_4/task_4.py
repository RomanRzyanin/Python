'''Задание №4
Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой
функции.'''
from functools import wraps


def count_func(cnt):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # result = []
            for i in range(cnt):
                print(f'{i + 1:<3}-й запуск функции {func.__name__}({args[0]}) = {func(*args, **kwargs)}')

        return wrapper

    return decorator


@count_func(10)
def factorial(n):
    '''Факториал числа n'''
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


factorial(100)
print(f'{factorial.__name__ = }')
help(factorial)
