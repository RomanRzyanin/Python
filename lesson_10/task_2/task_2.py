'''Задание №2
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.
'''


class Rectangle:
    def __init__(self, *args):
        self.__length = args[0]
        self.__width = self.__length if len(args) == 1 else args[1] # 'тернарный оператор'


    def area(self):
        return (f'The area of a rectangle with a length - {self.__length} and width - {self.__width} '
                f' = {round(self.__length * self.__width, 2)}')

    def perimeter(self):
        return (f'The perimetr of a rectangle with a length - {self.__length} and width - {self.__width}'
                f' = {round((self.__length + self.__width) * 2, 2)}')


r_1 = Rectangle(3, 5)
r_2 = Rectangle(456)
r_2._Rectangle__length = 12
r_3 = Rectangle(11, 34)
print(r_1.perimeter(), r_1.area(), sep='\n')
print(r_2.perimeter(), r_2.area(), sep='\n')
print(r_3.perimeter(), r_3.area(), sep='\n')

r_2._Rectangle__length = 12
print(r_2._Rectangle__length)