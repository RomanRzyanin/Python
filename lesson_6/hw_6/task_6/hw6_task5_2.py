

def generate_random_queens_placement():
    '''Генерирует случайную расстановку 8 ферзей.
    Возвращает:
    Список из 8 кортежей, каждый из которых содержит случайные
    координаты ферзя'''

    import random
    return [(i, random.randint(1, 8)) for i in range(8)]


def print_valid_placements(num_placements=4):
    '''
    Выводит заданное количество случайных валидных расстановок
    ферзей.
    Аргументы:
    num_placements -- количество случайных валидных расстановок для
    вывода'''

    count = 0
    while count < num_placements:
        placement = generate_random_queens_placement()
        if are_queens_safe(placement):
            print(placement)
            count += 1