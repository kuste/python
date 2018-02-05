from turtle import *


def kvadrat(a):
    for i in range(4):
        fd(a)
        lt(90)
    return

def main():
    speed(10)
    a = int(input('kvad. a: '))
    b = int(input('kvad. b: '))
    c=str(input('boja1: '))
    e=str(input('boja2: '))
    fillcolor(c)
    begin_fill()
    kvadrat(a)
    end_fill()
    fillcolor(e)
    begin_fill()
    kvadrat(b)
    end_fill()
    mainloop()

    return


main()