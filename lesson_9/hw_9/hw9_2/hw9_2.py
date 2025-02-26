'''Задача 2. Замедление кода
В программировании иногда возникает ситуация, когда работу функции нужно
замедлить. Типичный пример — функция, которая постоянно проверяет,
изменились ли данные на веб-странице или её код.
Реализуйте декоратор, который перед выполнением декорируемой функции
ждёт несколько секунд.
'''

from functools import wraps
from time import sleep


def time_delay(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Задержка выполнения функции 10 сек.')
        sleep(10)
        return func(*args, **kwargs)

    return wrapper


@time_delay
def test_1():
    print('Test text number one')


@time_delay
def test_2():
    print('Test text number two')


if __name__ == '__main__':
    test_1()
    test_2()
