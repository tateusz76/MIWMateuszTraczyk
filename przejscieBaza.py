import numpy as np
import math

def czyOrtogonalna(a):
    diagA = np.dot(np.transpose(a), a)
    for i in range(0, len(diag)):
        for j in range(0, len(diag[i])):
            if j != i and diagA[i][j] != 0:
                result = "Nie ortogonalna"
            else:
                result = "Ortogonalna"
    return result


def normalizacja(a):
    result = []
    normA = np.transpose(a)
    for i in normA:
        norm = math.sqrt(np.dot(i, i))
        result.append((i/norm))
    diag = np.dot(np.transpose(result), result)
    return diag, result


a = np.array([
    [1, 1, 1, 0, 1, 0, 0, 0],
    [1, 1, 1, 0, -1, 0, 0, 0],
    [1, 1, -1, 0, 0, 1, 0, 0],
    [1, 1, -1, 0, 0, -1, 0, 0],
    [1, -1, 0, 1, 0, 0, 1, 0],
    [1, -1, 0, 1, 0, 0, -1, 0],
    [1, -1, 0, -1, 0, 0, 0, 1],
    [1, -1, 0, -1, 0, 0, 0, -1],
])


x = np.array([8, 6, 2, 3, 4, 6, 6, 5])
ortA = normalizacja(a)[1]
xBaza = np.round(np.dot(ortA, x), 2)
print(xBaza)
