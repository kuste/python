#PLAVO ZUTA SAHOVNICA

from turtle import *
from random import *

speed(0)
colormode(255)
tracer(False)

def kvadrat(a,boja):
    fillcolor(boja)
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()
    fd(a)




def red(a,n,promjeni):
    if promjeni%2==0:
        for i in range(n):
          kvadrat(a,'blue')
          kvadrat(a, 'yellow')

    else:
        for i in range(n):
          kvadrat(a,'yellow')
          kvadrat(a, 'blue')




def main():
    n=int(input('unesite broj polja: '))
    a=int(input('unesite velicinu kvadrata :'))
    i=0
    p=2
    pu()
    for i in range(n):
        goto(0, a * i)
        red (a, int(n/2), p)
        i+=1
        p+=1
main()
mainloop()