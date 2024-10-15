import glob
def funkcja(text):
    text = glob.escape('Nana[{|}]na$%?%@&*')
    return text

def funkcja2():
    a = glob.glob('plik1.pydocx')
    return a

import os

def funkcja3():
    # change the current working directory
    # to specified path
    
    os.chdir('c:\\Users\ewa\Desktop\drugi')
     
    # verify the path using getcwd()
    cwd = os.getcwd()
     
    # print the current directory
    print("Current working directory is:", cwd)
    a = os.listdir('c:\\Users\ewa\Desktop\os glob')
    print(a)
    b = os.path.exists('c:\\Users\ewa\Desktop\osglob')
    print(b)
