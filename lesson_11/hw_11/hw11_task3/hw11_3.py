'''Задача 3. Класс Rectangle - работа с прямоугольниками
Разработайте программу для работы с прямоугольниками. Необходимо создать класс
Rectangle, который будет представлять прямоугольник с заданными шириной и высотой.
'''


class Rectangle:
    def __init__(self, width, height=None):
        self._width = width
        self._height = height if height is not None else width

    def perimetr(self):
        return (self._width + self._height) * 2

    def area(self):
        return self._width * self._height

    def __add__(self, other):
        new_height = self._height + other._height
        new_width = self._width + other._width
        return Rectangle(new_width, new_height)

    def __sub__(self, other):
        if self._height < other._height or self._width < other._width:
            raise ValueError('Error. Wrong operation')
        return Rectangle(self._width - other._width, self._height - other._height)

    def __eq__(self, other):
        return self.area() == other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __str__(self):
        return f'Прямоугольник со сторонами {self._width} & {self._height}'

    def __repr__(self):
        return f'Rectangle({self._width}, {self._height})'


rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)
rect5 = Rectangle(8)
rect6 = rect5
rect3 = rect1 + rect2
rect4 = rect1 - rect2
print(repr(rect6))
print(f'{rect4 = }')
print(rect5)
print(f"Периметр rect1: {rect1.perimetr()}")
print(f"Площадь rect2: {rect2.area()}")
print(f"Периметр rect3: {rect3.perimetr()}")
# print(f"rect1 < rect2: {rect1 < rect2}")
# print(f"rect1 == rect2: {rect1 == rect2}")
# print(f"rect1 <= rect2: {rect1 <= rect2}")
# print(f"rect1 < rect2: {rect1 > rect2}")
# print(f"rect1 == rect2: {rect1 != rect2}")
# print(f"rect1 <= rect2: {rect1 >= rect2}")
