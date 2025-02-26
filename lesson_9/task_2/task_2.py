'''Задание №2
Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами
из диапазонов.
'''
from random import randint


def check_range(func):
    def wrapper(*args):
        if 1 <= args[0] <= 10 and 1 <= args[1] <= 100:
            return func(args[0], args[1])
        return func(randint(1, 100), randint(1, 10))

    return wrapper


@check_range
def nums_request(num, attempts):
    def func():
        nonlocal num, attempts
        while attempts > 0:
            user_num = int(input('Enter your number: '))
            if user_num == num:
                return 'You win!'
            attempts -= 1
        return f'The attempts are over and you have lost {num=}, {attempts=}'

    return func


#print(check_range(nums_request)(100, 60))
num = int(input('Загадайте число от 1 до 100: '))
attempt = int(input('Установите число попыток от 1 до 10: '))
user_game = nums_request(num, attempt)
print(user_game())
