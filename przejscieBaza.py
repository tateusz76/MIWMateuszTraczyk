import numpy as np

def czyOrt(a, aT):
    diagA = np.dot(aT, a)
    diagTest = np.diag(np.diag(diagA))
    return diagTest

def normalizacja(v):
    normV = v / np.sqrt(np.sum(v**2))
    return normV

a = np.array([
    [1,1,1,1,1,1,1,1],
    [1,1,1,1,-1,-1,-1,-1],
    [1,1,-1,-1,0,0,0,0],
    [0,0,0,0,1,1,-1,-1],
    [1,-1,0,0,0,0,0,0],
    [0,0,1,-1,0,0,0,0],
    [0,0,0,0,1,-1,0,0],
    [0,0,0,0,0,0,1,-1]
    ])

aT = np.transpose(a)

#print(czyOrt(a, aT))
for i in range(0,len(a)-1):
    a[i] = normalizacja(a[i])

v = [8,6,2,3,4,6,6,5]

print(np.dot(a,v))
