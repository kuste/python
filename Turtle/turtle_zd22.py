#CRTA KRUZNICE U KRUG

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

    return


def main():
    pu()
    a=100

    krug(a)
    circle(a,60)
    rt(180)
    for i in range(5):
        krug(a)
        circle(a,120)
        rt(180)

main()
mainloop()