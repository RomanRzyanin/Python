'''Задача 5. Абстрактный класс
Вы работаете в компании, занимающейся разработкой программного обеспечения
для архитектурных проектов. Вам необходимо разработать программу для расчёта
площади различных геометрических фигур, таких как круги, прямоугольники и
треугольники.
Задача
Создайте:
● класс Shape, который будет базовым классом для всех фигур и будет
хранить пустой метод area, который наследники должны переопределить;
● класс Circle;
● класс Rectangle;
● класс Triangle.
Классы Circle, Rectangle и Triangle наследуют от класса Shape и реализуют метод
для вычисления площади фигуры.'''

from math import pi
from abc import ABC, abstractmethod


class Area(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Area):
    """
    Класс для представления круга, наследует от Shape.
    """

    def __init__(self, radius):
        self._radius = radius

    def area(self):
        return round(pi * self._radius ** 2, 2)


class Rectangle(Area):
    """
    Класс для представления прямоугольника, наследует от Shape.
    """

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height


class Triangle(Area):
    """
    Класс для представления треугольника, наследует от Shape.
    """

    def __init__(self, base, height):
        self._base = base
        self._height = height

    def area(self):
        return 0.5 * self._base * self._height


# Создание экземпляров классов
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)
# Вычисление площади фигур
circle_area = circle.area()
rectangle_area = rectangle.area()
triangle_area = triangle.area()
# Вывод результатов
print("Площадь круга:", circle_area)
print("Площадь прямоугольника:", rectangle_area)
print("Площадь треугольника:", triangle_area)
# Попытка создания экземпляра абстрактного класса Shape (должно вызвать ошибку)
try:
    area = Area()  # Ожидается ошибка
except TypeError as e:
    print(f"Ошибка: {e}")
