def deleteLine(id):
    fn = 'pracownicy2.txt'
    f = open(fn)
    output = []
    #id="czwarta"
    for line in f:
        if not line.startswith(id):
            output.append(line)
    f.close()
    f = open(fn, 'w')
    f.writelines(output)
    f.close()
    deleteLine()

def addline():
    import fileinput
    for line in fileinput.FileInput('pracownicy2.txt',inplace=1):
        if "druga" in line:
            line = line.replace(line,line+"NEW_TEXT")
    print(line)

def nowa():
    x = 3+4
    print(x)

