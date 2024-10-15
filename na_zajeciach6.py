def glob_znajdz():
    import glob
    print(glob.glob('*.txt'))
    print(glob.glob(______,'*.docx'))
  
def zad_12():
    import re
    sek =  "ATTTGGCGAGAGACATCATCATCAT"
    sek2 = re.sub('T','U' ,sek)
    print(sek2)

def zad11():
    sek =  "ATTTGGCGAGAGACATCATCATCAT"
    import re
    #więcej niż 3 = {3, }
    x = re.findall(r'(GA)\1{2,}',sek)
    print(x)
    y = re.findall(r'(GA)(CAT) \1{1,} \2{1,}', sek)
    
    print(y)

def zad1():
    sek =  "ATTTGGCGAGAGACATCATCATCAT"
    import re
    kod = re.findall(r'(\w*\S)\1{2,}', sek)
    #kod2 = re.findall(r'(\w{3}\S)\1{2,}', sek)
    print(kod)

def zad1a():
    #niedziala
    import re
    sek =  "ATTTGGCGAGAGACATCATCATCAT"
    x = re.findall(r'(?<dwa>\w*\S)(?<trzy>\w*\S) \1{2,} \2{3,}', sek)
    print(x)

def wstaw_spacje():
    import re
    x = 'AdamNowak'
    cos = re.sub(r'([a-z])([A-Z])', r'\1 \2', x)
    print(cos)
    cos2 = re.sub(r'([a-z])([A-Z])', r'\1 alicja \2', x)
    cos3  = re.sub(r'([a-z])([A-Z])', r'\1  %s \2' %x, x)
    
    print(cos2)
    print(cos3)




def dwieduze_naduzamala():
    tekst = 'AAgggABgF'
    import re
    subst = re.sub(r'([A-Z])([A-Z])', lambda x: x.group(1) + x.group(2).lower(), tekst)
    print(subst)




def zdania_duzalitera():
    tekst = 'Ala ma kota. Kot ma Ale.'
    tekst2 = 'bSDVRE G?rAAdbT f. KWAJVIR njndj KSrgtR. eSHTYx fgbes.'
    tekst3 = tekst2.split(' .')
    for zdanie in tekst3:
        print('')
        

def spaaacje2():
    import re
    tekst = " KasiaKowalska AdamNowak"
    re.findall(r'(a-z)(A-Z)', tekst)
    tekst2 = re.sub(r'([a-z])([A-Z])', 'a', tekst)
    print(tekst2)
  



def spaaacje():
    import re
    tekst = " KasiaKowalska AdamNowak"
    re.findall(r'(a-z)(A-Z)', tekst)
    tekst2 = re.sub(r'([a-z])([A-Z])', r'\1 \2', tekst)
    print(tekst2)

def duze_litery():
    
    s = "DZisiaj jest czwartek. JUtro będzie piątek"
    import re
    s2 = re.sub(r'([A-Z])([A-Z])', lambda x: x.group(1) + x.group(2).lower(), s)
    print(s2)

#zaddom
def zdania(s):
    '''(string) -> string
    przyjmuje ciąg tekstowy, który przekształca tak,
    by zdania zaczynały się z wielkiej litery, a wszystkie inne znaki były małe
    >>>zdania('aldaAS dsADWF ADSshtKK. Gdwygh GIRT. fvrgoij muewrsd we. EEE.')
    Aldaas dsadwf adsshtkk. Gdwygh girt. Fvrgoij muewrsd we. Eee. 
    '''
    import re
    #pozbywam się kropki na końcu, jeśli jest
    if s[-1] == '.':
        s = s[:-1]
    else:
        None
    zdania = []
    for zdanie in s.split('. '):
        zdanie2 = re.sub(r'(^.)(.*$)', lambda x: x.group(1).upper() + x.group(2).lower(), zdanie)
        zdania.append(zdanie2 + '. ')
    sek = ''
    for i in range(len(zdania)):
        sek = sek + zdania[i]

    return(sek)

#ZAPYTAJ DLACZEGO NIE DZIAŁA DLA CAŁEJ ZEKWENCJI I TRZEBA PĘTLĄ ROBIC

#zaddom
def zadanie5(tekst):
    '''(string) -> string
    przyjmuje tekst, znajduje w nim daty w formacie YYYY-MM-DD
    i przekształca na format DD-MM-YYY
    >>>zadanie5('siabadaba 1234-12-09 amore. Oj amore 2021-12-30. Hell yeah 25-06-1998. Kropaaa')
    siabadaba 09-12-1234 amore. Oj amore 30-12-2021. Hell yeah 25-06-1998. Kropaaa
    '''
    import re
    tekst2 = re.sub(r'([0-9]{4})-([0-9]{2})-([0-9]{2})', lambda x: x.group(3) + '-' + x.group(2) + '-' + x.group(1), tekst)
    return tekst2





def zad4ponowne():
    import re
    s = 'aldaAS dsADWF ADSshtKK. Gdwygh GIRT. fvrgoij muewrsd we. EEE.'
    s2 = re.sub(r'(^.)(.*.[.])', lambda x: x.group(1).upper() + x.group(2).lower(), s)
    print(s2)


















