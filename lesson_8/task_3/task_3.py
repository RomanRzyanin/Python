'''Задание №3
Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV'''

import json
import csv


def func():
    with (
        open('te.json', 'r', encoding='utf-8') as f_read,
        open('test.csv', 'w', encoding='utf-8', newline='') as f_write
    ):
        data = json.load(f_read)
        # for k, v in data.items():
        all_data = []
        tmp = []

        for k, v in data.items():
            if len(list(v.items())) == 0:
                continue
            else:
                for key, value in v.items():
                    tmp.append(k)
                    tmp.extend([key, value])
                    all_data.append(tmp)
                    tmp = []

        #print(all_data)

        writer = csv.writer(f_write, delimiter=',')
        writer.writerow(['level', 'id', 'name'])
        for el in all_data:
            writer.writerow(el)
            #print(el)
    #print(all_data)


func()

# res.write('id,level,name')
# for level, users_lst in data.items():
#     for user in users_lst:
#         res.write(f'\n{user["id"]},{level},{user["name"]}')
