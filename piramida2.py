wysokosc_piramidy = int(input('podaj wysokość piramidy:'))
odstep_od_lewej = wysokosc_piramidy
for x in range(wysokosc_piramidy+1):
    y = ((2*x-1) * '#')
    print(odstep_od_lewej * ' '+y)
    odstep_od_lewej -= 1
