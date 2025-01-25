'''Задача 3. Число наоборот
Пользователь вводит два числа: N и K. Напишите программу, которая заменяет
каждое число на число, которое получается из исходного записью его цифр в
обратном порядке, затем складывает их, снова переворачивает и выводит
ответ на экран.
Пример:
Введите первое число: 102
Введите второе число: 123
Первое число наоборот: 201
Второе число наоборот: 321
Сумма: 522
Сумма наоборот: 225'''


def revers_digit(digit):
    '''Функция заменяет каждое число на число,
    которое получается из исходного записью его цифр в обратном порядке'''
    lst = [int(i) for i in digit.lstrip('0')][::-1]
    res = 0
    for i in range(len(lst)):
        res += lst[i] * 10 ** (len(lst) - i - 1)
    return res

# digit = '34567'
# print(revers_digit(digit))

a = input('Введите число a = ')
b = input('Введите число b = ')
sum = int(a) + int(b)
print(f'Число a = {int(a)}\nЧисло a наоборот = {revers_digit(a)}')
print(f'Число b = {int(b)}\nЧисло a наоборот = {revers_digit(b)}')
print(f'Сумма a + b =  {sum }\nСумма a + b наоборот = {revers_digit(str(sum))}')