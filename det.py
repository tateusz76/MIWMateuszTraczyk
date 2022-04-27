def wyznacznikKwadratowa(macierz, stopien):

    width = len(macierz)
    if width == 1:
        return stopien * macierz[0][0]
    else:
        znak = -1
        wynik = 0
        for i in range(width):
            temp1 = []
            for j in range(1, width):
                temp2 = []
                for k in range(width):
                    if k != i:
                        temp2.append(macierz[j][k])
                temp1.append(temp2)
            znak *= -1
            wynik = wynik + stopien * wyznacznikKwadratowa(temp1, znak * macierz[0][i])
            #znakHelper to zmienna pilnująca żeby przy rekurencji zmieniał się znak +,-,+,- itd.
            #znak robi to samo ale do ogólnego wyniku
    return wynik

tab = [[1,2,1],[2,1,2],[2,2,1]]

print(wyznacznikKwadratowa(tab, 1))
