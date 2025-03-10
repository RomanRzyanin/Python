from animal import Animal


class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def wing_length(self):
        return self.wingspan

    def __str__(self):
        return f'Животное класса {super().__str__()}, с размахом крыльев  {self.wing_length()}'
