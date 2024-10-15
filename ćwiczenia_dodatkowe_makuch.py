def liczby1():
    for x in range(3, 33, 1):
        print(x)

def liczby2():
    for x in range(0, 777, 1):
        if x%7 == 0:
            print(x)
        else:
            '''d'''
def lista1():
    ls = [2, 5, 8, 2, 12]
    for x in ls:
        if x > 3:
            print(x)
        else:
            '''c'''
def lista2():
    ls = ['ala', 'pies', 'slon', 'rzeka', 'stara', 'las', 'keke']
    ls3 = []
    for n in ls:
        ls2 = []
        ls2.append(len(n))
        #print(ls2)
        for m in range(0, len(n), 1):
            if n[m] == 'a':
                ls3.append(n)
            else:
                '''d'''
    print(set(ls3))

def lista3():
    ls = [2, 5, 8, 2, 12]
    y = - len(ls)
    for m in range(-1, y, -1):
        print(ls[m])

def dziesietne():
    x = input('liczba w systemie binarnym: ')
    y = len(x)
    z = 0
    ls = []
    ls2 = []
    while z < y:
        ls.append(int(x[z]))
        z += 1
    for n in ls:
        m = ls[n]*2**y
        y -= 1
        ls2.append(m)
    d = sum(ls2)
    print('W systemie dziesiętnym to będzie %d' %d)

def rozdziel1():
    x = input('niech poniesie Cię fantazja: ')
    y = x.split(',')
    print(y)

def zamien1():
    x = input('niech poniesie Cię fantazja: ')
    y = x.replace(' ', '_')
    print(y)

def znajdz():
    x = input('niech poniesie Cię fantazja: ')
    y = len(x)
    z = 0
    litery = []
    while z < y:
        litery.append(x[z])
        z += 1
    a = litery.index('a')
    b = a+1
    print('a to %d litera' %b)

def znajdz2():
    x = input('niech poniesie Cię fantazja: ')
    y = x.find('a') + 1 
    print('litera a jest na pozycju numer %d'%y)

'''funkcje .index i .find się różnią - lista.index('szukana fraza na liście')
lub string.find('szukana fraza w stringu') - do indexu potrzebujemy mieć listę, do .find wystarszy ciągły string'''

def liczeniea():
    x = input('niech poniesie Cię fantazja: ')
    print(x.count('a'))
    
def liczenie2():
    x = input('niech poniesie Cię fantazja: ')
    y = input('jak ą literę mamy liczyć?: ')
    print(x.count(y))

def reverseletters():
    x = input('niech poniesie Cię fantazja: ')
    a = x[0] 
    b = x[-1]
    #print(a,b)
    m = x[1:(-1)]
    #print(m)
    z = (b + m +a)
    print(z)

def usuwa():
    a = input('podaj słowo:')
    n = int(input('podaj cyfrę: '))
    if n > len(a):
        while n > len(a):
            n = int(input('podaj inną cyfrę: '))
    else:
        '''d'''
    b = a[:n-1] + a[n:]
    print(b)

def lista_alfabetyczna():
    ls = ['ala', 'katharsis', 'małolata', 'agnieszka', 'kot']
    print(sorted(ls))
    '''sorted - sortuje alfabetycznie listę :)'''

def element():
    ls = ['ala', 'katharsis', 'małolata', 'agnieszka', 'kot']
    print(ls[2])

def usuwapop():
    ls = ['ala', 'katharsis', 'małolata', 'agnieszka', 'kot']
    y = ls.pop(2)
    print(ls)
''' lista.pop(n) - usuwa n-ty element z listy (na liscie zostają wszystkei poza n-tym)'''

def usuwax():
    ls = ['ala', 'katharsis', 'małolata', 'agnieszka', 'kot', 'xenophobia', 'x']
    ls2 = []
    for x in ls:
        y = x.split()
        #y.replace('x', '')
        print(y)
        for y in x:
            if y[0] == 'x':
                y = y.replace(y[0], '')
                print(y)

'''ŹLE DZIAŁA< POPRAW'''

def usuwax3():
    x = ['ala', 'katharsis', 'małolata', 'agnieszka', 'kot', 'xenophobia', 'x']
    y = ['ala', 'katharsis', 'małolata', 'agnieszka', 'kot', 'xenophobia', 'x']

    '''stworzyłam kopię pierwszej listy (x nie równa się y, tylko chamska kopia), po to żeby z x usunąć 'x', a po y iterować'''
    dlugosci = []
    for n in y:
        z = len(n)
        dlugosci.append(z)
    print(dlugosci)
    
    for n in y:
        for m in dlugosci:
            for g in range(0, m):
                a = 0
                if str(n[g]) == 'x':
                    n.remove(n[a])
                    a += 1
                else:
                    a += 1
'''ŹLE DZIAŁA< POPRAW'''
    
  
