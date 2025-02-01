'''Задание №2
� Создайте модуль с функцией внутри.
� Функция принимает на вход три целых числа: нижнюю и
верхнюю границу и количество попыток.
� Внутри генерируется случайное число в указанных границах
и пользователь должен угадать его за заданное число
попыток.
� Функция выводит подсказки “больше” и “меньше”.
� Если число угадано, возвращается истина, а если попытки
исчерпаны - ложь.
'''

import random as r

__all__ = ['guess_the_number']


# def rock_paper_scissors():
#     '''Функция игры «Камень, ножницы, бумага»'''
#     print('Добро пожаловать в игру: "Камень, ножницы, бумага"')
#     print('Правила игры «Камень, ножницы, бумага»: программа запрашивает у \
# пользователя строку и выводит, победил он или проиграл. \nКамень бьёт \
# ножницы, ножницы режут бумагу, бумага кроет камень.')
#     choice_comp = {1: 'rock', 2: 'paper', 3: 'scissor'}
#     dot = True
#     while dot:
#         x_comp = r.randint(1, 3)
#         choice_gamer = input(f'Ваш выбор:\n 1 - Камень \n 2 - Бумага \n 3 - Ножницы \n '
#                              f'4 - Exit to Main menu \n 5 - Exit of the game\n>>> ')
#         match choice_gamer:
#             case '1':
#                 if x_comp == 1:
#                     print(f'Drawn game. You -> {choice_comp[1]}, Computer -> {choice_comp[x_comp]}')
#                 elif x_comp == 2:
#                     print(f'You lose. You -> {choice_comp[1]}, Computer -> {choice_comp[x_comp]}')
#                 else:
#                     print(f'You WIN!!! You -> {choice_comp[1]}, Computer -> {choice_comp[x_comp]}')
#             case '2':
#                 if x_comp == 1:
#                     print(f'You WIN!!! You -> {choice_comp[2]}, Computer -> {choice_comp[x_comp]}')
#                 elif x_comp == 2:
#                     print(f'Drawn game. You -> {choice_comp[2]}, Computer -> {choice_comp[x_comp]}')
#                 else:
#                     print(f'You lose. You -> {choice_comp[2]}, Computer -> {choice_comp[x_comp]}')
#             case '3':
#                 if x_comp == 1:
#                     print(f'You lose. You -> {choice_comp[3]}, Computer -> {choice_comp[x_comp]}')
#                 elif x_comp == 2:
#                     print(f'You WIN!!! You -> {choice_comp[3]}, Computer -> {choice_comp[x_comp]}')
#                 else:
#                     print(f'Drawn game. You -> {choice_comp[3]}, Computer -> {choice_comp[x_comp]}')
#             case '4':
#                 dot = False
#             case '5':
#                 print('Goodbye', 'We are waiting for you again', sep='\n')
#                 exit()
#             case _:
#                 print('Введите число от 1 до 4: ')


def guess_the_number(a, b, c):
    '''Функция игры "Угадай число"'''
    print('Добро пожаловать в игру: "Угадай число"')
    print(f'Угадайте число от {a} до {b} которое задумал компьютер.')
    dot = True
    while dot:
        digit = r.randint(a, b)
        cnt = 0
        # print(x)
        while dot:
            cnt += 1
            if cnt - 1 == c:
                print(f'Вы использовали все {c} попытoк и не угадали число {digit}')
                dot = False
            # print('Добрый день игрок! Угадайте число от 1 до 100')
            else:
                answer = int(input('Введите ваш ответ: '))
                if answer > digit:
                    print(f'Слишком много, поробуйте еще.')
                    print(f'У вас осталось {c - cnt} попытка. \n' if c - cnt == 1 else f'У вас осталось {c - cnt} попытки. \n' if 1 < c - cnt < 5 else f'У вас осталось {c - cnt} попыток.')
                elif answer < digit:
                    print(f'Слишком мало, поробуйте еще.')
                    print(f'У вас осталось {c - cnt} попытка. \n' if c - cnt == 1 else f'У вас осталось {c - cnt} попытки. \n' if 1 < c - cnt < 5 else f'У вас осталось {c - cnt} попыток.')
                elif answer == digit:
                    print(f'Правильно! Ответ = {digit}, вы угадали с {cnt} попытки\n')
                    dot = False

        choice_gamer = input('Хотите сыграть еще:\n 1 - да\n 2 - нет\n 3 - Exit of the game\n>>> ')
        match choice_gamer:
            case '1':
                dot = True
            case '2':
                dot = False
            case '3':
                print('Goodbye', 'We are waiting for you again', sep='\n')
                exit()
            case _:
                print('Введите число от 1 до 3: ')


# def main_menu():
#     '''Функция главного меню'''
#     print('<<< Давайте поиграем >>>\n')
#     while True:
#         option = input(f'Выберите действие:\n 1 - Запустить игру «Камень, ножницы, бумага» : '
#                        f'\n 2 - Запустить игру «Угадай число» : \n 3 - Exit \n >>> ')
#         match option:
#             case '1':
#                 pass
#                 #rock_paper_scissors()
#             case '2':
#                 guess_the_number()
#             case '3':
#                 print('Goodbye', 'We are waiting for you again', sep='\n')
#                 exit()
#             case _:
#                 print('Введите число от 1 до 3: ')


if __name__ == '__main__':
    guess_the_number()
