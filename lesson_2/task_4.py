'''task_№4
✔ Напишите программу, которая вычисляет площадь
круга и длину окружности по введённому диаметру.
✔ Диаметр не превышает 1000 у.е.
✔ Точность вычислений должна составлять
не менее 42 знаков после запятой.
'''
import decimal
import math

decimal.getcontext().prec = 120

def get_area(d):
    pi = decimal.Decimal(math.pi)
    d = decimal.Decimal(d)
    s = pi * (d / 2) ** 2
    l = pi * d
    return s, l


print(f'S = {get_area(111.097876674354354232)[0]}', f'L = {get_area(111)[1]}', sep='\n')

print(decimal.Decimal((1 + 5 ** 0.5) / 2))
print(decimal.Decimal(math.pi))

data: list[int | str | bool] = [5, 're', False]