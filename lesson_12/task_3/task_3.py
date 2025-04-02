'''Задание №3
Создайте класс-генератор.
Экземпляр класса должен генерировать факториал числа в
диапазоне от start до stop с шагом step.
Если переданы два параметра, считаем step=1.
Если передан один параметр, также считаем start=1.
'''

from math import factorial


class MyFactorial:
    # results = dict()
    def __init__(self, start, stop=None, step=1):
        # self.start = start
        if stop is None:
            start, stop = 1, start
        self.start = start
        self.stop = stop
        self.step = step
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.step <= 0:
            raise ValueError('The step should only be positive')
        res = factorial(self.current)
        self.current += self.step
        if self.current > self.stop:
            raise StopIteration
        return res

    def __str__(self):
        return f'Factorial: start = {self.start}, stop = {self.stop}, step = {self.step}, {self.current}! =>'


f = MyFactorial(5, 19, 2)
for i in f:
    print(f, i)
