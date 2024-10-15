def wykrzykniki():
    a = input('tekst irytującego młodszego brata: ')
    b = a.replace("!", "")
    #print(b)
    c = len(a) - len(b)
    #print(c)
    print(b+3*c*'!')

def login():
    a = input('Podaj imię i nazwisko: ')
    b = a.split(' ')
    c = b[0]
    d = b[1]
    #print(c[0])
    '''pierwsza litera imienia'''
   # print(d[0])
    '''pierwsza litera nazwiska'''
    print('Twój login to: '+str(c[0])+str(d[0])+str(len(c))+str(len(d)))

def login2():
    c = input('podaj imię: ')
    d = input('podaj nazwisko: ')
    print('Twój login to: '+str(c[0])+str(d[0])+str(len(c))+str(len(d)))


def angle2():
    a = float(input('Podaj wartość kąta w stopniach: '))
    from math import pi as pi
    b = round((a/360* 2* pi),3)
    import math
    from math import sin as sin, cos as cos
    c = round(sin(b), 3)
    d = round(cos(b), 3)
    from array import array
    opisy = (['kąty: ' , 'radiany: ', 'sinus: ', 'cosinus: '])
    dane = ([str(a), str(b), str(c), str(d)])
    for x in range(0,4):
        print(opisy[x]+dane[x])
