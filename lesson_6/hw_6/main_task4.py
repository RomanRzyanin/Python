import hw6_task4 as hw6_4


def true_data(data):
    '''Функция проверки существования даты'''
    d, m, y = (int(el) for el in data.split('.'))
    if y > 9999 or m > 12:
        return False
    m_30 = (4, 6, 9, 11)
    m_31 = (1, 3, 5, 7, 8, 10, 12)
    if m in m_30:
        if 0 < d < 31:
            return True
        else:
            return False
    elif m in m_31:
        if 0 < d < 32:
            return True
        return False
    elif m == 2:
        if hw6_4.__year_func(y):
            if 0 < d < 29:
                return True
            else:
                return False
        else:
            if 0 < d < 30:
                return True
        return False


def main_f():
    data = input('Введите дату в формате дд.мм.гггг: ')
    if true_data(data):
        print('Дата может существовать.')
    else:
        print('Такая дата невозможна.')


if __name__ == '__main__':
    main_f()
