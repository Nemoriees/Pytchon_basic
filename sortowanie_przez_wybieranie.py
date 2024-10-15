def sortowanie_przez_wybieranie(ls):
    import copy
    ls2 = copy.copy(ls)
    ls3 = []
    for x in range(len(ls)):
        ls2 = najmniejsza_na_poczatek(ls2)
        ls3.append(ls2[0])
        ls2.remove(ls2[0])
    print(ls3)

def sortowanie_przez_wybieranie_optymalizacja(ls):
    #nie działa
    import copy
    ls2 = copy.copy(ls)
    ls3 = []
    for x in range(len(ls)):
        ls2 = najmniejsza_na_poczatek(ls2)
        ls3.append(ls2[0])
        ls2.remove(ls2[0])
        ls2 = najwieksza_na_koniec(ls2)
        ls3.append(ls2[-1])
        ls2.remove(ls2[-1])
    print(ls3)
        


def najmniejsza_na_poczatek(ls):
    #ls = [3,6,1,9,16,2,3,2, -5]
    najmniejsza = ls[0]
    pozycja = 0
    for x in range(len(ls)):
        if ls[x] <najmniejsza:
            najmniejsza = ls[x]
            pozycja = x
        else:
            None
    a = ls[0]
    b = ls[pozycja]
    ls[0] = b
    ls[pozycja] = a
    return(ls)

def najwieksza_na_koniec(ls):
    #ls = [3,6,1,9,16,2,3,2,-5]
    najwieksza = ls[0]
    pozycja = 0
    for x in range(len(ls)):
        if ls[x] > najwieksza:
            pozycja = x
            najwieksza = ls[x]
        else:
            None
    a = ls[-1]
    b = ls[pozycja]
    ls[-1] = b
    ls[pozycja] = a
    return(ls)



def szukanie_najmniejszej(ls):
    #ls = [3,6,1,9,16,2,3,2, -5]
    najmniejsza = ls[0]
    pozycja = 0
    for x in range(len(ls)):
        if ls[x] <najmniejsza:
            najmniejsza = ls[x]
            pozycja = x
        else:
            None
    return(najmniejsza)
            
def szukanie_najwiekszej(ls):
    #ls = [3,6,1,9,16,2,3,2,-5]
    najwieksza = ls[0]
    pozycja = 0
    for x in range(len(ls)):
        if ls[x] > najwieksza:
            pozycja = x
            najwieksza = ls[x]
        else:
            None
    return(najwieksza)
