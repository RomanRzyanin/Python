'''Задача 2.
Поиск наибольшего числа в списке
Напишите программу, которая принимает список чисел через строку и
возвращает наибольшее число в этом списке.
'''
text = '1 2 3 3 4 5 6 7 8 9 6 34 56 5 7 2 13 1 4 46 457 56 43'
print(max([int(i) for i in text.split()]))