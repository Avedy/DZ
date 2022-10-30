"""
С помощью обработки ошибок разделить все элементы этого списка на 3.
При возникновении ошибки вывести надпись "Невозможно разделить"
"""


s = [1,2,"gonep"]
def gonep():
    delitel= 3
    try:
        delenie = [x//delitel for x in s]
        print(delenie)
    except:
        print("Невозможно разделить")


if __name__ == "__main__":
    gonep()