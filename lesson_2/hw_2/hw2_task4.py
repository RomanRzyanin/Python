'''Задача 4.
Сумма и произведение дробей'''

from fractions import Fraction


def sum_fraction(f_1, f_2):
    numerator_1, denominator_1 = map(int, f_1.split('/'))  # Получаем числитель и знаменатель первой дроби
    numerator_2, denominator_2 = map(int, f_2.split('/'))  # Получаем числитель и знаменатель второй дроби
    f1 = Fraction(numerator_1, denominator_1)  # Fraction для первой и второй дроби
    f2 = Fraction(numerator_2, denominator_2)  # Fraction для первой и второй дроби
    sum_frac = f1 + f2  # сумму дробей
    return sum_frac


def prod_fraction(f_1, f_2):
    numerator_1, denominator_1 = map(int, f_1.split('/'))  # Получаем числитель и знаменатель первой дроби
    numerator_2, denominator_2 = map(int, f_2.split('/'))  # Получаем числитель и знаменатель второй дроби
    f1 = Fraction(numerator_1, denominator_1)  # Fraction для первой и второй дроби
    f2 = Fraction(numerator_2, denominator_2)  # Fraction для первой и второй дроби
    product_frac = f1 * f2  # произведение дробей
    return product_frac


f_1 = input("Введите первую дробь (a/b): ")
f_2 = input("Введите вторую дробь (a/b): ")

print("Сумма:", sum_fraction(f_1, f_2))
print("Произведение:", prod_fraction(f_1, f_2))
