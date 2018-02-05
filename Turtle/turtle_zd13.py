#CRTA NTEROKUT OKO NTEROKUTA

from turtle import *

tracer(False)

def nterokut(a,br_kuteva):
    kut=360/br_kuteva
    for i in range(br_kuteva):
        fd(a)
        lt(kut)

    return

def main():
    pd()
    n=int(input('unesite broj str opisanih nterokuta: '))
    k=int(input('uneiste broj str srednjeg nterokuta: '))
    a=int(input('velicina str nterokuta: '))
    for i in range(k):
        for i in range(k):
            fd(a)
            rt(int(360/k))
            nterokut(a,n)





main()
mainloop()
