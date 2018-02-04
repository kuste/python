s=str(input('string: '))
s=s.upper()
a = s.count('LJ')
b = s.count('NJ')
c = s.count('C-')
d = s.count('C=')
e = s.count('S=')
f = s.count('Z=')
g = s.count('D-')
dz = s.count('DZ=')

ukupno = a+b+c+d+e+f+g

preostalo = len(s) - (ukupno-dz)*2 - dz*3
rezultat = ukupno + preostalo

#print(ukupno)
#print(dz)
print(rezultat)