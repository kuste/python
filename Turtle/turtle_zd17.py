#CRTA KRUZNE ISJECKE RANDOM BOJOM

from turtle import *
from random import *

speed(0)
colormode(255)
def komad(a):
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    fillcolor(r,g,b)
    begin_fill()
    circle(a,extent=90)
    lt(90)
    fd(a)
    lt(90)
    fd(a)
    end_fill()

def main():
    n=100
    pu()

    komad(n)
    lt(90)
    goto(n,n)
    lt(90)
    komad(n)
    goto(0,2*n)
    lt(180)
    komad(n)
    goto(-n,n)
    lt(180)
    komad(n)






main()
mainloop()