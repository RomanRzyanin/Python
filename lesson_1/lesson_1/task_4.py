# task_4

while True:
    num = int(input('Insert number: '))
    if 1 > num > 999:
        print('number out of range')
        continue
    elif 1 <= num < 10:
        print(num ** 2)
        break
    elif 10 <= num < 100:
        print((num % 10) * (num // 10))
        break
    elif 100 <= num < 1000:
        print(num % 10 * 100 + num // 10 % 10 * 10 + num // 100)
        break
