

def modul_choinki(a, nazwa):
    import datetime
    import sys
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


def choinka():
    k = sys.argv[1:]
    print(k)





    
