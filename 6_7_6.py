'''je li broj prost'''
'''jos jedna funkcija koja ce vracati koliko je prostih brojeva izmedju dva prirodna'''
'''vracati n po redu prosti broj'''
'''ispisivati sve susjedne proste brojeve do n; razlika im je 2'''

def prost(n):


    for i in range(2, round(n ** (1 / 2) + 1)):
        if n % i == 0:
            return False
    if n > 1:
        return True
    else:
        return False


def izmedju (n, m):
    brojeva=0
    for i in range(n,m+1):
        if prost(i):
            brojeva+=1
        else:
            continue

    return brojeva

def susjedi(n):

    lista = []
    izlaz = ""
    for i in range(1, n):
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        if count < 3:
            lista.append(int(i))

    for p in range(len(lista)-1):
        if lista[p] == lista[p+1] - 2:
            izlaz += str(lista[p]) + " " + str(lista[p+1]) + "\n"
    return izlaz


def nporedu (n):
    listaprostih = [2, ]
    brojprostih = 1
    broj = 3
    while brojprostih < n:
        if prost(broj):
            listaprostih.append(broj)
            brojprostih += 1
        broj += 2


    return max(listaprostih)





def main():

    n = input('unesite a za "izmedju", b za "susjedi" c za "nporedu":  ')
    if n=='a':

        d = int(input('unesite donju granicu '))
        g = int(input('unesite gornju granicu '))
        print(izmedju(d,g))
    if n=='b':
        unos=int(input('unesite broj: '))
        print(susjedi(unos))
    if n=='c':
        unos=int(input('unesite broj: '))
        print(nporedu(unos))

main()

