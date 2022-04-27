import random

#definicja przykładowej funkcji do sprawdzenia całki
def funkcja(x):
 return x

punkty = 10000 #im więcej punktów tym dokładniejsze całkowanie, czyli
#przy każdym uruchomieniu będzie mniejszy od siebie rozstrzał wyniku

def monteCarlo(startRange, endRange):
    calka = 0.
    dx = endRange - startRange #nasz przedział
    for i in range(punkty):
        calka += funkcja(startRange + random.uniform(0, dx)) #randomowo wyznaczamy punkty w przedziale Monte Carlo
    calka *= dx / punkty
    return calka

print(monteCarlo(0,1)) #leci po osi x więc podajemy przedział na osi x
