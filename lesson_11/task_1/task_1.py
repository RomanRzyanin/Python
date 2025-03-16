'''Задание №1
Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания
(time.time)
'''
import time


class MyStr(str):
    """class MyStr for task_1"""
    #t = time.strftime('%d.%m.%Y %H:%M', time.localtime(time.time()))

    def __new__(cls, text, name, t = time.strftime('%d.%m.%Y %H:%M', time.localtime(time.time()))):
        my_str = super().__new__(cls, text)
        print(my_str)
        my_str.name = name
        my_str.t = t
        return my_str

    # def __init__(self, *args):
    #     self.name = args[0]
    #     self.my_str = args[1]
    #     self.s_time = args[2]
    #
    # def __str__(self):
    #     return f'Автор: {self.name} создал строку: {self.my_str}.\n Время создания: {self.s_time}'


# name = 'Roman'
# text = 'Si vis pacem parabellum'
# t = time.time()
# my_text = MyStr(name, text, t)
# print(my_text)


s = MyStr('Si vis pacem parabellum', 'Roman')
print(s)
print(s.name)
print(s.t)
a = 'valenok'
print(a)
