ulaz=open('ulaz43.txt','r')
izlaz=open('izlaz.txt','w')

sve=ulaz.readlines()


listagradova=[]
listabrojeva=[]
for i in sve:
    grad=i.split()
    for j in grad:
        if not j.isdigit()==True:
            listagradova.append(grad[0])

        else:
            total=0
            for j in range(1,len(grad)):
                total+=int(grad[j])
            prosjek=round(total/(len(grad)-1),2)
    listabrojeva.append(prosjek)


for k in range(len(listabrojeva)):
    konacnalista=str(listagradova[k])+' '+str(listabrojeva[k])+'\n'


    izlaz.write(konacnalista)

