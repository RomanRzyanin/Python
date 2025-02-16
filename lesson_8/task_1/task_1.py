'''Задание №1
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее
файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
'''

import json
def save_json(name):
    with open('new_file.txt', 'r', encoding='utf-8') as f:
        my_file = f.readlines()
    my_dict = {el.split(':')[0].strip().title():  el.split(':')[1].rstrip('\n').strip() for el in my_file}
    with open(name + '.json', 'w', encoding='utf-8') as f_2:
        json.dump(my_dict, f_2, indent=2)


if __name__ == '__main__':
    save_json(input('Enter name file: '))
