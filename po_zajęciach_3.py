def slownik_z_listy1():
    
    '''przekształca listę dwuelementowych list w słownik w taki sposób, że
pierwszy element staje się kluczem, a drugi wartością'''
    
    lista_list = [[1,2], [3, 4], [5,6], [7, 8]]
    klucze = []
    wartosci = []
    for x in lista_list:
        klucze.append(x[0])
        wartosci.append(x[1])
    slownik_z_list = {}
    x = 0
    for n in range(len(klucze)):
        
        slownik_z_list[str(klucze[x])] = wartosci[x]
        x += 1
        
    print(slownik_z_list)

def slownik_z_listy_2():
    lista_list = [[1,2], [3, 4], [5,6], [7, 8]]
    klucze = []
    wartosci = []
    for x in lista_list:
        klucze.append(x[0])
        wartosci.append(x[1])
    slownik_z_list = {k:v for(k, v) in zip(klucze, wartosci)}

    print(slownik_z_list)

def slownik_z_listy_3():
    
    '''słowniki 2 i 3 robią to samo co 1, tylko w inny sposób, prościej'''
    
    lista_list = [[1,2], [3, 4], [5,6], [7, 8]]
    slownik_z_list = {k:v for(k, v) in lista_list}

    print(slownik_z_list)
    
def slownik_z_listy_4():
    
    '''tu okazuje się, że niekoniecznie musimy mieć do czynienia
z dwoma listami czy dwoma wartościami na listach - może być ich więcej'''
    
    lista_list = [[1,2,3], [4, 5, 6], [7, 8, 9]]
    slownik_z_list = {k:[v,z] for(k, v, z) in lista_list}

    print(slownik_z_list)

def trzecie_potegi():

    '''zwraca trzecie potegi liczb z zadanego zakresu'''

    trzecie_potegi =[]
    for x in range(3, 12, 1):
        trzecie_potegi.append(x**3)
    print(trzecie_potegi)

def trzecie_potegi_2(a,b):

    '''tym razem mozemy sami wybrac zakres liczb,
z ktorych beda liczone trzecie potegi'''
    
    trzecie_potegi =[]
    for x in range(a, (b+1), 1):
        trzecie_potegi.append(x**3)
    print(trzecie_potegi)
    
def trzecie_potegi_3():
    a = int(input('tu podaj liczbę: '))
    b = int(input('tu też podaj liczbę: '))
    trzecie_potegi =[]
    for x in range(a, (b+1), 1):
        trzecie_potegi.append(x**3)
    print(trzecie_potegi)

def ente_potegi():
    
    '''to samo, tylko sami możemy wybrać która potęga nas interesuje'''
    
    a = int(input('tu podaj liczbę: '))
    b = int(input('tu też podaj liczbę: '))
    c = int(input('która potęga, przywoływaczu? '))
    trzecie_potegi =[]
    for x in range(a, (b+1), 1):
        trzecie_potegi.append(x**c)
    print(trzecie_potegi)
    

def mnozenie_macierzy_brudnopis():

    '''mnozy przez siebie dwie macierze a i b'''

    a = [[1,5],[6,7],[7,8]]
    b = [[(-1),9,3],[2,(-5),7]]
    c = []
    d = []
    e = []
    ilosc_wierszy_a = len(a)
    wa = ilosc_wierszy_a
    ilosc_kolumn_b = len(b[0])
    kb = ilosc_kolumn_b
    ilosc_mnozen = len(b) 
    
    print('rozmiar nowej macierzy C to %d x %d' %(wa, kb))
    
    for x in range(0, wa, 1):
        for y in range(0, kb,1):
    
            '''patrzymy na jeden wiersz a i jedną kolumnę b'''
            for z in range(0, ilosc_mnozen , 1):
                
                print(a[x][z], b[z][y])
                iloczyn = a[x][z]*b[z][y]
                print(iloczyn)
                d.append(iloczyn)
            suma = sum(d)
            print('suma to:', suma)
            e.append(suma)
    c.append(e[0:3])
    e.pop(1)
    e.pop(1)
    e.pop(1)
    c.append(e[0:3])
    e.pop(1)
    e.pop(1)
    e.pop(1)
    c.append(e[0:3])
    print('c', c)
    #print(c)

def mnozenie_macierzy_czytopis1():

    '''mnozy przez siebie dwie macierze a i b - można modyfikować,
ważne, że ilosć kolumn a == ilosć wierszy b'''

    a = [[1,5],[6,7],[7,8]]
    b = [[(-1),9,3],[2,(-5),7]]
    c = []
    '''c to macierz wyjsciowa'''
    d = []
    e = []
    
    wa = len(a)
    '''wa = ilość wierszy nowej macierzy (czyli ilość wierszy a)'''
    kb = len(b[0])
    '''kb = ilość kolum nowej macierzy c( ale też ilość kolumn starej macierzy b)'''
    ilosc_mnozen = len(b)
    '''ważne do ilości obliczeń'''
    print('rozmiar nowej macierzy C to %d x %d' %(wa, kb))
    
    for x in range(0, wa, 1):
        for y in range(0, kb,1):
    
            '''patrzymy na jeden wiersz a i jedną kolumnę b'''
            for z in range(0, ilosc_mnozen , 1):
                iloczyn = a[x][z]*b[z][y]
                d.append(iloczyn)
            suma = sum(d)
            e.append(suma)
    print(e)
    for s in range(ilosc_mnozen+1):
        fragment = e[0:(ilosc_mnozen+1)]
        print(fragment)
        for r in range(ilosc_mnozen+1):
            e.pop(0)
        c.append(fragment)
        
    
    print('c', c)

