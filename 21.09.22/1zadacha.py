s=[]
name=input()
while name !='0':
    if name in s:
        print("Игра уже есть")
    else:
        s.append(name)
    name=input()
s.sort()
print(s)
