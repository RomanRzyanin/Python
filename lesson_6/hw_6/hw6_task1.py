'''Задание 1. Модуль для подсчета количества повторений слов
Создайте модуль с функцией, которая получает список слов и возвращает
словарь, в котором ключи — это слова, а значения — количество их повторений
в списке.
'''

__all__ = {'count_words'}
def count_words(text):
    '''функцией, которая получает список слов и возвращает
словарь, в котором ключи — это слова, а значения — количество их повторений
в списке'''
    my_dict = {}
    for el in text.split():
        my_dict[el] = my_dict.get(el, 0) + 1
    # res = {el: (res.setdefault(el, 0) + 1) for el in text.split()}
    return my_dict


_test_text = 'aaee aaee kdfgk rgkg djk djk djk'
# print(count_words(test_text))

if __name__ == '__main__':
    count_words()