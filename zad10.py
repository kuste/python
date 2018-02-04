


s='PROGRAMIRANJE'
l=len(s)
if l%2==0:
    for i in range(0,l,2):
        print(s[i+1],end='')
        print(s[i],end='')

else:
    for i in range(0,l-1,2):
        print(s[i+1],end='')
        print(s[i],end='')
    print(s[l-1])