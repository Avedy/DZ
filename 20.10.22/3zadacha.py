"""
Напишите функцию которая принимает 2 числа и выводит все числа между ними которые делятся на 3.
Напишите декоратор который выводит фразу:
"Данная функция выводит все числа между Число А и Число Б"(сюда подставьте числа что принимает функция)
и оберните функцию чтобы данная фраза выводилась перед ее выполнением
"""
a=int(input())
b=int(input())


def number(func):
    for i in range(a+1,b):
        if i%3==0:
            print(i)
    def irg():
        func()
    return irg

@number
def slova():
    print("Данная функция выводит все числа между Число А и Число Б, делящиеся на 3", (a, b))


slova()