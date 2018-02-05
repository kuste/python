#CRTA DANDOM OBOJANE KVADRATE NA RANDOM POZICIJAMA

from turtle import *
from random import *

speed(0)
colormode(255)
tracer(False)
def kvadrat(a):
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    begin_fill()
    fillcolor(r,g,b)
    for i in range(4):
        fillcolor()
        fd(a)
        lt(90)
    end_fill()

    return

def main():

    n = int(input('velicina kvadrata: '))
    k = int(input('broj kvadrata: '))

    for i in range(k):
        x = randint(-600, 600)
        y = randint(-600, 600)
        pu()
        goto(x,y)
        pd()
        kvadrat(n)


    return

main()
mainloop()