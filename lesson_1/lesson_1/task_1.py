# task_1
# 5 * x ** 2 - 10 * x - 400 = 0

#
from math import sqrt

a, b, c = 5, - 10, - 400
d = (b ** 2) - (4 * a * c)
if d < 0:
    print('Bad')
elif d == 0:
    x_1 = x_2 = (- b + sqrt(d)) / (2 * a)
else:
    x_1 = (- b + sqrt(d)) / (2 * a)
    x_2 = (- b - sqrt(d)) / (2 * a)
print(f'x_1 = {round(x_1, 2)}, x_2 = {round(x_2, 2)}')

# task_2
#