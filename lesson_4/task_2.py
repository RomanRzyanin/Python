'''Задание №2
✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
'''

def encoding_string(text):
    '''The function of printing list  unicum  elements and their code on utf-8'''
    res = []
    text_symbol = ''.join(text.split())
    text_set = sorted(list(set(text_symbol)))
    for el in text_set:
        res.append((el, ord(el)))
    #result = sorted(res, key=res[1])
    return res

x = encoding_string('Enter the text')
print(x)