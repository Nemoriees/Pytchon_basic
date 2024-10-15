def funt():
    '''funkcja przyjmuje wagę w kg, a zwraca w funtach przy okazji zaokrąglając obie wartości'''
    a = int(input('ile ważysz? '))
    x = float("{liczba1:.1f}".format(liczba1 = float(a)))
    b = 2205*x/1000
    z = "{liczba2:.1f}".format(liczba2 = x) 
    c = "{liczba:.1f}".format(liczba = b)
    print('Ważysz %s kg albo %s funtów' %(z,c))
    
def funt_2():
    ''' to samo co wyżej, tylko w dwóch linijkach'''
    
    x = float("{liczba1:.1f}".format(liczba1 = float(int(input('ile ważysz? ')))))
    print('Ważysz %s kg albo %s funtów' %(x,("{liczba:.1f}".format(liczba = 2205*x/1000))))

def ciag_liczba():
    ''' sprawdza, czy liczba jest dodatnia i czy jest całkowita'''
    a = float(input('podaj liczbę: '))
    if a > 0:
        if a == int(a):
            print('dodatnia, całkowita')
        else:
            print('dodatnia, niecałkowita')
    else:
        if a == int(a):
            print('całkowita, niedodatnia')
        else:
            print('niecałkowita, niedodatnia')
    
def ciag_liczba2():
    '''to samo co wyżej, ale musi być i dodatnia i całkowita,
    żeby program dał stosowny komunikat'''
    a = float(input('podaj liczbę: '))
    if a > 0:
        if a == int(a):
            print('dodatnia, całkowita')
        else:
            print('nie jest jednocześnie dodatnia i całkowita')
    else:
        if a == int(a):
            print('nie jest jednocześnie dodatnia i całkowita')
        else:
            print('nie jest jednocześnie dodatnia i całkowita')

def elementy_lista():
    '''wywołuje drugie elementy z listy list'''
    
    B = ([1,2],[3,4],[5,'f'],[7,8],['malpa', 'pies'])
    for x in B:
        print(x[1])

def elementy_lista_2():
    B = ([1,2],[3,4],[5,'f'],[7,8],['malpa', 'pies'])
    C = []
    D = []
    for x in B:
        print(x[0],':',x[1])
        

def elementy_lista_3():
    
    B = ([1,2],[3,4],[5,'f'],[7,8],['m', 'pi'])
    C = []
    D = []
    for x in B:
        z = 3 - len(str(x[1]))
        print(x[0],':', z*' ',x[1])


##def pamiec():
##    ''' zadanie robione w interpreterze, tu tylko skopiowałam funkcje'''
##a = [1,2,3,4,5,6]
##print(a)
##[1, 2, 3, 4, 5, 6]
##b = a
##print(b)
##[1, 2, 3, 4, 5, 6]
##b[1] = 7
##print(a)
##[1, 7, 3, 4, 5, 6]
##print(b)
##[1, 7, 3, 4, 5, 6]
##
###podmiana elementu na jednej liście powoduje taką samą podmianę na drugiej liście
##
##a = [1,2,3,4,5,6]
##b = a.copy()
##print(b)
##[1, 2, 3, 4, 5, 6]
##b[1] = 7
##print(a)
##[1, 2, 3, 4, 5, 6]

#jeśli użyjemy funkcji lista2 = lista1.copy() to po
#zamianie elementu listy 2 lista1 pozostanie niezmieniona
##
##L = {'id1' : [3,5], 'id2' : [9,18]}
##
##L.keys()
##dict_keys(['id1', 'id2'])
##L.values()
##dict_values([[3, 5], [9, 18]])
##L.get('id1')
##[3, 5]
##L.get('zlyklucz')
##---nic---
##L.values('id3' : [2,9])
##L['id3'] = [2,8]
##print(L)
##{'id1': [3, 5], 'id2': [9, 18], 'id3': [2, 8]}
##L.pop('id3')
##[2, 8]
##print(L)
##{'id1': [3, 5], 'id2': [9, 18], 'usunmnie': [5, 6, 7, 0], 'mnietezusun': [1]}
##del L('usunmnie')
##             del L(klucz) nie zadziałało - dlaczego ????
    
