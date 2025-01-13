'''task_3.
Простые числа
Напишите программу, которая считает количество простых чисел в заданной
последовательности и выводит ответ на экран.
Простое число делится только на себя и на единицу. Последовательность
задаётся при помощи вызова ввода (input) на каждой итерации цикла. Одна
итерация — одно число.'''


def prime_number(n):
    lst = []
    lst_res = []
    for _ in range(n):
        lst.append(int(input('Enter the number: ')))
    for el in lst:
        if el > 1:
            for i in range(2, el):
                if el % i == 0:
                    break
            else:
                lst_res.append(el)

    print('You enter numbers: ',  *lst, 'of which primes:', len(lst_res), ', prime numbers: ', *lst_res)


n = int(input('Enter number n: '))
prime_number(n)
