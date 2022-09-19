a=input('Чтобы начать игру введите слово - game:\n')
while a != 'off':
    if a != 'game':
        print('Неверная фраза! SyntaxError Invalid Syntax!!!')
    else:
        print('Вы запустили игру "Угадай число"!')
        for i in range(3):
            b=input('Напишите число от 1 до 10:\n')
            if b == '5':
                print('Вы выиграли билет на концерт Шуфутинского!')
                break
            elif b == 'off':
                break
            else:
                print('Неверно')
    a = input('Чтобы начать игру введите слово - game:\n')