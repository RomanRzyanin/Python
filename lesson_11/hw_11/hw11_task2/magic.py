class Storm:
    answer = "Вы сложили Воду и Воздух и получили класс Шторм"


class Steam:
    answer = "Вы сложили Воду и Огонь и получили класс Пар"


class Mud:
    answer = "Вы сложили Воду и Землю и получили класс Грязь"


class Bolt:
    answer = "класс Молния"


class Dust:
    answer = "класс Пыль"

    def __str__(self):
        return 'Dust'

class Lava:
    answer = "класс Лава"


class Fog:
    answer = "класс Туман"


class Mistake:
    # def __str__(self):
    #     return 'Ваш уровень Магии не позволяет соединять эти элементы'
    answer = 'ииииии нихера не получили, потому-что вы не ребанный Гарри Потер'