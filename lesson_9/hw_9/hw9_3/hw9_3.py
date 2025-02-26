'''Задача 3. Счётчик
Реализуйте декоратор counter, считающий и выводящий количество вызовов
декорируемой функции.
Для решения задачи нельзя использовать операторы global и nonlocal.'''
from functools import wraps


def counter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f'The function {func.__name__} started {wrapper.count}')
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper


@counter
def greeting(name, age):
    if age:
        return f'Ого, {name}! Тебе уже {age} лет, ты быстро растешь!'
    else:
        return f'Привет, {name}!'


@counter
def greeting2(name):
    return f'Привет, {name}!'


def main():
    print(greeting2('Том'))  # Вызов функции greeting с одним аргументом.
    print(greeting("Миша", 100))  # Вызов функции greeting с двумя     аргументами.
    print(greeting2("Маша"))  # Вызов функции greeting2.
    print(greeting("Катя", 16))   # Вызов функции greeting с именем и     возрастом.


main()
