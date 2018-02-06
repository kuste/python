
'''definiraj funkciju koja će vraćati zbroj prvih n brojeva'''

def zbroj(n):

    z = 0
    for i in range(n+1):
        z += i

    return z

def main():

    n = int(input('unesite neki broj '))
    z = zbroj(n)

    print(z)

main()
