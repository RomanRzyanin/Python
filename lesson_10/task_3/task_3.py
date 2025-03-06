'''Задание №3
Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст'''


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.__age = age

    @property  # 'getter'
    def age(self):
        if self.__age is None:
            return 'age is not specified'
        else:
            return f'Age: {self.__age}'

    @age.setter  # 'setter'
    def age(self, value):
        if value > 80:
            raise ValueError('oldest')
        self.age = value

    @age.deleter
    def age(self):
        del self.__age

    def birthday(self):
        if self.__age is None:
            return 'age is not specified'
        else:
            self.__age += 1
            return f'Age: {self.__age}'

    def full_name(self):
        return f'Name: {self.first_name}, Last name: {self.last_name}'


p_1 = Person('Donald', 'Trump', 200)
p_2 = Person('Dad', 'Scozlozhop', 34)
p_3 = Person('Nikola', 'T')

print(p_3.age, p_3.birthday(), p_3.age, p_3.full_name(), sep='\n')
print(p_2.age, p_2.birthday(), p_2.age, p_2.full_name(), sep='\n')
print(p_1.age, p_1.birthday(), p_1.age, p_1.full_name(), sep='\n')
