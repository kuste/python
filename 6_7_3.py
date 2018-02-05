
'''na osnovi koeficijena kvadratne funkcije vracati true ili false ako ima realne nultocke'''


def real(a,b,c):

    d = b**2 - 4*a*c
    if d >= 0:
        return True
    else:
        return False

def main():

    print('Unesite parametre kvadratne funkcije: ')
    a = float(input('a '))
    b = float(input('b '))
    c = float(input('c '))

    r = real(a,b,c)
    print(r)

main()
