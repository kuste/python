#KVADRAT S UPISANE 4 KRUZNICE
from random import *
from turtle import  *
speed(0)
colormode(255)
def kvadrat(a):
    fillcolor('yellow')
    begin_fill()
    for i in range(4):

        fd(a)
        lt(90)
    end_fill()

    return

def main():

    n=int(input('unesite stranicu kvadata: '))
    pu()
    kvadrat(n)
    fd(n / 4)
    for i in range(4):
        fd(n/2)
        fd(n / 4)
        lt(90)
        fd(n / 4)
        r = randint(0,225)
        g = randint(0,225)
        b = randint(0,225)
        fillcolor(r,g,b)
        begin_fill()
        circle(n/4)
        end_fill()


main()
mainloop()

