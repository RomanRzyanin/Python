class ValDescriptor:
    # def __init__(self, attr):
    #     self.attr = attr

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    # def __get__(self, instance, owner):
    #     return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.valid(value)
        setattr(instance, self.param_name, value)

    def valid(self, value):
        if value <= 0:
            raise ValueError('Incorrect data')


class Rectangle:
    __slots__ = '_length', '_width'
    length = ValDescriptor()
    width = ValDescriptor()

    def __init__(self, length, width=None):
        self._length = length
        self._width = length if width is None else width

    # @property
    # def length_rectangle(self):
    #     return self._length
    #
    # @length_rectangle.setter
    # def length_rectangle(self, length):
    #     if length <= 0:
    #         raise ValueError('Incorrect data')
    #     self._length = length
    #
    # @property
    # def width_rectangle(self):
    #     return self._width
    #
    # @width_rectangle.setter
    # def width_rectangle(self, width):
    #     if width <= 0:
    #         raise ValueError('Incorrect data')
    #     self._width = width

    def get_perimetr(self):
        return (self._length + self._width) * 2

    def get_area(self):
        return self._width * self._length
