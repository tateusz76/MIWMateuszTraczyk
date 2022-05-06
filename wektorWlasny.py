import numpy as np
import math

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


A = A = np.array([
    [3, 2],
    [4, 1],
])


def checkTriangle(A1):
    detA1 = np.linalg.det(A1)
    if(detA1 == np.prod(A1.diagonal())):
        return 1
    else:
        return 0

        
def eigenval(A):
    D1 = A
    Q0 = np.eye(len(A))

    Q1 = getQ(A)
    R1 = getR(Q1, A)

    A1 = R1 * Q1

    #while(checkTriangle(A1) == 0):
        
    


    

    





