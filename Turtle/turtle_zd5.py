
#CRTA SKALE

from turtle import *

n=int(input('unesi broj skala: '))
a=int(input('unesi velicinu skale: '))
speed(0)


for i in range(n):
    lt(90)
    fd(a)
    rt(90)
    fd(a)

mainloop()