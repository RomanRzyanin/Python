import csv
import string
import random as r
from memory_profiler import profile
import datetime

start = datetime.datetime.now()
print('Время старта: ' + str(start))


#@profile
def func():
    with open('test_gen.csv', 'w', newline='', encoding='utf-8') as cs_f:
        res = []

        for i in range(1, 10001):
            name_lst = ''.join(r.choices(string.ascii_lowercase, k=r.randint(4, 12))).title()
            tmp = {'level': r.randint(1, 7),
                   'id': str(i).zfill(10),
                   'name': name_lst,
                   'hash': hash(name_lst)}
            res.append(tmp)
        writer = csv.DictWriter(cs_f, fieldnames=res[0].keys())
        writer.writeheader()
        writer.writerows(res)



if __name__ == '__main__':
    func()

finish = datetime.datetime.now()
print('Время окончания: ' + str(finish))

print('Время работы: ' + str(finish - start))
