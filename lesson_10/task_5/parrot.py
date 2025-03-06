from task_5 import Animals


class Parrot(Animals):
    def __init__(self, name, age, words):
        super().__init__(name, age)
        self._words = words

    def get_special_info(self):
        return f'{self._words = }'

    def get_info(self):
        return f'Переопределенный метод: \n{self._name = } {self._age = }\n{self._words = }'


if __name__ == '__main__':
    parrot_1 = Parrot('Kesha', 3, 134)

    print(parrot_1.get_info(), '\n', parrot_1.get_special_info())
    print(parrot_1._name)
