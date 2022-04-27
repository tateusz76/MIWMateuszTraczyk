import math
import numpy as np


def proj(u, v):
    return (np.dot(v, u) / np.dot(u, u)) * u


def norm(v):
    return math.sqrt(np.dot(np.transpose(v), v))


def getE(u):
    return u / norm(u)


def getQ(A):
    U = [A[0]]
    for i in range(1, len(A)):
        v_i = A[i]
        u_i = v_i - proj(A[i - 1], v_i)
        U.append(u_i)
    Q = []
    for i in U:
        Q.append(getE(i))
    return np.array(Q)


def getR(Q, A):
    return np.dot(Q, np.transpose(A))


A = np.array([
    [1, 1, 0],
    [0, 1, 1],
    [1, 1, 1],
])
Q = getQ(A)
R = getR(Q, A)
print("Macierz Q: ")
print(np.transpose(Q))

print("Macierz R: ")
print(R)

def wartWlasne(Q,A):
    Qinv = np.linalg.inv(Q)
    return Qinv * A * Q

print("Wartości własne: ")
print(wartWlasne(Q,A))
