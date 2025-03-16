class User:

    def __init__(self, a, b):
        self.name = a
        self.age = b

    def correct(self, name):
        self.name = name

    def __str__(self):
        return f'User {self.name}, age {self.age}'

u1 = User('Roman', 42)
print(u1)
u1.correct('Ann')
print(u1)