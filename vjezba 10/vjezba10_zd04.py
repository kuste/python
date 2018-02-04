
#zad 4 vj 10


f_ulaz = open('ulaz4.txt','r')
f_izlaz = open ('izlaz4.txt','w')


lista= f_ulaz.readlines()
temp=str()

try:
    for i in range(len(lista)):
        
        linija=lista[i].split()
        
        if linija[1]=='+':
            temp=float(linija[0])+float(linija[2])
           

        elif linija[1]=='-':
            temp=float(linija[0])-float(linija[2])

        elif linija[1]=='*':
            temp=float(linija[0])*float(linija[2])
        
        elif linija[1]=='/':
            temp=float(linija[0])/float(linija[2])


        f_izlaz.write(str(temp)+'\n')
                       
     
except:
   print('greska') 




f_ulaz.close()
f_izlaz.close()
