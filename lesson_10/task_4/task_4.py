'''Задание №4
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления
суммы цифр id на семь'''
from task_3 import Person

class Human(Person):
    def __init__(self, first_name, last_name, age, uid):
        super().__init__(first_name, last_name, age)
        self.uid = uid
        self.access_level = uid % 7

    # def access_level(self):
    #     return f'Access level: {self.uid % 7}'
    #
    # def age(self):
    #     return f'Age: {self.__age}'

    # def birthday(self):
    #     self.__age += 1
    #     return f'Age: {self.__age}'
    #
    # def full_name(self):
    #     return f'Name: {self.first_name}, Last name: {self.last_name}'


p_1 = Human(1, 'Donald', 'Trump', 200)
p_2 = Human(23, 'Dad', 'Scozlozhop', 34)
p_3 = Human(12344534, 'Nikola', 'T', 121)

print(f'Uid: {p_3.uid}', p_3.access_level, p_3.age, p_3.full_name(), sep='\n')
print(f'Uid: {p_2.uid}', p_2.access_level,  p_2.full_name(), sep='\n')
print(f'Uid: {p_1.uid}', p_1.access_level,  p_1.full_name(), sep='\n')
