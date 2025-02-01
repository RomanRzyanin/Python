'''Задание №3
� Улучшаем задачу 2.
� Добавьте возможность запуска функции “угадайки” из
модуля в командной строке терминала.
� Строка должна принимать от 1 до 3 аргументов: параметры
вызова функции.
� Для преобразования строковых аргументов командной
строки в числовые параметры используйте генераторное
выражение.'''

import task_2 as t
from sys import argv


def main_menu(args):
    '''Функция главного меню'''
    print('<<< Давайте поиграем >>>\n')
    while True:
        option = input(f'Выберите действие:\n 1 - Запустить игру «Камень, ножницы, бумага» : '
                       f'\n 2 - Запустить игру «Угадай число» : \n 3 - Exit \n >>> ')
        match option:
            case '1':
                pass
                # rock_paper_scissors()
            case '2':
                #a, b, c = (int(i) for i in input('Введите три числа через пробел: а - нижняя граница, в - верзняя граница, с - количество попыток: ').split())
                t.guess_the_number(args[0], args[1], args[2])
            case '3':
                print('Goodbye', 'We are waiting for you again', sep='\n')
                exit()
            case _:
                print('Введите число от 1 до 3: ')


if __name__ == '__main__':
    #main_menu()
    args = [int(el) for el in argv[1:]]
    #print(args)
    main_menu(args)