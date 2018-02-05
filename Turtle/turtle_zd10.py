#TRI KVADRATA OKO JEDNAKOSTR TROKUTA

from turtle import *
from random import *

speed(0)
colormode(255)
tracer(False)

def kvadrat(a):

    fillcolor('blue')
    begin_fill()
    for i in range(4):
        fd(a)
        rt(90)
    end_fill()


def main():

    a=int(input('str kvadrata: '))
    for i in range(3):
        kvadrat(a)
        fd(a)
        lt(120)


main()
mainloop()
