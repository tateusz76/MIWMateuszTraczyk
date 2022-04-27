import numpy as np
import random

#plik = open("australian.dat")
plik = open("test.dat")
lista = []
for line in plik:
    lista.append(list(map(lambda e:float(e) , line.replace('\n','').split(' '))))
plik.close()

plik2 = open("test.dat")
oryginal = []
for line in plik2:
    oryginal.append(list(map(lambda e:float(e) , line.replace('\n','').split(' '))))
plik2.close()

x=[1,1,1,1,1,1,1,1,1,1,1,1,1,1]


def euklides2(lista1, lista2):
    lista1 = lista1[:-1]
    lista2 = lista2[:-1]
    v1 = np.array(lista1)
    v2 = np.array(lista2)
    c=0
    for i in range(len(v1)):
        c += (v1[i]-v2[i])**2

    return c**(1/2)

#print(euklides2(lista[0], lista[1]))



bezKlasy=lista

for i in range(len(bezKlasy)):
    bezKlasy[i] = bezKlasy[i][:-1]

def dodajKlase(lista):
    for i in range(len(bezKlasy)):
        klasaRandom = random.randint(0,1)
        bezKlasy[i].append(klasaRandom)
        
dodajKlase(bezKlasy)
#print(bezKlasy)

#print(euklides2(bezKlasy[5], bezKlasy[4]))


def podzielKlasy(bezKlasy, klasa):
    odleglosci = []
    odl = 0
    jednaKlasa = []
    for i in range(len(bezKlasy)):
        if(bezKlasy[i][-1] == klasa):
            jednaKlasa.append(bezKlasy[i])

    return jednaKlasa


klasa0 = podzielKlasy(bezKlasy, 0)
klasa1 = podzielKlasy(bezKlasy, 1)

oryginal0 = podzielKlasy(oryginal, 0)
oryginal1 = podzielKlasy(oryginal, 1) 

print(oryginal1)

def odleglosc(wiersz1, wiersz2):
    tabOdl = []
    for i in range(len(wiersz1)):
        odl = euklides2(wiersz1, wiersz2)
    #tabOdl.append(odl)
        
    return odl

#print(odleglosc(bezKlasy[0], bezKlasy[1])) #odległość od wiersza 1 do wiersza 2


def odlegloscDlaWierszy(tab):
    odlDlaWiersza = []
    sumaDlaWierszy = []
    for i in range(len(tab)):
        suma = 0
        for j in range(len(tab)):
            odl = euklides2(tab[i],tab[j-1])
            #odlDlaWiersza.append(odl)
            suma =  suma + odl
        sumaDlaWierszy.append(suma)
    return sumaDlaWierszy
    
print("Generowane: ")

odlTab0 = odlegloscDlaWierszy(klasa0)
odlTab0.sort()
print("Środek ciężkości dla klasy 0: " + str(odlTab0[0]))

odlTab1 = odlegloscDlaWierszy(klasa1)
odlTab1.sort()
print("Środek ciężkości dla klasy 1: " + str(odlTab1[0]))


print("Australian: ")

odlOg0 = odlegloscDlaWierszy(oryginal0)
odlOg0.sort()
print("Środek ciężkości dla klasy 0: " + str(odlOg0[0]))

odlOg1 = odlegloscDlaWierszy(oryginal1)
odlOg1.sort()
print("Środek ciężkości dla klasy 1: " + str(odlOg1[0]))
print("\n")

pokrycie = 0
for i in range(len(oryginal)):
    if(oryginal[i] == bezKlasy[i]):
        pokrycie = pokrycie + 1
pokrycie = pokrycie / len(oryginal)

print("Podobieństwo między klasami decyzyjnymi w oryginalnym pliku i wygenerowanym: ")
print(str(pokrycie) + "%")




            


