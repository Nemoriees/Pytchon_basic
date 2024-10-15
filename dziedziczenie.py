class prostokaty:

    abstrakcyjne_b = 99
    
    def __init__(self, podstawa, wysokosc):
        self.h = wysokosc
        self.a = podstawa

    def pole(self):
        return(self.a * self.h)

    def obwod(self):
        return(2*self.a + 2*self.h)

    def __add__(self, other):
        return self.a + other.a

    def __str__(self):
        #zmienia komunikat print(obiekt)
        return('to jest obiekt typu prostokaty')

    def __repr__(self):
        #zmienia komunikat po wywolaniu obiektu bez metody
        return('obiekt prostokaty '+ str(self.h)+ ' ' + str(self.a))

class rownolegloboki(prostokaty):
    def __init__(self, podstawa, wysokosc, bok):
        prostokaty.__init__(self, podstawa, wysokosc)
        self.b = bok

    def obwod(self):
        return(2*self.a + 2*self.b)

class trapezy(prostokaty):
    #inny sposob dziedziczenia
    def __init__(self,podstawa, wysokosc, bok1, bok2, podstawa2):
        super().__init__(podstawa,wysokosc)
        self.b1 = bok1
        self.b2 = bok2
        self.p2 = podstawa2





'''

class RNA:
    def __init__(ident, gatunek, sekwencja):

    def __add__

'''       
































