from random import randint


class Human:
    def __init__(self, name, house, hunger=50):
        self.name = name
        self.hunger = hunger
        self.house = house

    def eat(self):
        '''Eat & food'''
        if self.house.food >= 10:
            self.hunger += 10
            self.house.food -= 10
            print(f'{self.name} поел. Сытость увеличилась до {self.hunger}, еда уменьшилась до {self.house.food}.')
        else:
            print(f'{self.name} хотел поесть, но в доме недостаточно еды!')

    def work(self):
        '''Метод, который уменьшает сытость человека и увеличивает
        количество денег в доме.'''

        self.hunger -= 10
        self.house.earn_money(50)
        print(f'{self.name} поработал. Сытость уменьшилась до {self.hunger}.')

    def play(self):
        '''Метод, который уменьшает сытость человека.'''

        self.hunger -= 5
        print(f'{self.name} поиграл. Сытость уменьшилась до {self.hunger}.')

    def shop_for_food(self):
        '''Метод, который покупает еду за деньги.'''

        self.house.buy_food(15, 50)

    def live_day(self):
        '''Метод, который моделирует один день жизни человека.'''

        cube = randint(1, 6)
        print(f'\nСегодняшний кубик: {cube}')
        if self.hunger < 20:
            self.eat()
        elif self.house.food < 10:
            self.shop_for_food()
        elif self.house.money < 50:
            self.work()
        elif cube == 1:
            self.work()
        elif cube == 2:
            self.eat()
        else:
            self.play()
        if self.hunger <= 0:
            print(f"{self.name} you're dead.")
            return False
        return True
