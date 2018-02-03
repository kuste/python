#vjezba11 zad 5

from turtle import *
speed(0)

n=int(input('Unesite br vrhova str. '))

reset()
if n>2:
    pu()
    goto(0,-200)
    pd()
    fillcolor('red')
    begin_fill()
    circle(200)
    end_fill()
    fillcolor('blue')
    begin_fill()
    circle(200,steps=n)
    end_fill()
        
else:
    print()
