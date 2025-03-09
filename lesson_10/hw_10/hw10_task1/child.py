class Child:
    def __init__(self, name_child, age_child):
        self.name = name_child
        self.age = age_child
        self.calm = False
        self.hungry = True

    def get_status(self):
        calm_status = 'спокоен' if self.calm else 'не спокоен'
        hungry_status = 'сыт' if not self.hungry else 'голоден'
        print(f'Child  {self.name} is {calm_status} & {hungry_status}.')

    def __str__(self):
        return f'Child {self.name}, {self.age} years old'
