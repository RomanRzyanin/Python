from random import choices, randint
from string import ascii_lowercase


def func_1(ext, files=42, min_len=6, max_len=30, min_bytes=256, max_bytes=4096):
    for _ in range(files):
        name = ''.join(choices(ascii_lowercase, k=randint(min_len, max_len))) + ext
        with open('D:\\GeekBrains\\2nd_year\\Python\\lesson_7\\task_4\\f2\\' + name, 'w') as f:
            pass


def func_2(files=10, **kwargs):
    # values = []
    # for value in kwargs.values():
    #     values.append(value)
    for _ in range(files):
        ext = str(*choices(list(kwargs.values())))
        func_1(ext, 5)

#func_1('.txt')
func_2(5, a='.txt', b='.doc', c='.bin')