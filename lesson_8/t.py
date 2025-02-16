import json
#
# my_dict = {}
# my_dict.setdefault(1, {2: 'roman'})
# my_dict[1].update({3: 'borat'})
# my_dict[1].update({7: 'de-borat'})
# my_dict.setdefault(3, {3: 'john'})
# my_dict[3].update({7: 'de-generat'})
# print(my_dict)
#
# with open('test.json', 'w', encoding='utf-8') as f_2:
#     json.dump(my_dict, f_2, indent=4)

# data = {str(i): dict() for i in range(1, 8)}
# print(data)
#
# print(my_dict[1].keys())

# a = 'Hello world!'
# b = {k: v for k, v in enumerate(a)}
# c = json.dumps(b, indent=3) #separators=('; ', '= ')
# print(c)
# with open('t.json', 'w', encoding='utf-8')as f:
#     for el in c.split('\n'):
#         json.dump(el, f, indent=4, ensure_ascii=False)

# import string
#
# print(string.ascii_lowercase)

from memory_profiler import profile
import datetime
from random import randint as r

start = datetime.datetime.now()


def fib(n):
    res = (r(1, 1000) for _ in range(100000))
    if n < 3:
        return n
    return fib(n - 1) + fib(n - 2)

@profile
def func(n):
    return fib(n)


print(func(7))
finish = datetime.datetime.now()
print('Время старта: ' + str(start))
print('Время окончания: ' + str(finish))

print('Время работы: ' + str(finish - start))
