"""
Напишите генератор выводящий все символы строки на печать, но только в том случае, если они являются буквами (остальные игнорируются).
"""
s='a','b','c'
generator=(i for i in s if i.isalpha())
for i in generator:
    print(i)