from task_5 import Animals


class Cat(Animals):
    def __init__(self, name, age, jump, sleep):
        super().__init__(name, age)
        self._jump = jump
        self._sleep = sleep

    def get_special_info(self):
        return f'{self._jump = }\n{self._sleep = }'

    def get_info(self):
        return f'Переопределенный метод: \n{self._name = } {self._age = }\n{self._jump = } {self._sleep = }'


if __name__ == '__main__':
    cat_1 = Cat('Barsik', 13, 2, 23)

    print(cat_1.get_info(), '\n', cat_1.get_special_info())
    print(cat_1._name)
