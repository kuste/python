
#vjezba11 zad 2

from turtle import *
speed(0)

def kvadrat(duljina):
    pu()
    goto(-duljina//2,-duljina//2)
    pd()
    for i in range(4):
    
        fd(duljina)
        lt(90)

    return

def main():
    reset()
    n=int(input('unesite duljinu stranice u pikselima: '))

    if n>0:
        
        kvadrat(n)
    else:
        print('greska')
    
    return


main()


pu()

mainloop()
