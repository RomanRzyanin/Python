'''Задача 2. Модуль для удаления дублирующихся подряд символов
Напишите модуль с функцией, которая принимает строку и возвращает строку с
удаленными дублирующимися подряд идущими символами. Например, строка
"aabbccaa" должна быть преобразована в "abca".'''

__all__ = {'delete_duplicates'}


def delete_duplicates(s):
    '''функцией, которая принимает строку и возвращает строку с
удаленными дублирующимися подряд идущими символами.'''
    if not s:
        return s
    res = [s[0]]
    for el in s[1:]:
        if el != res[-1]:
            res.append(el)
    return ''.join(res)


# str_1 = "aabbccaa"
# s = delete_duplicates(str_1)
# print(s)

if __name__ == '__main__':
    delete_duplicates()
