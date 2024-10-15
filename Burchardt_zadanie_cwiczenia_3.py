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
    '''tej funkcji można podyktować macierze A i B (np. żeby potem je przemnożyć)
działa dla liczb całkowitych(!)'''
    
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
