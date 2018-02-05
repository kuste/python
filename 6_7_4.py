
'''zbroj znemenaka nekog broja'''

def zbroj(n):

    s = 0
    if n < 0:
        n = -1 * n
    
    while n > 0:
        m = n % 10
        n = n // 10
        s += m
    return s

def main():

    n = int(input('unesi neki broj '))
    z = zbroj(n)

    print(z)

main()
