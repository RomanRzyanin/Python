'''Задание №2
Напишите функцию, которая в бесконечном цикле
запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в
JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо
от уровня доступа.
При перезапуске функции уже записанные в файл данные
должны сохраняться.
'''
import json


def read_file(filename):
    '''function reading file'''
    try:
        with open(filename, 'r', encoding='utf-8') as f_read:
            data = json.load(f_read)
    except FileNotFoundError:
        data = {str(i): dict() for i in range(1, 8)}
    return data


def write_file(filename, data):
    '''function writing file'''
    with open(filename, 'w', encoding='utf-8') as f_write:
        json.dump(data, f_write, indent=4, ensure_ascii=False)


def add_users():
    '''main function'''
    filename = input('Введите название файла: ') + '.json'
    while True:
        options = input('Выберите действие: 1 - добавить пользователя, 2 - выйти из программы: ')

        match options:
            case '1':
                data = read_file(filename)
                #print(data)

                name = input('Ввведите имя: ')
                user_id = input('Введите ваш id: ')
                level = input('Введите ваш уровень доступа: ')

                list_id = []
                for i in range(1, 8):
                    list_id.extend(data[str(i)])
                #print(list_id)
                if user_id not in list_id:
                    data[level].update({user_id: name})
                else:
                    print(f'Пользователь с {user_id = } уже существует.')

                write_file(filename, data)

            case '2':
                print('Goodbye', 'We are waiting for you again', sep='\n')
                exit()
            case _:
                print('Введите число от 1 до 2: ')


if __name__ == '__main__':
    add_users()
