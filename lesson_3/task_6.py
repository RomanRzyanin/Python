'''Задание №6
Погружение в Python | Коллекции
Пользователь вводит строку текста. Вывести каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого длинного
слова был один пробел между ним и номером строки.'''

text = 'to be or not to be'.split()
max_l = len(max(text, key=len))
for i, el in enumerate(sorted(text), 1):
    print(f'№{i}) {el:>{max_l}}')

print(max_l)