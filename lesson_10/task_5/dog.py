from task_5 import Animals, NewClass


class Cat(Animals, NewClass):
    def __init__(self, name, age, speed):
        super().__init__(name, age)
        self._speed = speed

    def get_special_info(self):
        return f'{self._speed = }'
