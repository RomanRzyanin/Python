from animal import Animal


class Fish(Animal):
    def __init__(self, name, max_depth):
        super().__init__(name)
        self.max_depth = max_depth

    def depth(self):
        if self.max_depth < 10:
            return 'мелководная'
        elif self.max_depth > 100:
            return 'глубоководная'
        else:
            'средневодная'

    def __str__(self):
        return f'Животное класса {super().__str__()}, относится к {self.depth()} рыба'
