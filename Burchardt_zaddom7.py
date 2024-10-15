#zad_time
import datetime
def your_age():
    '''funkcja pyta użytkwnika o jego datę urodzenia w formacie DD-MM-YYYY,
    a następnie podaje mu informację ile lat, miesięcy i dni ułynęło od jego urodzenia
    '''
    brth_date = input('Podaj datę stojego urodzenia w formacie DD-MM-YYYY: ')
    brth_date = string_to_date(brth_date)
    now_date = datetime.datetime.now()
    b_y = years_from_date(brth_date)
    b_m = months_from_date(brth_date)
    b_d = days_from_date(brth_date)
    n_y = years_from_date(now_date)
    n_m = months_from_date(now_date)
    n_d = days_from_date(now_date)

    years = n_y - b_y
    if n_m < b_y:
        years = years - 1
        n_m = n_m + 12
    else:
        None
    months = n_m - b_m
    #tu należałoby jeszcze dopasować wartość add_days dla każdego miesiąca
    add_days = 30
    if n_d < b_d:
        months = months - 1
        n_d = n_d + add_days
    else:
        None
    days = n_d - b_d
    if months >= 12:
        years = years + 1
        months = months - 12
    print('Od Twoich urodzin minęło: %d lat, %d miesięcy i %d dni.' %(years, months, days))

def years_from_date(date):
    '''(datetime) -> int
    funkcja oddaje rok z podanej daty'''
    return int(date.strftime("%Y"))

def months_from_date(date):
    '''(datetime) -> int
    funkcja oddaje miesiąc z podanej daty'''
    return int(date.strftime("%m"))

def days_from_date(date):
    '''(datetime) -> int
    funkcja oddaje dzień z podanej daty'''
    return int(no_zero(date.strftime("%d")))

def no_zero(string_number):
    '''(string) -> string
    przyjmuje stringa składającego się z cyfr. Jeżeli na jego początku znajduje się 0, usuwa je
    >>>no_zero(07)
    7
    '''
    if string_number[0] == '0':
        string_number = string_number[1:]
    return string_number

def string_to_date(data):
    '''(string)-> datetime
    przyjmuje datę w formacie DD-MM-YYYY i zwraca datę w formacie
    obsługiwanym przez moduł datetime
    >>>string_to_date('12-12-1999')
    datetime.datetime(1999, 12, 12, 0, 0)'''
    data = data.split('-')
    x = datetime.datetime(int(data[2]), int(data[1]), int(data[0]))
    return x

#zad_potega
class Power:
    def __init__(self, number, power):
        self.number = number
        self.power = power
        
    def power_of_math(self):
        param = 0
        if self.power > 0:
            wynik = self.number
            while pram < self.power:
                wynik = wynik * self.number
                param =+ 1
                return wynik
        elif self.power < 0:
            self.number = 1/self.number
            wynik = self.number
            while pram < -self.power:
                wynik = wynik * self.number
            return wynik
            param =+ 1
        else:
            wynik = 1
            return wynik
        
    def __str__(self):
        return('wynik to %d' %wynik)

    #próbowałam zmienić sposób wywoływania (__str__, ale też __repr__, ale nie działa
    #nie wiem dlaczego tak się dzieje i jak to można obejść

#zad_walec
    
import math
from math import pi as pi

def pitagoras(a, b):
    '''Liczy długośc przeciwprostokątnej na podstawie znanych wartości dwóch przyprostokątnych'''
    s_kwadratow = a**2 + b**2
    c = math.sqrt(s_kwadratow)
    return c

class Walec:
    def __init__(self, promien, wysokosc):
        self.r = promien
        self.h = wysokosc
        
    def podstawa(self):
        pole = pi* self.r**2
        return pole
    
    def pole_boczne(self):
        obwod = pi * 2 * self.r
        pole_boczne = self.h * obwod
        return pole_boczne

    def objetosc(self):
        objetosc = pi* self.r**2 * self.h
        return objetosc

    def pret(self):
        dl_preta = pitagoras(self.h, 2*self.r)
        return dl_preta
    
'''a = Walec(3, 9)
print(a.podstawa())
print(a.pole_boczne())
print(a.objetosc())
print(a.pret())'''

