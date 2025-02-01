'''Задание №7
� Создайте модуль и напишите в нём функцию, которая
получает на вход дату в формате DD.MM.YYYY
� Функция возвращает истину, если дата может существовать
или ложь, если такая дата невозможна.
� Для простоты договоримся, что год может быть в диапазоне
[1, 9999].
� Весь период (1 января 1 года - 31 декабря 9999 года)
действует Григорианский календарь.
� Проверку года на високосность вынести в отдельную
защищённую функцию.'''

__all__ = {'true_data', 'my_data'}

my_data = '30.02.2012'


def __year_func(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return False
    return True


def true_data(data):
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
        if __year_func(y):
            if 0 < d < 29:
                return True
            else:
                return False
        else:
            if 0 < d < 30:
                return True
        return False

if __name__ == '__main__':
    true_data()