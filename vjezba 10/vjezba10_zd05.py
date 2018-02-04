
#Vježba 10 - zadatak 5

def broji_znamenke(znamenka, string):

    
    znamenka_str = str(znamenka)
    count = string.count(znamenka_str)
    postotak = float(count/len(string))
    postotak = round(postotak, 2)
    return postotak

def main():

    
    ulaz = open('ulaz5.txt','r')
    izlaz = open('izlaz5.txt','w')

    string = ulaz.read()
    ispis = ""
    
    for i in range(10):
        digit = str(i)
        if digit in string:
            znamenka = i
            broj = broji_znamenke(znamenka, string)
            ispis = str(i) + "-" + str(broj) + "\n"
            izlaz.write(ispis)
            
    
    ulaz.close()
    izlaz.close()

main()


