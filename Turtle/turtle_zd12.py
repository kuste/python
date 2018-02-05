#JEDNAKOSTR TROKUTI OKO JEDNE TOCKE

from turtle import *
from random import *

colormode(255)
tracer(False)


def trokut(a):
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    fillcolor(r, g, b)
    begin_fill()
    for i in range(3):
        fd(a)
        lt(120)
    end_fill()

    return

def main():
    pu()
    n=int(input('unesite broj trokuta: '))
    a=int(input('unesite str tokuta: '))
    for i in range(n):
        kut=360/n
        a=100
        trokut(a)
        lt(kut)





main()
mainloop()


