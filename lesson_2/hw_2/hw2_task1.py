'''Задача 1.
Нахождение наибольшего общего делителя (НОД) двух
чисел'''
import  math

x = math.gcd(17, 51)
print(x)

def gdc_1(a, b):
    while b:
        a, b = b, a % b
    return a
print(gdc_1(51, 17))