'''Задание №1
Погружение в Python | Функции
✔ Напишите функцию, которая принимает строку текста.
Вывести функцией каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого
длинного слова был один пробел между ним и номером строки.'''


def print_words(text):
    '''The function of printing a new word with a new line'''
    words = sorted(text.lower().split())
    for i, w in enumerate(words, 1):
        print(f'{i:>3}.{w: >{len(max(words, key=len)) + 1}}')


text = input('Enter the text: ')

print_words(text)
