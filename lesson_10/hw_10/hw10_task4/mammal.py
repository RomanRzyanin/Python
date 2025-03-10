from animal import Animal


class Mammal(Animal):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight

    def category(self):
        if self.weight < 1:
            return 'малявка'
        elif self.weight > 200:
            return 'гигант'
        else:
            'обычный'

    def __str__(self):
        return f'Животное класса {super().__str__()}, относится к типу {self.category()}'
