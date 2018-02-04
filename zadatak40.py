ulaz=open('ulaz.txt','r')
izlaz=open('izlaz.txt','w')

u=ulaz.read()
lista=u.split()

l=len(lista)
izlaz.write(str(l))

lista2=[]

for i in lista:
    if len(i) < 5:
        lista2.append(i)

print(lista2)

a='\n'.join(lista2)
izlaz.write(a)
print(len(lista))