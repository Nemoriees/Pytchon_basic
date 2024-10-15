def lista():
    L = [x for x in range(10)]
    print(L)
    podzielne = list(map(lambda x:x%5 == 0, L))
    print(podzielne)
    podzielne2 = list(filter(lambda x: x%5 == 0, L))
    print(podzielne2)
    
def lambda_potegi():
    a = lambda x : x**x
    print(a(4))

def lambda_3_7(x):
    
    funckja1 = lambda x: x%3 == 0 
    print('Liczba podzielna przez 3:', funckja1(x))
    b = lambda x: x%7 == 0 
    print('Liczba podzielna przez 7:', b(x))    

def sortowanie():
    numerki = [3,8,1,0,34,2,6]
    numerki.sort()
    print(numerki)

def takeSecond(elem):
    return(elem[1])
    
def a_keys(wyniki):
    wyniki = [['Ania', 37],['Ala', 0],['Basia', 90],['Bartek', 17],['Lucas',38]]
    wyniki.sort(key = takeSecond)
    print(wyniki)

#zad.1
def lambda_keys(results):
    results = [['Ania', 37],['Ala', 0],['Lucas',38],['Basia', 90],['Bartek', 17]]
    takeSec = lambda x : x[-1]
    takeFirst = lambda x : x[0]
    results.sort(key = takeSec)
    sec_last = lambda x : x[-2]
    return(takeFirst(sec_last(results)))




def lista_skladana():
    seq = ["ATTGC", "AGGC", "TTTGC"]
    tymins = []

    for x in seq:
        y = x.count('T')
        tymins.append(y)
    print(tymins)
        
        
def lista_skladana_2():
    seq = ["ATTGC", "AGGC", "TTTGC"]
    tym_count = lambda x : x.count('T')
    tymins = map(tym_count, seq)
    print(list(tymins))
    
#zad1.1
def lista_skladana_3(seq):
    '''przyjmuje listę sekwencji i zwraca
    listę ilości tymin w każdej sekwencji'''
    tym_count = lambda x : x.count('T')
    return(list(map(tym_count, seq)))
    

def filter():
    seq = ["ATGCC", "TATC", "GGATGGGG"] 
    for x in seq:
        if len(x) < 5:
            seq.remove(x)
        else:
            None
    print(seq)

def filter_2():
    seq = ["ATTGC", "AGGC", "TTTGC"]
    seq2 = [x for x in seq if len(x)>4]
    return(seq2)


def filterTG():
    seq = ["ATTGC", "AGGC", "TTTGC"]
    seq2 = [x for x in seq if 'TG' in x]
    return(seq2)

#zad.dom2
def codons(seq):
    '''takes list of genetic codes and returns fragments with deletion'''
    #seq = ["ATTGC", "AGGC", "TTTGC"]
    seq2 = [x for x in seq if len(x)%3 != 0]
    return(seq2)


def lista_skladana():
    #list(map(lambda x:x**x, [1,2,3,4,5,6]))
    numbers = [x for x in range(1,7)]
    a = lambda x : x**x
    b = list(map(a, numbers))
    return(b)

def lista_skladana_2():

    b = list(map(lambda x:x**x, [x for x in range(1,7)]))
    return(b)

def rna():
    s = "UGAGGUAGUAGGUUUUUUUUUU, UGAGGUAGUAGGUUGAUUUUUU, UGAGGUAGUAGGUUGUUUUUUU, UGAGGUAGUAGGUUGUGAUUUU, UGAGGUAGUAGGUUGUAUGGUU"
    seq = s.split(', ')
    #print(seq)
    seq2 = sorted(seq, key = uracyl)
    print(seq2)


def uracyl(miniseq):
    return(miniseq.count('U'))


def rna2():
    s = 'UUA, U, GTGTGUUUUUU, UU, UUU'
    seq = s.split(', ')
    #print(seq)
    seq2 = sorted(seq, key = uracyl, reverse= True)
    print(seq2)

#ćwiczenie3
def rna_3(s):
    '''takes string, split it into sequences
    and sort them by the number of 'U' in descending order '''
    uracyl = lambda x : x.count('U')
    seq2 = sorted(s.split(', '), key = uracyl, reverse= True)
    return(seq2)



def pracownicy2():
    import pandas as pd
    f = open('pracownicy.txt', 'r')
    data = f.read()
    print(data)
    data2 = data.split('\n')
    print(data2)
    f.close()




def pracownicy():
    #zmodyfikowałam plik pracownicy.txt - plik miał źle wstwioną spację,
    #która zaburzała podział pliku na listę stringów
    f = open('pracownicy.txt', 'r')
    data = f.read()
    f.close()
    print(data)
    data = str(data)
    data = data.replace(';', ' ')
    data = data.split()
    for x in range(4):
        data.remove(data[0])
    salary = []
    for x in range(len(data)):
        if (x+1)%4 ==0:
            salary.append(int(data[x]))
        else:
            None
    salaries = sum(salary)
    print('suma wynagrodzeń pracowników to %d' %salaries)

def salary(ls):
    '''takes list from pracownicy.txt and returns list of salaries'''
    salary = []
    for x in range(len(ls)):
        if (x+1)%4 ==0:
            salary.append(int(data[x]))
        else:
            None
    return(salary)

def names(ls):
    '''takes list from pracownicy.txt and returns list of employes names'''
    names = []
    for x in range(len(ls)):
        if (x-1)%4 ==0:
            names.append(ls[x])
        else:
            None
    return(names)

def change_salary():
    #wywalić to f.open i f.close potem
    #f = open('pracownicy.txt', 'r+')
    id_employee = int(input('podaj ID pracownika: '))
    import fileinput
    for line in fileinput.input('pracownicy2.txt', inplace = 1):
        print(line)
        if line.startswith(str(id_employee)):
            print('TUTAJ')


    #f.close

            
def pracownicy_3():
#źle działa
    
    #zmodyfikowałam plik pracownicy.txt - plik miał źle wstwioną spację,
    #która zaburzała podział pliku na listę stringów
    f = open('pracownicy.txt', 'r+')
    data = f.read()
    
    print('lista płac:')
    print(data)
    data = str(data)
    data = data.replace(';', ' ')
    data = data.split()
    for x in range(4):
        data.remove(data[0])

    loop_on = 1
    while loop_on == 1:

        print('1-wyświetl listę pracowników, 2-zmień uposażenie pracownika, \n3 - zamknij program i zapisz, 4- wyłącz program')
        command = int(input('co chcesz zrobić?'))
        if command == 1:
            print('Imiona pracowników:', names(data))
        elif command == 2:
            id_employee = int(input('podaj ID pracownika: '))
            new_salary = int(input('podaj nową stawkę pracownika: '))
            data = data.insert(id_employee*4 + 3 ,new_salary)
            data2 = data.remove(data[id_employee+4])
            #pensa = id*4 +3
        elif command == 3:
            print('33')
        elif command == 4:
            loop_on = 0
        else:
            print('nie mogę tego zrobić')
            loop_on = 0
    f.close()
    print(data)

