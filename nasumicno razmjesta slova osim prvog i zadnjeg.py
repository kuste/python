from random import *

def razmjena(s):
    lista=list(s[1:len(s)-1])
    shuffle(lista)
    novi =s[0]
    for i in range(len(lista)):
        novi +=lista[i]
    novi +=s[-1]
    return novi

def main():
    s=input('Unesite string: ')
    print(razmjena(s))
    return

main()
