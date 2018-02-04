from codecs import *
u=open('ulaz.txt','r',encoding='utf8')
iz=open('izlaz.txt','w',encoding='utf8')

ul = u.readline()
znakovi = ul.split()

tekst = u.read()
tekst_lista = tekst.split()

rezultat = []

for i in znakovi:

    for j in tekst_lista:

        if i in j and j not in rezultat:
            rezultat.append(j)

print(rezultat)
