'''je li broj savrsen'''
'''sve savrsene brojeve do n'''

def savrsen(n):

    a = n // 2
    s = 0

    for i in range(1, a+1):
        if n % i == 0:
            s += i

    if s == n:
        return True
    else:
        return False

def popis(n):

    lista = []
    for i in range(1, n+1):
        a = i // 2
        s = 0

        for j in range(1, a + 1):
            if i % j == 0:
                s += j

        if s == i:
            lista.append(i)

    return lista

def main():

    n = int(input('unesi neki broj '))
    r = savrsen(n)
    if r == True:
        print('Ovaj broj je savrsen ')
    else:
        print('Ovaj broj nije savrsen')

    p = popis(n)

    if len(p) > 0:

        print('Savrseni brojevi do ', n, ' su ', p)
    else:
        print('Ne postoji')



main()
