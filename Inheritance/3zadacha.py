"""
Создайте класс SpaceObject у которого будут свойство размер.
Создайте 2 класса Star и Planet которые будут наследовать SpaceObject. В классе Star добавьте свойство яркость
и метод светить в котором будет выводится на экран с какой яркостью светит звезда.
Классу Planet добавьте свойства население и прирост за год и метод который будет печатать население через переданное
ему количество лет.
"""


class SpaceObject():
    def __init__(self, size):
        self.size = size


class Star(SpaceObject):
    def __init__(self, bright, size):
        super().__init__(size)
        self.bright = bright


    def shining(self):
        print('Звезда светит с яркостью:', self.bright)


class Planet(SpaceObject):
    def __init__(self, population, growth, size):
        super().__init__(size)
        self.population = population
        self.growth = growth


    def print(self, year):
        print('Через ' + str(year) + ' лет население будет: ' + str(year * self.growth + self.population))


star = Star(338, 111)
star.shining()
planet = Planet(500000, 1259, 1561)
planet.print(5)