
#vj 10 zad 8

from kompresija import *

 
print('unesite k za kompresiju ili d za dekompresiju: ', end='')
unos=input()
if unos=='k':
    ulaz=open(input('unesite naziv datoteke za kompresiju: ' ),'r')
    izlaz=open(input('unesite naziv datoteke za pohranu: ' ),'w')
    komp=kompresija(ulaz.read())
    izlaz.write(komp)
    
    ulaz.close()
    izlaz.close()
    
if unos=='d':
    ulaz=open(input('unesite naziv datoteke za dekompresiju ' ),'r')
    izlaz=open(input('unesite naziv datoteke za pohranu ' ),'w')
    komp=dekompresija(ulaz.read())
    izlaz.write(komp)
    
    ulaz.close()
    izlaz.close()
    
