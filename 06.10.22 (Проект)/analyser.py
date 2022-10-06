def main(req):
    if 'расп' in req.lower() or 'дни' in req.lower():
        zanyatie()
    if 'трен' in req.lower() or 'контакт' in req.lower():
        contact()
    if 'оплат' in req.lower() or 'цена' in req.lower() or 'деньги' in req.lower():
        babki()
    if 'адрес' in req.lower() or 'место' in req.lower() or 'локац' in req.lower():
        adress()
    if 'не понятно' in req.lower() or 'вопрос' in req.lower() or 'что делать?' in req.lower():
        voprosi()

def zanyatie():
        print('Расписание занятий:')
        print('Понедельник - 18:30')
        print('Вторник - 18:30')
        print('Пятница - 18:30')

def contact():
        print('Контактные данные тренера:')
        print('Номер телефона: +79188888888')
        print('Электронная почта: treneradler@gmail.com')
        print('YouTube канал: https://www.youtube.com/channel/UCJ_GdEUJCS3qpfKDj76nfFQ')

def babki():
        print('Сумма к оплате одного занятия:')
        print('983 рубля')

def adress():
        print('Адрес спортбазы:')
        print('Сочи, Адлерский р-н, Воскресенская 18, 3 Этаж')

def voprosi():
    print('Все остальные вопросы спрашивать по телефону у тренера')



