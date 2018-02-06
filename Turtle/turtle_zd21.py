#CRTA LATICE RANDOM BOJA

from turtle import *
from random import *

speed(0)
colormode(255)

def latica(a):
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    fillcolor(r, g, b)
    begin_fill()
    circle(2 * a, extent=60)
    lt(120)
    circle(2 * a, extent=60)
    end_fill()

def main():
    a=236
    pu()
    for i in range(6):
        seth(i*60)
        latica(a)


main()
mainloop()