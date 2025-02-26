'''Задание №1
Создайте функцию-замыкание, которая запрашивает два целых
числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток.
'''


def nums_request(num, attempts):
    def func():
        nonlocal num, attempts
        while attempts > 0:
            user_num = int(input('Enter your number: '))
            if user_num == num:
                return 'You win!'
            attempts -= 1
        return 'The attempts are over and you have lost'

    return func


# num = int(input('Загадайте число от 1 до 100: '))
# attempt = int(input('Установите число попыток от 1 до 10: '))
user_game = nums_request(15, 5)
print(user_game())
