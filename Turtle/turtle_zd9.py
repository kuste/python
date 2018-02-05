#POLA RAZNOBOJNE SAHOVNICE

from turtle import *
from random import *

speed(0)
colormode(255)
tracer(False)

def kvadrat(a):
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    fillcolor(r,g,b)
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()
    fd(a)




def red(a,n):
        for i in range(n):
          kvadrat(a)





def main():
    n=int(input('unesite broj polja: '))
    a=int(input('unesite velicinu kvadrata :'))
    i=0
    p=2
    pu()
    for i in range(n):
        goto(0, a * i)
        red (a, int(n))
        i+=1
        p+=1
        n-=1
main()
mainloop()