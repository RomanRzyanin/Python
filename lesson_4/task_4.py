'''Задание №4
✔ Функция получает на вход список чисел.
✔ Отсортируйте его элементы in place без использования
встроенных в язык сортировок.
✔ Как вариант напишите сортировку пузырьком.
Её описание есть в википедии.
'''
import random as r
import time as t
from timeit import timeit


def my_bubble_sort(lst_1):
    '''Bubble sort'''
    for i in range(1, len(lst_1)):
        for j in range(0, len(lst_1) - i):
            if lst_1[j] > lst_1[j + 1]:
                lst_1[j], lst_1[j + 1] = lst_1[j + 1], lst_1[j]
    return lst_1


'''Creating a list'''
my_lst = [r.randint(0, 1000) for i in range(10000)]

'''Coping lists'''
# my_lst_c = my_lst.copy()
# my_lst_c2 = my_lst.copy()
# my_lst_c3 = my_lst.copy()

'''Bubble sort'''
start_1 = t.time()
# res_1 = my_bubble_sort(my_lst[:])
stop_1 = t.time()
'''Function sorted()'''
start_2 = t.time()
res_2 = sorted(my_lst[:])
stop_2 = t.time()
'''Method .sort()'''
start_3 = t.time()
my_lst[:].sort()
stop_3 = t.time()

'''Time of sorted Bubble_sort'''
time_1 = (stop_1 - start_1) * 1000
'''Time of sorted Function sorted()'''
time_2 = (stop_2 - start_2) * 1000
'''Time of sorted Method .sort()'''
time_3 = (stop_3 - start_3) * 1000

print(timeit('my_bubble_sort(my_lst[:])', globals=globals(), number=10))

# print(f'{my_lst = } \n\n Bubble sort: \n  \n {time_1 = } \n\n Function sorted: \n  \n {time_2 = } '
#       f'\n\n Method sort \n  \n {time_3 = }')
