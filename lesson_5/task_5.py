'''Задание №5
✔ Напишите программу, которая выводит
на экран числа от 1 до 100.
✔ При этом вместо чисел, кратных трем,
программа должна выводить слово «Fizz»
✔ Вместо чисел, кратных пяти — слово «Buzz».
✔ Если число кратно и 3, и 5, то программа
должна выводить слово «FizzBuzz».
✔ *Превратите решение в генераторное выражение.
'''

#my_iter = (i for i in range(101))
# for el in range(1, 101):
#     if el % 5 == 0 and el % 3 == 0:
#         print('FizzBuzz', end=' ')
#     elif el % 3 == 0:
#         print('Fizz', end=' ')
#     elif el % 5 == 0:
#         print('Buzz', end=' ')
#     else:
#         print(el, end=' ')

# for el in range(1, 101):
#     print('FizzBuzz') if el % 5 == 0 and el % 3 == 0 else print('Buzz') if el % 5 == 0 else print('Fizz') if el % 3 == 0 else print(el)
#     #print()

num_gen = ('FizzBuzz' if el % 5 == 0 and el % 3 == 0 else 'Buzz' if el % 5 == 0 else 'Fizz' if el % 3 == 0 else el for el in range(1, 101))
for el in num_gen:
    print(el, end=' ')