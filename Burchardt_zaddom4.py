
#zad_1
def tymins(seq):
    '''(lista) -> lista
    przyjmuje listę sekwencji i zwraca
    listę ilości tymin w każdej z przyjętych sekwencji
    >>>tymins(['ATT', 'TTT', 'GGCC'])
    [2, 3, 0]
    '''
    tym_count = lambda x : x.count('T')
    return(list(map(tym_count, seq)))


#zad_2
def codons(seq):
    '''(lista) -> lista
    przyjmuje listę sekwencji i zwraca listę tych sekwencji, które uległy delecji
    >>>codons(['ATT', 'TTT', 'GGCC', 'ACACCAC'])
    ['GGCC', 'ACACCAC']'''
    seq2 = [x for x in seq if len(x)%3 != 0]
    return(seq2)

#zad_3
def sequences(s):
    '''(string) -> lista
    przyjmuje ciąg tekstowy z sekwencjami, zapisuje sekwencje
    jako elementy listy oraz sortuje je ze względu na ilość reszt uracylowych w każdej
    w nich w kolejności malejącej
    >>>sequences("UGUUUUUUUU, GUAGUA, UUUU, UGAGG, UGAGGUAGUAGGUUGUAUGGUU")
    ['UGUUUUUUUU', 'UGAGGUAGUAGGUUGUAUGGUU', 'UUUU', 'GUAGUA', 'UGAGG']'''
    uracyl = lambda x : x.count('U')
    seq2 = sorted(s.split(', '), key = uracyl, reverse= True)
    return(seq2)
