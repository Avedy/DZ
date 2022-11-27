"""
В классе Hero из предыдущего занятия добавьте приватное свойство rank.
Создайте геттер, сеттер и делиттер чтобы можно было получить звание героя, установить звание "Победитель арены"
в случае победы героя в битве и удалить ранк в случае поражения.
"""


class Hero():
    def __init__(self, name, health, armor, rank):

        self.name = name
        self.health = health
        self.armor = armor
        self.__rank = rank


    def getrank(self):
        return self.__rank


    def setrank(self):
        self.__rank = 'Победитель арены'


    def delrank(self):
        del self.__rank


    def print_info(self):
        print(self.name)
        print('Уровень здоровья: ', self.health)
        print('Класс брони:', self.armor)




print('---Создайте своего персонажа---')
name = input('Имя:')
health = int(input('Хп: '))
armor = int(input('Броня: '))
knight1 = Hero(name, health, armor, "НонРанг")
knight2 = Hero('', 10, 5, 0)
print(name, health, armor)