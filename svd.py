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
    [5, 2],
    [2, 8]
])

np.set_printoptions(precision=0, suppress=True)

print("Ak:\n")

for i in range(20):
    Q = getQ(A)
    R = getR(Q,A)
    A = np.dot(R,np.transpose(Q))
    
print(A)

def eigen(A):
    tabEigen = []
    for i in range(len(A)):
        tabEigen.append(round(A[i][i]))
    return tabEigen

def sigma(A):
    tabSigma = []
    for i in range(len(A)):
        tabSigma.append(math.sqrt(round(A[i][i])))
    return tabSigma

print("Lewe wartości własne:")
print(eigen(A))
print("Lewe wartości singularne:")
print(sigma(A))
