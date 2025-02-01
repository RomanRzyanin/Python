'''Задание №1
✔ Вручную создайте список с целыми числами, которые
повторяются. Получите новый список, который содержит
уникальные (без повтора) элементы исходного списка.
✔ *Подготовьте два решения, короткое и длинное, которое
не использует другие коллекции помимо списков.'''

my_list = [1, 2, 4, 5, 6, 8, 2, 3, 4, 5, 7, 4, 14, 5, 4, 14, 4, 14]
my_list_u_shot = list(set(my_list))
print(f'{my_list = }\n{my_list_u_shot = }')

my_list_u_long = []
for el in my_list:
    if el not in my_list_u_long:
        my_list_u_long.append(el)
my_list_u_long.sort()
my_list_c = my_list_u_long

print(f'{my_list = }\n{my_list_u_long = }')
print((my_list_u_long) == (my_list_u_shot))
print(type(my_list_u_long), type(my_list_u_shot))
print(id(my_list_u_long), id(my_list_u_shot))
print(id(my_list_u_long), id(my_list_c))
