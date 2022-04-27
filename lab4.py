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
print("\n")

def odleglosc(wiersz1, wiersz2):
    tabOdl = []
    for i in range(len(wiersz1)):
        odl = euklides2(wiersz1, wiersz2)
    #tabOdl.append(odl)
        
    return odl

#OD TĄD ZACZYNAĆ POPRAWKI - MA BYĆ TABELA ODLEGŁOŚCI OD NP PIERWSZY WIERSZ DO KAŻDEGO, POTEM DRUGI DO KAŻDEGI ITP.... I POTEM TE ODLEGŁOŚCI SUMUJEMY [sumaOdPierwszegoDoKażdego, sumaOdDrugiegoDoKażdego, .......]
def sumujKlasy(bezKlasy, klasa):
    odleglosci = []
    odl = 0
    jednaKlasa = []
    for i in range(len(bezKlasy)):
        if(bezKlasy[i][-1] == klasa):
            jednaKlasa.append(bezKlasy[i])

    #print(jednaKlasa)
    for i in range(len(jednaKlasa)):
        for j in range(i + 1, len(jednaKlasa)):
            odl = odleglosc(jednaKlasa[i], jednaKlasa[j])
            odleglosci.append(odl)

    return sum(odleglosci)


#print("Środki punktów dla klas ")
#print("\n")
#print("0: " + str(sumujKlasy(bezKlasy,0)))
#print("1: " + str(sumujKlasy(bezKlasy,1)))
#print("\n")

#print(bezKlasy[0]) 

def zliczZmiany(lista):
    licznik = 0
    for i in range(len(lista)):
        if(oryginal[i][-1] != lista[i][-1]):
            licznik+=1
    return licznik


def porownaj(lista):
    suma0 = sumujKlasy(lista,0)
    suma1 = sumujKlasy(lista,1)
    licznikZmian = zliczZmiany(lista)
    
    #while(licznikZmian > 0):
    #    for i in range(len(lista)):
            
                    
    return lista

#print(porownaj(bezKlasy))

#---------------------------------------------------------------------------------------
#inne zadanie

tabTest = np.array([1,2,3,4])

def srednia(wektor1):
    wektor2 = np.ones(len(wektor1))
    wynik = np.dot(wektor1, wektor2)
    return wynik/len(wektor1)

print("Srednia:")
sr = srednia(tabTest)
print(sr)

#print("\n")

def wariancja(wektor1):
    sr = srednia(wektor1)
    wektorSr = np.ones(len(wektor1))
    a = wektor1 - sr * wektorSr
    b = np.dot(a,a)
    return b/len(wektor1)

print("Wariancja:")
print(wariancja(tabTest))

def odchylenie(wektor1):
    return wariancja(wektor1) ** 0.5
    
print("Odchylenie standardowe:")
print(odchylenie(tabTest))
    
            
