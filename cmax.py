import numpy as np

# def CMAX(pi, n, m):     # dla dwóch maszyn
#     C = np.zeros((len(pi),m),int)
#     C[0,0] = pi[0].czasy[0]
#     C[0,1] = C[0,0]+pi[0].czasy[1]

#     for i in range(1,len(pi)):
#         C[i,0] = C[i-1,0] + pi[i].czasy[0]

#     for i in range(1,len(pi)):
#         C[i,1] = max(C[i-1,1], C[i,0]) + pi[i].czasy[1]

#     return C, int(C[len(pi)-1,m-1])


def CMAX(pi, n, m):
    n = len(pi)
    m = len(pi[0].czasy)
    C = np.zeros((n,m), dtype=int)

    C[0,0] = pi[0].czasy[0]

    for i in range(1,m):
        C[0,i] = C[i-1,0] + pi[0].czasy[i]      # pierwszy wiersz macierzy
    
    for i in range(1,n):
        C[i,0] = C[i-1,0] + pi[i].czasy[0]      # pierwsza kolumna macierzy

    for i in range(1,n):
        for j in range(1,m):
            C[i,j] = max(C[i-1,j], C[i,j-1]) + pi[i].czasy[j]
    
    return C, int(C[n-1,m-1])
