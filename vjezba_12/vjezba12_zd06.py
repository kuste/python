
#vj12zd06

from random import *

print('dobrodosli u loto 7/39. za prekid igre unesite 0 ')


lista_u=[]
b=0
while b < 7:
    try:
      
       n=int(input('unesite broj '))
   
       if n in range(1,40):
       
           if n not in lista_u:
               lista_u.append(n)
               b+=1
       
           
           else:
               print('unjeli ste isti broj.')
               b=b
           
               continue
        
       elif n==0:
            break
   
       else:
            print('unesite ponovo')
            b=b
    except:
        print('Unjeli ste slovo: ')
        b=b
def izvlacenje():
    
    lista_i = [i for i in range(1,40)]   
    lista_k = sample(lista_i, 7)
    
    return lista_k
    
    

def usporedi(lista1,lista2):

    lista_r = list()
    a=0
    for e in lista1:
        if e in lista2:
            lista_r.append(e)
            a+=1
    	
    return lista_r, a
    	
    	
def main ():

    print('unjeli ste ', lista_u)
    rez=izvlacenje()
    r=usporedi(lista_u, rez)
    
    print('izasli su brojevi: ',rez)
    print(' pogodili ste ', r)
    
    return
    
    
if __name__=='__main__':
    main()
    
    
    
       
    
 


