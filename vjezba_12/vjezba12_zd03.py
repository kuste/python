#vj11 zd 03


ulaz=open('ulaz.txt','r')
izlaz=open('izlaz.txt','w')
u=ulaz.read()
u=u.split()

print(ulaz)

d=[]
for i in u:
    a=[tuple(u[i:i+2]) for i in range(0, len(u), 2)]
    

    b=sorted(a, key=lambda element: (element[1], element[0]))
    
    c=''
    
    for i in b:
        
        i=' '.join(i)
        c+=i+' '+'\n'
        
print(b)
izlaz.write(c)    
ulaz.close()
izlaz.close()
