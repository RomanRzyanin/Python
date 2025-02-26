'''Задача 4. Кэширование для ускорения вычислений
Создайте декоратор, который кэширует (сохраняет для дальнейшего использования)
результаты вызова функции и, при повторном вызове с теми же аргументами,
возвращает сохранённый результат.
Примените его к рекурсивной функции вычисления чисел Фибоначчи.
В итоге декоратор должен проверять аргументы, с которыми вызывается функция, и,
если такие аргументы уже использовались, должен вернуть сохранённый результат
вместо запуска расчёта.
'''

from functools import wraps
from time import time

def cash_func(func):
    my_cash = {}
    @wraps(func)
    def wrapper(*args):
        start = time()
        #my_cash = {}
        if args in my_cash:
            print('Данные из кэша')
            return my_cash[args]
        else:
            my_cash[args] = func(*args)
            return my_cash[args]

    return wrapper

@cash_func
def fibonacci(n):
    print(f'Вычисление числового ряда Фибоначчи для числа: {n}')
    n1 = n
    res = [1, 1]
    fib1 = fib2 = 1
    while n - 2 > 0:
        fib1, fib2 = fib2, fib1 + fib2
        res.append(fib2)
        n -= 1
    return f'Числовой ряд Фибоначчи числа {n1} = {res}'

import timeit
# # код, время выполнения которого нужно измерить
# code_to_test = """ a = range(1000000) b = [] for i in a: b.append(i*2) """
# # вычисление времени выполнения кода
# elapsed_time = timeit.timeit(code_to_test, number=2)/2
# print('Elapsed time: ', elapsed_time)


print(fibonacci(10))
print(fibonacci(11))
print(fibonacci(12))
print(fibonacci(10))
print(fibonacci(11))

