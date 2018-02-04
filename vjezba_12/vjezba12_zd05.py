
#vj12zd05
from turtle import *
from random import *
n=int(input())
speed(0)
colormode(255)
a=300

for i in range(5):
    r = randint(0, 255)
    fillcolor(r,r,r)
    begin_fill()
    for i in range(3):
        fd(a)
        lt(120)

    a=a-n

    end_fill()

mainloop()


