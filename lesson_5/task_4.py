'''Задание №4
✔ Создайте генератор чётных чисел от нуля до 100.
✔ Из последовательности исключите
числа, сумма цифр которых равна 8.
✔ Решение в одну строку.
'''

my_iter = (i for i in range(0, 101, 2) if sum([int(el) for el in str(i)]) != 8) #if sum([int(el) for el in str(i)]) != 8 # if i % 10 + i // 10 & 10 != 8

for el in my_iter:
    print(el, end=' ')
print()
print(type(my_iter))