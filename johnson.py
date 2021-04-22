from copy import copy
import numpy as np
from operator import attrgetter
from RandomNumberGenerator import *
from cmax import *

n = int(input("podaj ilosc zadan: "))   # zadania 6
m = int(input("podaj ilosc maszyn: "))  # maszyny 2
Z = int(input("podaj ziarno: "))   # seed 1

random = RandomNumberGenerator(Z)

class zrob:
    def __init__(self,numer):
        self.numer = numer
        self.czasy = []
        for i in range(m):
            self.czasy.append(random.nextInt(1,29))   # dodawanie czasów na m maszyn

tab_zadania = []    # pusta tabela zadan
for k in range(n):
    tab_zadania.append(zrob(k))  # przydzielanie zadań z przydzielonymi czasami na m maszyn

print("---------------------\nczasy zadan:")
for i in tab_zadania:
    print(i.czasy)

def Johnson(tab_zadania):
    pi = np.zeros((n,1),dtype=int)  # stworzenie zerowego wektora
    l = 0
    k = n-1

    N = copy(tab_zadania)  # skopiowanie zadan
    pi = copy(tab_zadania)

    while N:
        numer_zadania = min(N,key=attrgetter("czasy"))  # znajdowanie zadania o najkrótszym czasie wykonywania
        numer_maszyny = numer_zadania.czasy.index(min(numer_zadania.czasy)) # numer masszyny na ktorym najkrotsze zadanie sie wykonuje
        if numer_zadania.czasy[0] < numer_zadania.czasy[m-1]:
            pi[l] = copy(numer_zadania)
            l += 1
        else:
            pi[k] = copy(numer_zadania)
            k -=1
        N.remove(numer_zadania)
    print("---------------------\nJOHNSON")
    print("---------------------\npi: ",end = " ")
    for i in pi:
        print(i.numer + 1, end = " ")
    print()
    return pi

pi = Johnson(tab_zadania)

a,b = CMAX(pi, n, m)
print("---------------------\nC:\n",a)
print("---------------------\nCmax: ",b)
