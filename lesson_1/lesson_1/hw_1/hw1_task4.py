'''task_4.
Яма
Представьте, что вы разрабатываете компьютерную игру с текстовой графикой.
Вам поручили создать генератор ландшафта. Напишите программу, которая
получает на вход число N и выводит на экран числа в виде ямы'''


def hole(n):
    for i in range(n):
        for j in range(n, n - i - 1, -1):
            print(j, end='')
        point_cnt = 2 * (n - i - 1)
        print("." * point_cnt, end='')
        for right_number in range(n - i, n + 1):
            print(right_number, end='')
        print()

n = int(input('Enter the depth of the pit: '))
hole(n)