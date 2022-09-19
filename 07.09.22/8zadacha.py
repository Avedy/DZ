chislo=int(input())
a=chislo%10
b=chislo//10
c=b%10
d=b//10
e=d%10
print(sum([a,c,e]))
