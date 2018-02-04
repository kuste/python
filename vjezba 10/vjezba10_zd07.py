
#vjezba 10 zad 7


ulaz = open('ulaz7.txt','r')
izlaz = open('izlaz7.txt', 'w')

broj=[]
element=ulaz.readlines()
for i in element:
    broj.append(i)

    
broj=broj[0]
broj=broj.split()
lista=[]
for i in broj:
    try:
        n = int(float(i))
        lista.append(n)
    except:
        [lista.append(int(i)) for i in list(i) if i.isdigit() ]
        
        while 0 in lista:
            lista.remove(0)
            
        continue
    
lista.sort()
izlaz.write(','.join(map(str,lista)))


ulaz.close()
izlaz.close()
