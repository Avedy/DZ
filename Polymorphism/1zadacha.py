"""
Создайте классы утка и человек. У обоих классов нету свойств, но есть методы крякать и носить одежду.
Утка крякает, а человек имитирует кряканье. Добавьте экземпляры этих классов в список и вызовите в цикле соответствующие методы.
"""


class Person:
    def utka(self):
        print('Крякать :(')


    def clothes(self):
        print('Я ношу Prada')


class Duck:
    def utka(self):
        print('Крякать :)')


    def clothes(self):
        print('Утка носит Louis Vuitton')


def cikl():
    list=[Person(), Duck()]
    for i in list:
        i.utka()
        i.clothes()


cikl()