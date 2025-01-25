'''Задание №6
✔ Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка.
'''


def sum_list(id_1, id_2, lst):
    '''Функция получает на вход список чисел и два индекса.
    ✔ Вернуть сумму чисел между переданными индексами.
    ✔ Если индекс выходит за пределы списка, сумма считается
    до конца и/или начала списка'''
    if id_1 >= id_2:
        print('no element')
    elif id_1 < 0 and id_2 > len(lst):
        return sum(lst)
    elif id_1 < 0:
        return sum(lst[:id_2])
    elif id_2 > len(lst):
        return sum(lst[id_1 + 1:])
    else:
        return sum(lst[id_1 + 1: id_2])



lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum_list(4, 8, lst))
print(sum(lst[4: len(lst) + 1]))


def test(id_1, id_2, lst):
    lst_i = sorted([id_1, id_2])
    return sum(el for el in lst if lst.index(el) in range(lst_i[0] + 1, lst_i[1]))

print(test(4, 8, lst))