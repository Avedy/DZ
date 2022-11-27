"""
Создайте класс банковского аккаунта по аналогии с примером из презентации. Сделайте атрибут name защищенным, а
balance и pasport приватными.
Добавьте геттер-методы на pasport и balance. Сделайте смену номера паспорта по поролю. А изменение баланса
на определенную сумму(сумма не может падать меньше 0, так что сделайте проверку).
Создайте метод удаляющий паспортные данные с аккаунта(также по поролю).
"""

class BankAccount():
    def __init__(self, name, balance, passport):
        self._name = name
        self.__balance = balance
        self.__passport = passport


    def getpassport(self):
        return self.__passport


    def getbalance(self):
        return self.__balance


    def setpassport(self, number, password):
        if password == '12345':
            self.__passport = number
            print('Номер изменён')
        else:
            print('Неверный пароль')


    def setbalance(self, summa):
        if self.__balance + summa >= 0:
            self.__balance += summa
        else:
            print('У вас не хватает денег...')


    def delpassport(self, password):
        if password == '12345':
            del self.__passport
            print('Номер удалён')
        else:
            print('Неверный пароль')


account = BankAccount('gonep', 53714, 965596)
print(account.getpassport())
print(account.getbalance())
account.setbalance(12300)
account.setpassport(4123, '12345')
account.delpassport('12345')