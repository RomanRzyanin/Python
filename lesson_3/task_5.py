'''Задание №5
Погружение в Python | Коллекции
✔ Создайте вручную список с повторяющимися целыми числами.
✔ Сформируйте список с порядковыми номерами
нечётных элементов исходного списка.
✔ Нумерация начинается с единицы.'''

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 21, 245, 6, 67, 35, 45, 25, 56, 67, 87, 6, 83, 745, 634, 534, 654, 7655, 87, 86]

res = []
for i in range(len(lst)):
    if lst[i] % 2:
        res.append(i + 1)

print(res)

res_1 = [i + 1 for i in range(len(lst)) if lst[i] % 2 != 0]
print(res_1)

res_2 = [i for i, el in enumerate(lst, 1) if el % 2]
print(res_2)