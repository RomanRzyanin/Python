'''Задание №1
� Вспомните какие модули вы уже проходили на курсе.
� Создайте файл, в котором вы импортируете встроенные в
модуль функции под псевдонимами. (3-7 строк импорта).'''

from random import randint as ri
from math import sqrt as s
import string as srt_i

print(round(s(2), 4))
print([ri(0, 17) for i in range(15)])
