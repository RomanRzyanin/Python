class Parents:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self.children = []

    def info(self):
        return f'My name: {self._name}, I\'m {self._age} years old'

    def add_child(self, child):
        if self._age - child.age >= 16:
            self.children.append(child)
            print(f'Ребёнок {child.name} добавлен к {self._name}.')
        else:
            print(f'Ребёнок {child.name} не добавлен к {self._name}, '
                  f'так как разница в возрасте слишком мала.')

    def feed(self, child):
        if child in self.children:
            child.hungry = False
            print(f'{self._name} покормил(а) {child.name}.')
        else:
            print(f"{child.name} не является ребёнком {self._name}.")

    def calm(self, child):

        if child in self.children:
            child.calm = True
            print(f'{self._name} успокоил(а) {child.name}.')
        else:
            print(f'{child.name} не является ребёнком {self._name}.')

    def list_children(self):

        if self.children:
            print(f'{self._name} has the following children:')
            for child in self.children:
                print(f' - {child}')
        else:
            print(f'У {self._name} нет детей.')