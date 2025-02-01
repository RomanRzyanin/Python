import hw6_task2 as hw6_2


def in_text():
    s = input('Введите строку: ')
    print(f'Исходная строка: {s} \nСтрока с удаленными дубликатами:  {hw6_2.delete_duplicates(s)}.')


if __name__ == '__main__':
    in_text()
