"""
Напишите генератор выводящий все числа делящиеся на 11 в диапазоне от 0 до 100
"""
def delenie():
    a=[i for i in range(0,100)]
    for i in range(100):
        if i%11==0:
            yield i
deln=delenie()
for i in deln:
    print(i)

