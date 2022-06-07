import random
import numpy as np

def fun(x):
    return x #calka z x = 0,5

def calkaKwadraty(start, koniec):
    wynik = 0
    baza = np.linspace(start, koniec, 10000)
    dx = (baza[-1] - baza[0]) / 10000
    for i in range(len(baza)):
        wynik = wynik + dx * fun(baza[i])
    return wynik

print(calkaKwadraty(0, 1))
