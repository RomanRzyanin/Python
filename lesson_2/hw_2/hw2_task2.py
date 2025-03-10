'''Задание 2.
Преобразование числа в шестнадцатеричное
представление'''


def get_hex(number):
    hex_string = ''
    hex_digits = '0123456789ABCDEF'
    # for number in numbers:
    if number == 0:
        hex_string = '0'
    else:
        is_negative = number < 0
        if is_negative:
            number = -number

    hex_string = ''
    while number > 0:
        remainder = number % 16
        hex_string = hex_digits[remainder] + hex_string
        number //= 16

    if is_negative:
        hex_string = '-' + hex_string
    print(hex_string)


get_hex(56716745)

print(hex(56716745))