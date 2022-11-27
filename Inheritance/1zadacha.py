"""
Добавьте на основании классов из презентации класс Magician который наследует Hero. Со своими методами hello и atack.
"""


class Hero():
    def __init__(self, name, health, armor):
        self.name = name
        self.health = health
        self.armor = armor


    def print_info(self):
        print('Уровень здоровья: ', self.health)
        print('Броня: ', self.armor)


class Magician(Hero):
    def hello(self):
        super().print_info()


    def attack(self):
        print('Волшебник бьёт палкой врага')
        print('Урон - 287')


magician = Magician('volsh',100, 300)
magician.hello()
magician.attack()