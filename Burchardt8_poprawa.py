#zad_DNA_RNA
class RNA:
    def __init__(self, ident, gatunek, sekwencja):
        self.idt = ident
        self.g = gatunek
        self.seq = sekwencja

    def complementary(self):
        seq = self.seq
        seq = seq.replace('A', 'u')
        seq = seq.replace('U', 'a')
        seq = seq.replace('G', 'c')
        seq = seq.replace('C', 'g')
        seq = seq.upper()
        return seq

    def length(self):
        length = len(self.seq)
        return(length)
        
    def __add__(self, other):
        new_id = self.idt + '_' + other.idt
        new_genre = self.g+ ', ' + other.g
        new_seq = self.seq + other.seq
        new_object = RNA(new_id, new_genre, new_seq)
        return new_object

    def __str__(self):
        #zmienia komunikat printa
        return('należę do klasy RNA ( ͡° ͜ʖ ͡°) ')
    
    def __repr__(self):
        #zmienia komunikat po wywolaniu obiektu bez metody
        return('jestem z klasy RNA. ID: %s, gatunek: %s, sekwencja: %s.' %(self.idt, self.g, self.seq))

def rna_to_dna(seq):
    seq = seq.replace('U', 'T')
    return seq

class DNA(RNA):
    def __init__(self, ident, gatunek, sekwencja):
        RNA.__init__(self, ident, gatunek, sekwencja)
        sekwencja = rna_to_dna(self.seq)
        self.seq = sekwencja
        
    def complementary(self):
        seq = self.seq
        seq = seq.replace('A', 't')
        seq = seq.replace('T', 'a')
        seq = seq.replace('G', 'c')
        seq = seq.replace('C', 'g')
        seq = seq.upper()
        return seq

#zad_choinka
import sys
import datetime
argmuents = sys.argv[1:]
a1 = argmuents[1]
a0 = argmuents[0]
def modul_choinki(a0, a1):
    import datetime

    '''x = 0
    print(2*' ' + '#' + 2* ' ')
    print(' ' + 3 * '+' + ' ')
    print(5* '+')
    while x + 1 < a:
        print(2*' ' + '+' + 2* ' ')
        print(' ' + 3 * '+' + ' ')
        print(5* '+')
        x += 1
    print(2*' ' + '|' + 2* ' ')
    print(2*' ' + '|' + 2* ' ')
    date = datetime.datetime.now()
    year = date.strftime("%Y")
    print('Merry Christmas', year)'''
    #nazwa = 'nowa_nazwa'
    f = open(nazwa, 'w')
    x = 0
    f.write('  $  \n')
    f.write(' +++ \n')
    f.write('+++++\n')
    while x + 1 < a:
        f.write('  +  \n')
        f.write(' +++ \n')
        f.write('+++++\n')
        x += 1
    f.write('  |  \n')
    f.write('  |  \n')
    date = datetime.datetime.now()
    year = date.strftime("%Y")
    f.write('Merry Christmas %s' %year)    
    f.close()


