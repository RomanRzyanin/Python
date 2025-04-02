# class Number:
#     def __init__(self, num):
#         self.num = num
#     def __call__(self, *args, **kwargs):
#         pass
#
# n = Number(42)
# print(f'{callable(Number) = }')
# print(f'{callable(n) = }')

# class MyClass:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __repr__(self):
#         return f'MyClass(a={self.a}, b={self.b}'
#
#     def __call__(self, *args, **kwargs):
#         self.a.append(args)
#         self.b.update(kwargs)
#         return True
#
# x = MyClass([42], {73: True})
# y = x(3.14, 100, 500, start=1)
# x(y=y)
# print(x)


# Итераторы

# class Fibonacci:
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
#         self.first = 0
#         self.second = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.first < self.stop:
#             self.first, self.second = self.second, self.first + self.second
#             if self.start <= self.first < self.stop:
#                 return self.first
#         raise StopIteration
#
# fib = Fibonacci(0, 100000)
# for num in fib:
#     print(num)


# class Iter:
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         for i in range(self.start, self.stop):
#             return chr(i)
#         raise StopIteration
#
#
# chars = Iter(65, 91)
#
# for c in chars:
#     print(c)


import sqlite3

# connection = sqlite3.connect('sqlite.db')
# cursor = connection.cursor()
# cursor.execute('''create table if not exists users(name, age);''')
# cursor.execute('''insert into users values ('Gvido', 66);''')
# connection.commit()
# connection.close()

# class DB:
#     def __init__(self, name):
#         self.name = name
#         self.connection = None
#         self.cursor = None
#
#     def __enter__(self):
#         self.connection = sqlite3.connect(self.name)
#         self.cursor = self.connection.cursor()
#         return self.cursor
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.connection.commit()
#         self.connection.close()
#         self.cursor = self.connection = None
#
# db = DB('sqlite_1.db')
# with db as cur:
#     cur.execute('''create table if not exists users(name, age);''')
#     cur.execute('''insert into users values ('Gvido', 66);''')

#
# class MyClass:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def __enter__(self):
#         self.full_name = self.first_name + ' ' + self.last_name
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.full_name = self.full_name.upper()
#
# x = MyClass('Gvido van', 'Rossum')
# with x as y:
#     print(y.full_name)
#     print(x.full_name)
#
# print(y.full_name)
# print(x.full_name)




