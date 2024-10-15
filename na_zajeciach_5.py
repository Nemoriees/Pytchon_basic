def randoms():
    import random
    a = random.randint(0,11)
    print(a)

def randoms2():
    import random
    a = random.random()
    print(a)

def lista_random():
    numbers = [2,5,8,2,-6,9]
    import random
    random.shuffle(numbers)
    print(numbers)
    print(random.choice(numbers))

def divide_by_5():
    numbers = [x for x in range(-5, 6)]
    divided = [5/x for x in numbers]
    print(divided)
    try:
        divide_by_5()

    except ZeroDivisionError as error:
        print(error)

    else:
        print('da')

#chyba nie zrozumiałam jaka jest rola * przed nazwą funkcji
#bez gwiazdki program zadziala tak samo
        
def loginy(*imiona):
    ''' program przyjmuje nieokreslona liczbe argumentow w postaci
    stringa 'imie naziwsko' oddzielone spacja
    >>> loginy('Marek Kowalski', 'Jan Gut', 'Anna Karenina', 'Yang Zgang')
    ['MK13', 'JG6', 'AK12', 'YZ9']
    >>> loginy('xya qwe', 'ASD as')
    ['XQ6', 'AA5']
    '''

    lista_loginow = []
    for ele in imiona:
        lista_loginow.append(pierwsze_litery(ele))
        
    print(lista_loginow)
    return lista_loginow

def pierwsze_litery(imie_nazwisko):
    '''(string) -> string
    pzyjmuje string będący imieniem i nazwiskiem
    zwraca inicjały i ilość liter w iminieniu i nazwisku'''

    rozdziel = imie_nazwisko.split(' ')
    inicialy = rozdziel[0][0] + rozdziel[1][0] + str(len(rozdziel[0])+len(rozdziel[1])) 
    
    return(inicialy)

#zad.kwargs
def czyWypozyczone(**wypozyczenia):
    ''' Funkcja zwraca w postaci listy użytkowników (ID),
    którzy wypożyczyli 'Potop'.
    >>> czyWypozyczone(id1=['Potop', 'Pan Tadeusz'], id2=['Ferdydurke'])
    [id1]
    >>> czyWypozyczone(id1=['Potop', 'Pan Tadeusz'], id2=['Ferdydurke'], id3=['Zbrodnia i kara', 'Potop', 'Harry Potter'])
    [id1, id3]
    '''
    tytul = input('Jakiego tytułu szukasz? ')
    listaId = []
    for key, value in wypozyczenia.items():
        if tytul in value:
            listaId.append(key)

    return listaId

def powtorka_sekwencje(s2):
    s2 = "ATGCTCGAAGAAtcACAGGCAGAACTCAATGtggAGCCCCCTCTGAGTCagGAGACATTttCCGACTTGTGGTGA"
    s2 = s2.upper()
    #print(s2)
    s2 = s2.replace('T', 'U')
    print(s2)
    
    if s2[:3] == 'AUG':
        print('mamy kodon start')
    else:
        print('nie mamy kodonu start')

    if s2[-3:] in ['UAA', 'UGA', 'UAG']:
        print('mamy kodon sop')
    else:
        print('nie mamy kodonu stop')



    if 'CUC' in s2:
        print('jest cuc')
    else:
        print('ni ma cuc')

    a = int(len(s2)/3)
    pusto = []
    for x in range(a-1):
        if s2[3*x] == 'C':
            if s2[3*x +1] == 'U':
                if s2[3*x + 2] == 'C':
                    pusto.append(1)
                else:
                    None
            else:
                None
        else:
            None
    print('jest %d CUC w kodonach' %(len(pusto)))
            
    return(s2)

    

def wytnij_s2():
    s2 = powtorka_sekwencje("ATGCUCGAAGAAtcACAGGCAGAACTCAATGtggAGCCCCCTCTGAGTCagGAGACATTttCCGACTTGTGGTGA")
    s3 = s2[3: -3]
    print(s3)

def regularne_3():
    s1 = 'mama, mem, mom'
    s2 = 'ac, abc, abbc, abbbc'
    s3 = 'tab, teb, teab, teaab'
    import re
    print(re.findall('m[aeo]ma?', s1))
    print(re.findall('ab*c',s2))
    print(re.findall('ab{0,3}c',s2))
    print(re.findall('te?a{0,2}b', s3))


def regularne_4():
    import re
    s1 = 'sawanna konie'
    print(s1.startswith('saw'))
    if s1[:3] == 'saw':
        print(True)
    else:
        print(False)
    print(re.findall('^saw',s1))
    

def regularne_5():
    import re
    tekst = 'Marie Sklodowska Curie (1867–1934) was the first person ever to receive two Nobel Prizes: the first in 1903 in physics, shared with Pierre Curie (her husband) and Henri Becquerel for the discovery of the phenomenon of radioactivity, and the second in 1911 in chemistry for the discovery of the radioactive elements polonium and radium.'
    daty = re.findall('[0-9]{4}', tekst)

    print(daty)


#zad.dom 
def regularne_6(ciag_znakow):
    '''(string) -> string
    usuwa wszystkie małe litery z ciągu znaków
    >>>regularne_6("ATTTGgccTaC")
    "ATTTGTC" '''
    import re
    wyciete = re.sub('[a-z]','', ciag_znakow)
    return(wyciete)

#zad dom
def regularne_7(tekst):
    '''(string) -> lista stringów
    znajduje w tekście wszystkie adresy e-mail i robi z nich listę
    >>>regularne_7("ala ma kota: ala@interia.pl ola hahaha@wp.pl grzes nie ma pk81@gmail.com")
    ['ala@interia', 'hahaha@wp', 'pk81@gmail'] '''
    import re
    maile = re.findall('[a-z0-9]+@[a-z0-9]+', tekst)
    return(maile)

#zad dom
def regularne_8(imiona_nazwiska):
    '''(lista stringów) -> lista stringów
    przyjmuję listę imion i nazwisk, zwraca listę imion i nazwisk,
    które rozpoczynają się na taką samą literę
    >>>regularne_8(["Mirek Maro","Adam Nowak", "Kasia Klimczak", "Maria Rudzik"])
    ['Mirek Maro', 'Kasia Klimczak'] '''
    import re
    lista_ID = []
    for osoba in imiona_nazwiska:
        osobno = osoba.split(' ')
        lit_imie = re.search("^[A-Z]", osobno[0])
        lit_naz = re.search("^[A-Z]", osobno[1])
        if str(lit_imie) == str(lit_naz):
            lista_ID.append(osoba)
        else:
            None
    return lista_ID




    
