#SIMETRALE STRANICA I KUTA OKO NTEROKUTA

from turtle import *

speed (10)
def nterokut(a,br_kuteva):
    pencolor('red')
    kut=360/br_kuteva
    for i in range(br_kuteva):
        fd(a)
        lt(kut)

    return

def simetrala_kuta(a, br_kuteva):
    pencolor('blue')
    kut = int(((br_kuteva-2)*180)/br_kuteva)
    pu()
    fd(a)
    lt(180)
    rt(kut/2)
    pd()
    bk(a/2)
    fd(a/2)
    rt(kut/2)
    return

def simetrala_str(a,br_kuteva):
    pencolor('green')
    kut = int(360 / br_kuteva)
    pu()
    fd(a/2)
    lt(int(90))
    pd()
    bk(a)
    fd(a)
    rt(90)
    pu()
    fd(a/2)
    lt(kut)
    return

def main():
    n = int(input('broj kutova: '))
    a = int(input('velicina str: '))
    nterokut(a, n)
    home()
    for i in range(n):
        simetrala_kuta(a, n)
    for i in range(n):
        simetrala_str(a, n)

    return

main()
mainloop()
