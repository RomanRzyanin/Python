'''Задание №6
✔ Выведите в консоль таблицу умножения
от 2х2 до 9х10 как на школьной тетрадке.
✔ Таблицу создайте в виде однострочного
генератора, где каждый элемент генератора —
отдельный пример таблицы умножения.
✔ Для вывода результата используйте «принт»
без перехода на новую строку.
'''

#
# for j in range (2, 10):
#     for i in range (2, 6):
#         print(i, '*', j, '=', i * j, end='   \t')
#     print()
# print()
# for j in range (2, 10):
#     for i in range (6, 10):
#         print(i, '*', j, '=', i * j, end='   \t')
#     print()


my_gen = (f'\n' if j == 11 else f'{i} * {j} = {j * i}'.ljust(15) for i in range(2, 10) for j in range(2, 12))
# print(*my_gen)

for el in my_gen:
    print(el, end=' ')
