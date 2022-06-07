import math
import numpy as np

def normalizacja(v):
    return math.sqrt(np.dot(v, v))

def projekcja(u,v):
    top = np.dot(v,u)
    bot= np.dot(u,u)
    return(top/bot) * u

def getE(u):
    return u/normalizacja(u)

def getQ(A):
    Qtemp = [A[0]]
    Q = []
    for i in range(1, len(A)):
        v = A[i]
        u = v - projekcja(A[i-1],v)
        Qtemp.append(u)
    for i in Qtemp:
        Q.append(getE(i))
    return np.array(Q)

def getR(Q, A):
    return(np.dot(Q, np.transpose(A))) #dziwna rzecz z kalkulatorami online


A = np.array([
    [0, 1, 2],
    [1, 0, 2],
])

Q = getQ(A)
print("Q:\n")
print(Q)

R = getR(Q,A)
print("R:\n")
print(R)
