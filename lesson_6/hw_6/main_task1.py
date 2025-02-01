import hw6_task1 as hw6

def in_text():
    text = input('Введите текст: ')
    print(f'Cловарь {hw6.count_words(text)}, в котором ключи — это слова, а значения — количество их повторений.')

if __name__ == '__main__':
    in_text()