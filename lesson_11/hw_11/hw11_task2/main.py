from random import choice
from hw11_2 import Water, Fire, Air, Soil, Dust

CNT = 10


def main():
    elements = [Water(), Fire(), Air(), Soil(), Dust()]
    try_count = 0
    while try_count < CNT:
        element_1 = choice(elements[:-1])
        element_2 = choice(elements)
        result = element_1 + element_2
        if result is None or element_1 == Dust():
            continue
        try_count += 1
        print(f'Волшебство №{try_count}')
        print(f' Вы соединили {element_1} & {element_2} и получили {result.answer}')
        print()


if __name__ == '__main__':
    main()
