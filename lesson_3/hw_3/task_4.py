'''Задача 4. Генерация паролей
Напишите программу, которая генерирует случайный пароль заданной длины,
состоящий из букв, цифр и специальных символов.
'''

import random as r
import string as s

length = int(input("Введите длину пароля: "))

char = s.ascii_letters + s.digits + s.punctuation

passw = ''.join(r.choice(char) for i in range(length))

print(passw)
print(char)