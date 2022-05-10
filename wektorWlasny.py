import numpy as np
import math


def get_An(Q, A):
    Qn = np.transpose(Q)
    Rn = np.dot(Qn, A)
    
    return np.dot(Rn, Q)

def checkTriangle(A):
    for i in range(1, len(A)):
        for j in range(0, i):
            if abs(A[i][j]) > 0.001:
                return False
    return True


def eigenval(A):
    Q, R = np.linalg.qr(A)
    An = np.round(np.dot(Q, R))
    eigenvalTab = []
    
    while not checkTriangle(An):
        Qn = np.transpose(Q)
        Rn = np.dot(Qn, An)
        An = np.dot(Rn, Q)
        Q, R = np.linalg.qr(An)
        
    for i in range(len(An)):
        for j in range(len(An)):
            if i == j:
                eigenvalTab.append(An[i][j])
    return eigenvalTab

def matrixLambda(A, lambd):
    for i in range(0, len(A)):
        for j in range(0, len(A)):
            A[i][j] -= lambd

    return A


A = np.array([
    [1, 2, 5],
    [5, 8, 6],
    [8, 6, 7]
])

tabLambda = eigenval(A)
print(tabLambda)

matrixLambda1 = matrixLambda(A, tabLambda[0])

print(matrixLambda1)




    


    

    





