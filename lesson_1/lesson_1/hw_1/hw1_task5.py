'''task_5.
Игра «Компьютер угадывает число»
Мальчик загадывает число между 1 и 100 (включительно). Компьютер может
спросить у мальчика: «Твоё число равно, меньше или больше, чем число N?»,
где N — число, которое хочет проверить компьютер. Мальчик отвечает одним из
трёх чисел: 1 — равно, 2 — больше, 3 — меньше.
Напишите программу, которая с помощью цепочки таких вопросов и ответов
мальчика угадывает число.
Дополнительно: сделайте так, чтобы можно было гарантированно угадать
число за семь попыток.
'''


# import random
# res = True
# while res:
#     x = random.randint(1, 100)
#     #print(x)
#     while res:
#         print('Добрый день игрок! Угадайте число от 1 до 100')
#         answer = int(input('Введите ваш ответ: '))
#         if answer > x:
#             print('Слишком много, поробуйте еще.\n')
#         elif answer < x:
#             print('Слишком мало, поробуйте еще.\n')
#         elif answer == x:
#             print(f'Правильно! Ответ = {x}\n')
#             res = False
#     game = input('Хотите сыграть еще, да/нет:')
#     if game == 'да':
#         res = True
#     else:
#         print('До свидания')
#         res = False

def game():
    start = 1
    finish = 100
    dot = True
    cnt = 1
    # answer = {1: 'равно', 2: 'больше', 3: 'меньше'}
    print('Загадайте число от 1 до 100')
    while dot:
        n = (start + finish) // 2
        print('Ваше число: равно, больше или меньше, числа - ', n)
        ans = int(input('1 - равно, 2 - больше, 3 - меньше: \n'))
        # try:
        #     ans not in (1, 2, 3)
        # except:
        #     print('Введите числа: 1, 2, 3')
        # else:
            if ans == 1:
                print(f'Вы загадали число {n}, угадано с {cnt} попытки.')
                game_loop = int(input('Сыграем еще?: 1 - да, 2 - нет: \n'))
                if game_loop == 2:
                    print('До свидания.')
                    dot = False
                else:
                    start = 1
                    finish = 100
                    cnt = 1
            elif ans == 2:
                start = n
            elif ans == 3:
                finish = n
            cnt += 1


game()
