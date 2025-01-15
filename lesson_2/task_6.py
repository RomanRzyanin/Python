'''task_6
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
'''


cash = 0
cnt_a = 0
cnt_o = 0
while True:
    if cash > 5_000_000:
        print(f'You are lokh - {cash * 0.1}')
        cash -= cash * 0.1
    action = input('Enter the command: Out cash - o, Add cash - a, Exit - q: ')
    if action == 'q':
        print('Exit')
        print(f'Your are balance: {cash}')
        break
    elif action == 'a':
        amount = int(input('Enter the sum add: '))
        if amount % 50 == 0:
            cash += amount
            cnt_a += 1
            if cnt_a % 3 == 0:
                cash *= 1.03
        else:
            print('Enter the incorrect sum')
    elif action == 'o':
        amount = int(input('Enter the sum out: '))
        tax = amount * 0.015
        if tax < 30:
            tax = 30
        elif tax > 600:
            tax = 600
        if amount + tax > cash:
            print('Not cash')
        else:
            if cash % 50 == 0:
                cash -= amount + tax
                cnt_o += 1
                if cnt_o % 3 == 0:
                    cash *= 1.03
            else:
                print('Enter the incorrect sum')
    print(f'You are balance: {cash}')

