'''Задание №3
Погружение в Python | Коллекции
✔ Создайте вручную кортеж содержащий элементы разных типов.
✔ Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа.'''

import time

my_dict = {'one': 1, 'two': 2}
my_tuple = ((1, 2, 3), 'text', 2, 4, 6, False, True, [1, 2], (1, 2), {1, 2}, my_dict, 2.3, None, None)
res_d = dict()
start_1 = time.time()
for el in my_tuple:
    el_type = type(el)
    lst = []
    for elem in my_tuple:
        if type(elem) == el_type:
            lst.append(elem)
    res_d[el_type] = lst
    # if type(el) not in res_d:
    #     res_d[type(el)] = list().append(el)
    # else:
    #     res_d[type(el)].values().append(el)
stop_1 = time.time()
print(res_d)

dict_obj = {}
start_2 = time.time()
for el in my_tuple:
    dict_obj.setdefault(type(el), []).append(el)
stop_2 = time.time()
print(dict_obj)

time_1 = (stop_1 - start_1)
time_2 = (stop_2 - start_2)
print(time_1, time_2)