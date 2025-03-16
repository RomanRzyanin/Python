'''Для одной игры необходимо реализовать механику магии, где при соединении
двух элементов получается новый. У нас есть четыре базовых элемента:
«Вода», «Воздух», «Огонь», «Земля». Из них получаются новые: «Шторм»,
«Пар», «Грязь», «Молния», «Пыль», «Лава».
Таблица преобразований:
● Вода + Воздух = Шторм;
● Вода + Огонь = Пар;
● Вода + Земля = Грязь;
● Воздух + Огонь = Молния;
● Воздух + Земля = Пыль;
● Огонь + Земля = Лава.
Напишите программу, которая реализует все эти элементы. Каждый элемент
необходимо организовать как отдельный класс. Если результат не определён,
то возвращается None.
'''

from magic import Storm, Steam, Mud, Dust, Bolt, Fog, Lava, Mistake


class Water:
    def __add__(self, other):
        if isinstance(other, Soil):
            return Mud()
        elif isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Dust):
            return Fog()
        else:
            return Mistake()

    def __str__(self):
        return 'Water'


class Fire:
    def __add__(self, other):
        if isinstance(other, Air):
            return Bolt()
        elif isinstance(other, Soil):
            return Dust()
        else:
            return Mistake()

    def __str__(self):
        return 'Fire'


class Air:
    def __add__(self, other):
        if isinstance(other, Fire):
            return Bolt()
        elif isinstance(other, Soil):
            return Dust()
        else:
            return Mistake()

    def __str__(self):
        return 'Air'


class Soil:
    def __add__(self, other):
        if isinstance(other, Water):
            return Mud()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        else:
            return Mistake()

    def __str__(self):
        return 'Soil'
