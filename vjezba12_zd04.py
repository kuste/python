#Ivica Kustura
#vj12 zd4


def tocka(a):
    a = a.replace('(','')
    a = a.replace(')','')
    a = a.split(',')
    return float(a[0]), float(a[1])
def povrsina_trokuta (a,b,c):
    x1, y1 = tocka(a)
    x2, y2 = tocka(b)
    x3, y3 = tocka(c)
    p=0.5*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))

    return p



def main():
    a = input('inesite koordinatu: ')
    b = input('inesite koordinatu: ')
    c = input('inesite koordinatu: ')

    a=povrsina_trokuta(a, b, c)
    if a<1:
        r=print('Zadane tocke ne tvore trokut!')
        return r
    else:
        r=print('povrsina trokuta je: ',a)

        return r

main()
