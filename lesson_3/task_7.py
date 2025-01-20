'''Задание №7
Погружение в Python | Коллекции
✔ Пользователь вводит строку текста.
✔ Подсчитайте сколько раз встречается
каждая буква в строке без использования
метода count и с ним.
✔ Результат сохраните в словаре, где ключ —
символ, а значение — частота встречи
символа в строке.
✔ Обратите внимание на порядок ключей.
Объясните почему они совпадают
или не совпадают в ваших решениях.'''

text = 'to be or not to be'
my_dict = {}
for el in text:
    if el.isalpha():
        val = text.lower().count(el)
        my_dict[el] = val
print(my_dict)

my_dict1 = {}
for el in text:
    if el.isalpha():
        cnt = 0
        for elem in text:
            if elem == el:
                cnt += 1
        my_dict1[el] = cnt

print(my_dict1)

my_dict2 = {}
for el in text:
    if el.isalpha():
        my_dict2[el] = my_dict2.get(el, 0) + 1

print(my_dict2)

result = {el: text.count(el) for el in text.lower() if el.isalpha()}
print(result)