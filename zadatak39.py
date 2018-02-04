ulaz=open('ulaz.txt','r')
izlaz=open('izlaz.txt','w')
lista=ulaz.readlines()
o=''
r=[]
for i in lista:
    o=str(i)
    podlista=o.split()

    if '*' in podlista:
        rez1=float(podlista[0])*float(podlista[2])
        r.append(str(rez1))

    if '/' in podlista:
        rez1 = float(podlista[0]) / float(podlista[2])
        r.append(str(rez1))

    if '+' in podlista:
        rez1=float(podlista[0]) + float(podlista[2])
        r.append(str(rez1))

    if '-' in podlista:
        rez1=float(podlista[0]) - float(podlista[2])
        r.append(str(rez1))
print(lista, podlista, r)

r='\n'.join(r)
izlaz.write(r)

ulaz.close()
izlaz.close()

