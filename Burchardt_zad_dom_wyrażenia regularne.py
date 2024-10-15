def czyWypozyczone(**wypozyczenia):
    ''' Funkcja zwraca w postaci listy użytkowników (ID),
    którzy wypożyczyli 'Potop'.
    >>> czyWypozyczone(id1=['Potop', 'Pan Tadeusz'], id2=['Ferdydurke'])
    [id1]

    '''
    tytul = input('Jakiego tytułu szukasz? ')
    listaId = []
    for key, value in wypozyczenia.items():
        if tytul in value:
            listaId.append(key)
    return listaId

def regularne_6(ciag_znakow):
    '''(string) -> string
    usuwa wszystkie małe litery z ciągu znaków
    >>>regularne_6("ATTTGgccTaC")
    "ATTTGTC" '''
    import re
    wyciete = re.sub('[a-z]','', ciag_znakow)
    return(wyciete)

def regularne_7(tekst):
    '''(string) -> lista stringów
    znajduje w tekście wszystkie adresy e-mail i robi z nich listę
    >>>regularne_7("ala ma kota: ala@interia.pl ola hahaha@wp.pl grzes nie ma pk81@gmail.com")
    ['ala@interia', 'hahaha@wp', 'pk81@gmail'] '''
    import re
    maile = re.findall('[a-z0-9]+@[a-z0-9]+', tekst)
    return(maile)

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
