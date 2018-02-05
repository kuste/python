#CRTA RAZNOBOJNE LINIJE IZ ISTE TOCKE, RAZLICITE DUZINE



from turtle import *
from random import *

br_linija=int(input('broj linija: '))
duljina_linija=int(input('buljina: '))
speed(0)
n=duljina_linija
pensize(5)
colormode(255)

for i in range(br_linija):
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    pencolor(r, g, b)
    fd(n)
    pu()
    bk(n)
    pd()
    lt(20)
    n=n-(n*0.1)

mainloop()