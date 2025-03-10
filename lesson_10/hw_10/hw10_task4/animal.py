class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError('Данный метод реализован в подклассе')

    def __str__(self):
        return f"{self.__class__.__name__} названный {self.name}"