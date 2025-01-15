'''task_№5
✔ Напишите программу, которая решает
квадратные уравнения даже если
дискриминант отрицательный.
✔ Используйте комплексные числа
для извлечения квадратного корня.'''
from math import sqrt


# import complex


def sqrt_complex(a, b, c):
    d = b ** 2 - 4 * a * c
    if d == 0:
        x_1 = x_2 = -b / (2 * a)
    elif d > 0:
        x_1 = (sqrt(d) - b) / (2 * a)
        x_2 = (- d ** 0.5 - b) / (2 * a)
    else:
        real = round(-b / (2 * a), 4)
        imaginary = round(sqrt(abs(d)) / (2 * a), 4)
        x_1 = complex(real, imaginary)
        x_2 = complex(real, -imaginary)
    return x_1, x_2


res = sqrt_complex(10, -50, 100)
print(f'x_1 = {res[0]:.4f}, x_2 = {res[1]:.4f}')