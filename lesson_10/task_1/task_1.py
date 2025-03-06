'''Задание №1
Создайте класс окружность.
Класс должен принимать радиус окружности при создании
экземпляра.
У класса должно быть два метода, возвращающие длину
окружности и её площадь.
'''
from math import pi


class Circle:
    def __init__(self, radius, name=None):
        self.radius = radius
        self.name = name

    def area(self):
        return f'The area of a circle with a radius of {self.radius} = {round(pi * self.radius ** 2, 2)}'

    def length(self):
        return f'The length of a circle with a radius of {self.radius} = {round(2 * pi * self.radius, 2)}'

    def __str__(self):
        return 'This is a bagel'


c_1 = Circle(7)
c_2 = Circle(20)

print(c_1.area(), c_1.length(), sep='\n')
print(c_2.area(), c_2.length(), sep='\n')
print(c_1)
