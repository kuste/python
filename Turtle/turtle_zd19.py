#CRTA KVADRAT S OPISANIM POLUKRUZNICAMA

from turtle import *
from random import *

speed(5)
colormode(255)
def kvadrat(a):
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    fillcolor(r, g, b)
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()

    return

def komad(a):
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    fillcolor(r,g,b)
    begin_fill()
    circle(a,extent=180)
    end_fill()
    rt(90)

def main():
    n=int(input('unesite str kvadrata: '))
    pu()
    kvadrat(n)
    goto(n,0)
    for i in range(4):
        komad(n/2)


main()
mainloop()