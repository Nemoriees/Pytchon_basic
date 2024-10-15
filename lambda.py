import math
def obwod(r):
    obwod = lambda x: 2*x*math.pi
    
    #print (obwod(r))
    return obwod
def sznurek():
    '''zakładamy, że mamy zrobić okrąg ze sznura. Sznur ma określoną długość
    jaki promień może mieć koło'''
    radius = int(input('jaki promien chcesz sprawdzic? '))
    lengh = int(input('jaki długi jest sznur? '))
    if int(obwod(radius)) > lengh:
        print('za krótki')
        return False
    else:
        print('za dlugi')
        return True
