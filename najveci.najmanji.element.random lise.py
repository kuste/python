from random import *
def veci_manji(a):
    najveci=najmanji=a[0]
    
    for i in range(1,20):

        if a[i]> najveci:
            najveci = a[i]
        if a[i] < najmanji:
            najmanji = a[i]
    return najveci, najmanji

def main():
    a=[randint(1,100) for i in range(20)]
    print(a)
    veliki,mali=veci_manji(a)
    print('najveci je: ',veliki, 'najmanji je: ',mali)

main()
