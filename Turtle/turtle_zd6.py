#CRTA N PRAVOKUTNIKA U 2 BOJE

from turtle import *

n=int(input('broj provokutina: '))
a=int(input('str. a: '))
b=int(input('str. b: '))
speed(0)
def pravokutnik(a,b):
    for i in range(2):
        fd(a)
        lt(90)
        fd(b)
        lt(90)

    return

for i in range(int(n/2)):

    begin_fill()
    fillcolor('blue')
    pravokutnik(a,b)
    end_fill()
    fd(a)
    begin_fill()
    fillcolor('yellow')
    pravokutnik(a,b)
    fd(a)
    end_fill()


mainloop()