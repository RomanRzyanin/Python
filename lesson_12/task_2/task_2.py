'''Задание №2
Доработаем задачу 1.
Создайте менеджер контекста, который при выходе
сохраняет значения в JSON файл.
'''

from math import factorial
from json import dump


class MyFactorial:
    # results = dict()
    def __init__(self, k):
        self.k = k
        self.history = []

    def __call__(self, n):
        res = factorial(n)
        self.history.append({n: res})
        self.history = self.history[-self.k:]
        return res

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('task_2.json', 'w', encoding='utf-8') as f:
            dump(self.history, f)

    def get_history(self):
        return self.history


f = MyFactorial(3)
with f as json_f:
    for i in range(1, 11):
        print(f'{i}! = {f(i)}')

print(f.get_history())
