"""
Напишите программу, которая запрашивает ввод двух значений.
Если хотя бы одно из них не является числом, то должна выполняться конкатенация, то есть соединение строк.
В остальных случаях введенные числа суммируются.
"""


def dig(num1, num2):
        try:
            return int(num1)+int(num2)
        except:
            return str(num1)+str(num2)


def gonep():
        print(dig(str(input()), str(input())))


gonep()