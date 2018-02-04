
#vj11 zd 02


s=str(input('Unesite neki string: '))

def samoglasnici(string):
    br=0
    string=string.lower()
    for i in string:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            br+=1

    

    return int(br)

def main():

    
    postotak=(samoglasnici(s)/len(s))
    print('Broj samoglasnika u stringu "{}" je {}, sto cini {:.2%} od ukupnog broja znakova. '.format(s,samoglasnici(s),postotak))

    return

if __name__=='__main__':
          main()