def przyjmowanie_macierzy_reczne():
    
    print('Podaj wymiary macierzy A i B, w formacie: liczba_wierszyXliczba_kolumn\nliczba kolumn A musi być równa liczbie kolumn B')
    wymiary_a = input('Macierz A: ')
    wymiary_b = input('Macierz B: ')
    wymiary_a = wymiary_a.split('X')
    wymiary_b = wymiary_b.split('X')
    wiersze_a = int(wymiary_a[0])
    kolumny_a = int(wymiary_a[1])
    wiersze_b = int(wymiary_b[0])
    kolumny_b = int(wymiary_b[1])
    print(wymiary_a)
    print(wymiary_b)
    macierz_a = []
    for y in range(0, wiersze_a):
        print('podyktuj wartości z %d wiersza A:' %(y+1))
        wiersz_a = []
        for x in range(0, kolumny_a):
            obiekt_a = int(input('Podaj kolejną wartość: '))
            wiersz_a.append(obiekt_a)
        print('Wiersz numer %d:' %(y+1), wiersz_a)
        macierz_a.append(wiersz_a)
        
    print('Cała macierz A: ', macierz_a)
    
    macierz_b = []
    for m in range(0, wiersze_b):
        print('podyktuj wartości z %d wiersza B:' %(m+1))
        wiersz_b = []
        for n in range(0, kolumny_b):
            obiekt_b = int(input('Podaj kolejną wartość: '))
            wiersz_b.append(obiekt_b)
        print('Wiersz numer %d:' %(n+1), wiersz_b)
        macierz_b.append(wiersz_b)
        
    print('Cała macierz B: ', macierz_b)
    
def sortowanie_babelkow():
    ls = [1,4,6,7,3,4,5,9,9,2,0]
    parametr_odjęcia = 0
    for ilosc_przejsc in range(len(ls)):
        parametr_odjęcia = 0
        parametr = 0
        parametr2 = len(ls) - 1 - parametr_odjecia
        for ilosc_zmian in range(parametr2):
            if ls[parametr]>ls[parametr+1]:
                ls.insert(ls[parametr + 1], parametr)
                parametr += 1
            else:
                parametr += 1
        parametr_odjecia -= 1
        
    print(ls)
    
'''nie działa'''

def sortowanie_babelkow2():
    ls = [1,9,7,5,4,8,0]
    ilosc_elementow = len(ls)
    print(ilosc_elementow)
    numer_petli = ilosc_elementow - 1
    print(numer_petli)
    for x in range(0, numer_petli, 1):
        if ls[x] > ls[x+1]:
            print('komenda na zamiane miejsc')
        else:
            print('pozostaw')


def sortowanie_babelkow3():
    '''sortowanie bąbelkowe - poniżej wersja,
która zwraca tylko uporządkowaną listę bez komunikatów'''
    ls = [1,9,7,5,4,8,0]
    ilosc_elementow = len(ls)
    print(ilosc_elementow)
    numer_petli = ilosc_elementow - 1
    print(numer_petli)
    ilosc_powtorzen = len(ls) - 1

    parametr = 0
    for y in range(0, ilosc_powtorzen, 1):
        
        for x in range(0, numer_petli, 1):
            if ls[x] > ls[x+1]:
                a = ls[x] 
                b = ls[x+1]
                ls[x] = b
                ls[x+1] = a
                print('zmieniono')
            else:
                print('pozostaw')
        numer_petli = numer_petli -1
        print('koniec %d cyklu' %(ilosc_elementow - numer_petli - 1))
    print(ls)

def sortowanie_babelkow4():
    ls = [1,9,7,5,4,8,0]
    ilosc_elementow = len(ls)
    numer_petli = ilosc_elementow - 1
    ilosc_powtorzen = len(ls) - 1
    parametr = 0
    for y in range(0, ilosc_powtorzen, 1):
        
        for x in range(0, numer_petli, 1):
            if ls[x] > ls[x+1]:
                a = ls[x] 
                b = ls[x+1]
                ls[x] = b
                ls[x+1] = a
            else:
                ''''''
        numer_petli = numer_petli -1
    print(ls)

def przyjmowanie_listy():
    ls1 = input('podaj listę:')
    print(ls1)
    ls = ls1.split(',')
    print(ls)
    ls[0] = int(ls[0])
    
    for x in range(0,len(ls),1):
        ls[x] = int(ls[x])
    print(ls)

def sortowanie_babelkow5():
    ls1 = input('podaj listę:')
    ls = ls1.split(',')
    for x in range(0,len(ls),1):
        ls[x] = int(ls[x])
        
    ilosc_elementow = len(ls)
    numer_petli = ilosc_elementow - 1
    ilosc_powtorzen = len(ls) - 1
    parametr = 0
    for y in range(0, ilosc_powtorzen, 1):
        
        for x in range(0, numer_petli, 1):
            if ls[x] > ls[x+1]:
                a = ls[x] 
                b = ls[x+1]
                ls[x] = b
                ls[x+1] = a
            else:
                ''''''
        numer_petli = numer_petli -1
    print('posortowana lista:',ls)

    
    
def sortowanie_wstawianie():
    ls = [1,9, -2, -80, 7,5,4,8,0]
    sort = []
    sort.append(ls[0])
    ls.remove(ls[0])
    for x in range(len(ls)):
        sort.insert(0, ls[0])
        #trzeba dać na początek!
        
        ls.remove(ls[0])
        sort = compare(sort)
    print(sort)       
    
def compare(ls):
    #ls = [8,1, 3.5, 7, 8, 9]
    for x in range(len(ls)-1):
        if ls[x] > ls[x+1]:
            a = ls[x]
            b = ls[x+1]
            ls[x]= b
            ls[x+1] = a
        else:
            break
    print(ls)
    return(ls)








        
