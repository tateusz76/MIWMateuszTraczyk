import random
import numpy as np

def fun(x):
    return x #calka z x = 0,5

def calkaKwadraty(start, koniec, punkty):
    wynik = 0
    baza = np.linspace(start, koniec, punkty)
    dx = (baza[-1] - baza[0]) / punkty
    for i in range(len(baza)):
        wynik = wynik + dx * fun(baza[i])
    return wynik

print(calkaKwadraty(0, 1, 1000))
