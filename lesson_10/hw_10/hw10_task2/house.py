class House:
    def __init__(self, food=50, money=0):
        self.food = food
        self.money = money

    def buy_food(self, quantity, price):
        '''Buy food'''
        if self.money >= price:
            self.food += quantity
            self.money -= price
            print(f'Купили {quantity} единиц еды за {price} денег.')
        else:
            print('You don\'t have a money!!!')

    def earn_money(self, salary):
        '''Work'''
        self.money += salary
        print(f'Заработали {salary} денег.')
