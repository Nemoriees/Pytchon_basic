#zaddom - cwiczenia 6
#zadanie 6
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

#wcześniej próbowałam to zadanie zrobić prościej:
def zad4ponowne():
    import re
    s = 'aldaAS dsADWF ADSshtKK. Gdwygh GIRT. fvrgoij muewrsd we. EEE.'
    s2 = re.sub(r'(^.)(.*.[.])', lambda x: x.group(1).upper() + x.group(2).lower(), s)
    print(s2)
#niestety funkcja nie działa (tak jakby traktowała całego stringa jako jedno zdanie)
#jak można ją poprawić?

#zadanie5
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
