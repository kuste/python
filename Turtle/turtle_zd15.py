#CRTA RAZNOBOJNE KRUZNICE KRUZNICE JEDNA UNUTAR DRUGE

from turtle import *
from random import *
tracer(False)
colormode(255)

n=int(input('polumjer kruznice: '))
r=n//10

for i in range(r):
    pu()
    goto(0, -n)

    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    fillcolor(r, g, b)
    begin_fill()
    circle(n)
    end_fill()
    n -=10

mainloop()




