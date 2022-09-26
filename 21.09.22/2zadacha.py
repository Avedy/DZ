grad=int(input())
s=[]
while grad!=0:
    if grad>2 and grad<=5:
        s.append(grad)
    grad = int(input())
print(sum([s.count(3),s.count(4),s.count(5)])/len([s])*100)
