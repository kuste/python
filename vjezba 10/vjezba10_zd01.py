#zad 1 Vjezba 10

f_ulaz = open('ulaz1.txt','r')

s=f_ulaz.read()
izlaz=str()

for i in s:
    if str.isalpha(i):
        izlaz +=i

print(izlaz)

f_ulaz.close()
