'''Задание №2
✔ Напишите функцию, которая генерирует
псевдоимена.
✔ Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
'''

import random as r
__all__ = ['write_names']

def gen_name():
    vowels = ('a', 'i', 'e', 'u', 'o', 'y')
    lst = [chr(r.randint(97, 122)) for i in range(r.randint(4, 7))]
    if any(let in vowels for let in lst):
        return ''.join(lst).title() + '\n'
    return ''.join(lst).title() + r.sample(vowels, 1)[0] + '\n'


def write_names(n):
    for _ in range(n):
        with open('names.txt', 'a', encoding='utf-8') as f_n:
            f_n.write(gen_name())


# if __name__ == '__main__':
#     gen_name()
