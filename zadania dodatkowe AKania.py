def iloczyn():
    x = int(input('wpisz pierszą liczbę: '))
    y = int(input('wpisz drugą liczbę: '))
    z = x*y
    if z > 0:
        print('iloczyn większy od 0')
    else:
        print('iloczyn mniejszy lub równy 0')
        
def kwadratowa():
    import math
    print('równanie kwadratowe wyraża się wzorem ax^2+bx +c, poniżej podaj parametry a, b oraz c')
    a = float(input('a: '))
    
    while a == 0:
        a = float(input('a musi być różne od zera! Podaj nowe a: '))
        
    b = float(input('b: '))
    c = float(input('c: '))
    d = b**2 -4*a*c
    
    if d > 0:
        x_1 = (-b - math.sqrt(d))/(2*a)
        x_2 = (-b + math.sqrt(d))/(2*a)
        print('miejsca zerowe to %f i %f' %(x_1, x_2))
    elif d == 0:
        x = -b/(2*a)
        print('Miejsce zerowe to %f' %x)

    else:
        print('Brak meijsc zerowych')

    
def podzielne_3():
    x = 1
    
    while x in range(26):
        if x%3 ==0:
            print(x)
            x +=1
        else:
            x +=1
def lista1():
    ls = [1, 2, 3]
    a = ls[-1]
    b = ls[-2]
    c = ls[-3]
    d = len(ls)  
    #print(a, b, c, d)
    while d < 8:
        a = ls[-1]
        b = ls[-2]
        c = ls[-3]
        e = a*b*c
        ls.append(e)
        d = len(ls)
        #print(e)
    print(ls)
    
def wyswietl_dodatnie_z_listy():
    ls = [1, 2, (-2), 0, (-6), 7, (-11), 12, 12]
    for x in ls:
        if x > 0:
            print(x)
        else:
            '''f'''
def dodatnie_2():
    ls = [1, 2, (-2), 0, (-6), 7, (-11), 12, 12]
    y = []
    for x in ls:
        if x > 0:
            y.append(x)
        else:
            ''' c'''
    print(set(y))

    
def lista_skladana():
    ls = []
    ls2 = []
    for x in range(1, 7, 1):
        ls.append(x)
    #print(ls)
    for x in ls:
        y = x**3
        ls2.append(y)
    print(ls2)

    
def czy_dodatnia():
    a = float(input('tu wpisz liczbę rzeczywistą: '))
    if a > 0:
        print('liczba dodatnia')
    elif a < 0:
        print('liczba ujemna')
    else:
        print('liczba nie jest ani dodatnia, ani ujemna')
        
def liniowa():
    print('podaj parametry a i b dla równania liniowego ax + b = 0')
    a = float(input('tu wpisz liczbę rzeczywistą a: '))
    if a == 0:
        a = float(input('podaj liczbę a różną od 0: '))
    else:
        '''d'''
    b = float(input('tu wpisz liczbę rzeczywistą b: '))
    
    x = -b/a
    print('x = %f' %x)
    
def czy_pierwsza():
    a = int(input('podaj liczbę, a powiem czy jest pierwsza: '))
    x = 2
    z = 0
    while x < a:
        if a%x == 0:
            z += 1
            x += 1
        else: 
            x += 1
    if z == 0:
        print('Twoja liczba jest pierwsza')
    else:
        print('Twoja liczba nie jest pierwsza')
            
    
