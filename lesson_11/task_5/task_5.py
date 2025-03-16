'''Задание №5
Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр
прямоугольника.
Складываем и вычитаем периметры, а не длинну и ширину.
При вычитании не допускайте отрицательных значений.'''


class Rectangle:
    def __init__(self, *args):
        self._length = args[0]
        self._width = self._length if len(args) == 1 else args[1]  # 'тернарный оператор'
        self._perimeter = round((self._length + self._width) * 2, 2)
        self._area = round(self._length * self._width, 2)

    def area(self):
        return (f'The area of a rectangle with a length - {self._length} and width - {self._width} '
                f' = {round(self._length * self._width, 2)}')

    def get_area(self):
        return self._area

    def perimeter(self):
        return (f'The perimetr of a rectangle with a length - {self._length} and width - {self._width}'
                f' = {round((self._length + self._width) * 2, 2)}')

    def get_perimeter(self):
        return self._perimeter

    def __add__(self, other):
        return Rectangle(self._perimeter + other._perimeter)

    def __sub__(self, other):
        if other._perimeter > self._perimeter:
            raise ValueError('Недопустимая операция')
        return Rectangle(self._perimeter - other._perimeter)


    def __eq__(self, other):
        return self._area == other._area

    def __lt__(self, other):
        return self._area < other._area

    def __le__(self, other):
        return self._area <= other._area

    # def __gt__(self, other):
    #     return self._area > other._area
    #
    # def __ge__(self, other):
    #     return self._area >= other._area
    #
    # def __ne__(self, other):
    #     return self._area != other._area


    def __str__(self):
        return f'периметр = {self._perimeter}.'
        #return f'прямоугольник со сторонами {self._width}, {self._length} , прощадь = {self._area}, периметр = {self._perimeter}.'

rec_1 = Rectangle(3, 11)
rec_2 = Rectangle(6, 2)
print(rec_1.get_perimeter())
print(rec_2.get_perimeter())
# print(rec_1 == rec_2)
# print(rec_1 != rec_2)
# print(rec_1 > rec_2)
# print(rec_1 < rec_2)
# print(rec_1 >= rec_2)
# print(rec_1 <= rec_2)
print(rec_1 + rec_2)
print(rec_1 - rec_2)