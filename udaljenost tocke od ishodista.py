from math import *

def tocka(a):
    a = a.replace('(','')
    a = a.replace(')','')
    a = a.split(',')
    return float(a[0]), float(a[1])

def d(a,b):

    return sqrt(a**2+b**2)


def main():
    a=input('a: ')
    b=input('b: ')
    xa,ya = tocka(a)
    xb,yb = tocka(b)
    if d(xa,xb)<d(ya,yb):
        xa,ya,xb,yb = xb,yb,xa,ya

    print(xa,ya)

    return




if __name__=='__main__':
    main()
