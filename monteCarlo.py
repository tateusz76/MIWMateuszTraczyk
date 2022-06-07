import random

#definicja przykładowej funkcji do sprawdzenia całki
def funkcja(x):
    return x + 2

def monteCarlo(startRange, endRange):
    calka = 0
    przedzial = endRange - startRange #nasz przedział
    for i in range(10000): #im więcej tym dokładniej
        calka = calka + funkcja(startRange + random.uniform(0, przedzial)) #randomowo wyznaczamy punkty w przedziale Monte Carlo
    calka *= przedzial / 10000
    return calka

print(monteCarlo(0,1)) #leci po osi x więc podajemy przedział na osi x
