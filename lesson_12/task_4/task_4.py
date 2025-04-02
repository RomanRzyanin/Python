'''Задание №4
Доработайте класс прямоугольник из прошлых семинаров.
Добавьте возможность изменять длину и ширину
прямоугольника и встройте контроль недопустимых значений
(отрицательных).
Используйте декораторы свойств.
'''


class Rectangle:
    __slots__ = '_length', '_width'

    def __init__(self, length, width=None):
        self._length = length
        self._width = length if width is None else width

    @property
    def length_rectangle(self):
        return self._length

    @length_rectangle.setter
    def length_rectangle(self, length):
        if length <= 0:
            raise ValueError('Incorrect data')
        self._length = length

    @property
    def width_rectangle(self):
        return self._width

    @width_rectangle.setter
    def width_rectangle(self, width):
        if width <= 0:
            raise ValueError('Incorrect data')
        self._width = width

    def get_perimetr(self):
        return (self._length + self._width) * 2

    def get_area(self):
        return self._width * self._length
