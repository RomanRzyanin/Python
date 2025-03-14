'''Задача 5. Модуль для проверки ферзей
Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него
напишите код, решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно
расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8
ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 -
координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют
- ложь.
'''

import sys
from lesson_6.hw_6.task_6 import hw6_task5_1 as hw5_1
#from lesson_6.hw_6.task_6 import hw6_task5_2 as hw5_2
# Проверяем количество аргументов командной строки
if len(sys.argv) != 9:
    print("Usage: python main.py row1 col1 row2 col2 ... row8 col8")
    sys.exit(1)

# Получаем координаты ферзей из аргументов командной строки
positions = [(int(sys.argv[i]), int(sys.argv[i + 1])) for i in range(1, len(sys.argv), 2)]

# Проверяем, не бьют ли ферзи друг друга
if hw5_1.are_queens_safe(positions):
    print("True")
else:
    print("False")
