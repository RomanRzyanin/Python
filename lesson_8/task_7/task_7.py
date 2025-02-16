'''Задание №7
Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Распечатайте его как pickle строку.
'''

import csv
import pickle
from memory_profiler import profile
import datetime

start = datetime.datetime.now()



@profile
def csv_print():
    with open('test_gen.csv', 'r', newline='', encoding='utf-8') as cs_f:
        #data = list(csv.reader(cs_f))
        return pickle.dumps(list(csv.reader(cs_f)))


print(csv_print())
print(type(csv_print()))

finish = datetime.datetime.now()
print('Время старта: ' + str(start))
print('Время окончания: ' + str(finish))

print('Время работы: ' + str(finish - start))
