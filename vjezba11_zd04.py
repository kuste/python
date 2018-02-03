
#vjezba11 zad 4

from turtle import *
speed(0)

n=int(input('Unesite br vrhova str. '))

reset()
if n>2:
    pu()
    goto(0,-200)
    pd()
    circle(200)
    circle(200,steps=n)
        
else:
    print()
