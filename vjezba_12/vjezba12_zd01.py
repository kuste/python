
#vj12zd01
from random import *

n=int(input('unesite broj brojeva: '))
if n>0:
    lista1=[randint(1,100) for i in range(n) ]
    listap=[i for i in lista1 if i%2==0]
    listan=[i for i in lista1 if i%2!=0]
 
    print('u listi {} ima {} parnih i {} neparnih br.'.format(lista1,len(listap),len(listan)))
else:
    print('Trebate unjeti broj veci od 0. ')