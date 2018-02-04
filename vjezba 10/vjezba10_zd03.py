#zad 3 vj 10

f_ulaz = open('ulaz3.txt','r')
f_izlaz = open ('izlaz3.txt','w')


lista= f_ulaz.readlines()



for i in range(len(lista)):
    f_izlaz.write(str(i+1)+'.'+lista[i])
    
     





f_ulaz.close()
f_izlaz.close()
