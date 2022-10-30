"""
Напишите список функций по требованию. Пользователь вводит имя. Если имя заканчивается на А,Я,Г,М, то программа добавляет
к имени "Гений". Если на О,Ь,Л,Н. То добавляется "Сверхразум". Если ни на одну из этих букв то добавляется "Просто" перед именем.
"""


def nk(imya):
    word1 = "АЯГМ"
    word2 = "ОЬЛН"
    case_name = [(lambda x: print(x, "Гений")), (lambda x: print(x, "Сверхразум")), (lambda x: print("Просто", x))]
    if imya[-1].lower() in word1.lower():
        case_name[0](imya)
    elif imya[-1].lower() in word2.lower():
        case_name[1](imya)
    else:
        case_name[2](imya)


nk(input("Введите имя: "))