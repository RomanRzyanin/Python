'''Задание №7
✔ Создайте функцию-генератор.
✔ Функция генерирует N простых чисел,
начиная с числа 2.
✔ Для проверки числа на простоту используйте
правило: «число является простым, если делится
нацело только на единицу и на себя».
'''



def gen_prime(n):
    cnt = 0
    num = 1
    is_prime = True
    while cnt <= n:
        num += 1
        for j in range(2, int(num ** 0.5 + 1)):
            if num % j == 0:
                is_prime = False
                break
            else:
                is_prime = True
        if is_prime:
            cnt += 1
            yield num

#print(gen_prime(10))

for el in gen_prime(10):
    print(el, end=' ')