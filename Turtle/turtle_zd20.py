#CRTA JELKICU OD KRUGOVA

from turtle import *
from random import *

speed(0)
colormode(255)

def krug(a):
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    fillcolor(r, g, b)
    begin_fill()
    circle(a)
    end_fill()


def red(a,b):
    for i in range(b):
        fd(2 * a)
        krug(a)

def main():
    a=int(input('unesite radius kruga: '))
    b=int(input('unesite broj krugova: '))
    j=2
    pu()
    for i in range(b):
        goto(i*a,j*2*a)
        red(a,b)
        b-=1
        j+=1

main()
mainloop()