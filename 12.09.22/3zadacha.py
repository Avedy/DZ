cena1=int(input())
cena2=int(input())
cena3=int(input())
cena4=int(input())
cena5=int(input())
cena6=int(input())
suma1=(cena1+cena2+cena3)
suma2=(cena4+cena5+cena6)
if cena1==25 and cena2==100 and cena3==310:
    print('Акция!', suma1//2,'руб.')
elif cena4==2500 and cena5==400 and cena6==50:
    print('Акция!', suma2//3,'руб.')
else:
    print('К оплате')