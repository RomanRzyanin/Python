# a = 2
# b = 6
# while a <= b:
#     print(a)
#     a += 1

# a = 5
# print(id(a))
#
# a = 'Hello world'
# print(id(a))
#
# a = 3.14 / 3
# print(id(a))
#
# print(a, 456, 'text', sep=' (=^.^=) ', end='#')
# print('Any_text')
#
# res = input('Print your text: ')
# print('You print:', res)

# age = int(input('How old are you: '))
# print (f'You are {age} years old')
# ADULT = 18
# how_old = ADULT - age
#
# print(how_old, 'лет осталось до совершеннолетия')

# pwd = 'text'
# res = input('Input password: ')
# if res == pwd:
#     print('Good')
# else:
#     print('Bad')
# print('Bay-bay')

# res = int(input('2 + 2 = '))
# print('Good' if 2 + 2 == res else 'You are stupid')

# print('Neo' < 'Markus')

# count = 10
# for i in range(count):
#     for j in range(count):
#         for k in range(count):
#             print(i, j, k)


data = 0
while data < 100:
    data += 3
    if data % 40 == 0:
        break
# else:
#     data += 5
print(data)