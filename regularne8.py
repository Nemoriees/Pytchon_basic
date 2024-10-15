import re

L = ["Adam Nowak", "Kasia Klimczak", "Maria Rudzik", "Wiktor Wiktorowicz"]

def CheckInitials(listX):
    '''Przyjmuje liste stringow imion i nazwisk, zwraca nam elementy listy, ktore maja takie same litery na poczatku imion i nazwisk'''
    splited_listX = []
    result_list = []
    for i in listX:
        splited_listX.append(i.split())
    for j in splited_listX:
        found_name_initial = re.search(r"^[A-Z]", j[0])
        found_surname_initial = re.search(r"^[A-Z]", j[1])
        if str(found_name_initial) == str(found_surname_initial):
            result_list.append(j[0] + " " +j[1])

    return result_list

print(CheckInitials(L))