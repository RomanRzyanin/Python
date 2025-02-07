'''Задание №1
✔ Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции. '''
import random as r

def rnd_nums():
    return f'{str(r.randint(-1000, 1000)):>4} | {str(round(r.uniform(-1000, 1000), 3)):<6}\n'
def enter_digit(n, name):
    with open(name + '.txt', 'a', encoding='utf-8') as f:
        for _ in range(n):
            f.write(rnd_nums())


if __name__ == '__main__':
    enter_digit()
