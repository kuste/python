
#Vježba 10 - zadatak 6

ulaz = open('ulaz6.txt','r')
izlaz = open('izlaz6.txt', 'w')

lista_ljudi = ulaz.readlines() 
duzina_liste_ljudi = len(lista_ljudi)
osoba = ""
indeks_string = ""

indeks_lista = [] 

for i in range(duzina_liste_ljudi):

    osoba = lista_ljudi[i] 

    osoba_lista = osoba.split() 

    ime_osobe = osoba_lista[0] 
    kg_osobe = float(osoba_lista[1])
    visina_osobe = float(osoba_lista[2])

    indeks_mase = float(kg_osobe/(visina_osobe)**2) 
    indeks_mase = round(indeks_mase, 2) 

    indeks_string = str(indeks_mase) + " " + ime_osobe 
    indeks_lista.append(indeks_string) 


indeks_lista.sort() 

izlazni_string = "" 

for i in indeks_lista: 
    a = i.split() 

    if len(a[1]) > 8: 
        izlazni_string = str(a[1]) + "\t" + str(a[0]) + "\n" 
        izlaz.write(izlazni_string)
    else:
        izlazni_string = str(a[1]) + 2*"\t" + str(a[0]) + "\n"
        izlaz.write(izlazni_string)
        

ulaz.close()
izlaz.close()

