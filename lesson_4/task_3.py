'''Задание №3
✔ Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно.
'''


def func_digit(text):
    '''The function return of dictionary key - code on utf-8, value - integer'''
    return {chr(int(el)): int(el) for el in sorted((text.split()))}


digit = input('Enter two integers separated by spaces: ')
print(func_digit(digit))
