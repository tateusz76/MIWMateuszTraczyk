import numpy as np

tabX = [2,5,7,8]
tabY = [1,2,3,3]
ones = np.ones(len(tabX))

X = np.column_stack((ones, tabX))
print(X)
print("\n")

def transpozycja(macierz):
    rows = len(macierz)
    cols = len(macierz[0])

    T = []
    for j in range(cols):
        row = []
        for i in range(rows):
           row.append(macierz[i][j])
        T.append(row)

    return T

XT = transpozycja(X)
XT = np.row_stack(XT)
XTX = np.linalg.inv(np.dot(XT, X))
print(XT)
print("\n")

print(XTX)
print("\n")

B = np.dot(XTX, XT)
B = np.dot(B, tabY)

print(B)


    

#for i in range(len(tabX)):
#    print(X[0][0])

#B = (X^T * X) * X^T * Y
