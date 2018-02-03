#Ivica Kustura
#vjezba11 zad 3


from turtle import *
speed(0)

n=int(input('Unesite br vrhova str. '))

reset()
if n>2:
    
    for i in range(n):
        write(str(i+1),align='right')
        fd(100)
        lt(360/n)
        
else:
    print()
