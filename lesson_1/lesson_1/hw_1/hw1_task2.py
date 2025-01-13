'''task_2.
Треугольник
Треугольник существует только тогда, когда сумма любых двух его сторон
больше третьей. Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если
хотя бы в одном случае отрезок окажется больше суммы двух других, то
треугольника с такими сторонами не существует. Отдельно сообщить является
ли треугольник разносторонним, равнобедренным или равносторонним.'''


def triangle_check(a, b, c):
    if a + b < c or a + c < b or b + c < a:
        print('The triangle does not exists.')
    else:
        print('The triangle exist', end=' ')
        if a == b == c:
            print('and equilateral.')
        elif a == b or b == c or a == c:
            print('and isosceles.')


print(' Enter the sides of the triangle:')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

triangle_check(a, b, c)
