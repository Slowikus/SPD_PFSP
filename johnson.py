import copy
import numpy as np
from operator import attrgetter
from RandomNumberGenerator import *
# from BF import *
# from Cmax import *
# from BnB import *

n = 6   # zadania
m = 2   # maszyny
Z = 1   # seed

rand = RandomNumberGenerator(Z)

class zadanie:
    def __init__(self,numer):
        self.numer = numer
        self.czasy = []
        for i in range(m):
            self.czasy.append(rand.nextInt(1,29))

zadania = []
for k in range(n):
    zadania.append(zadanie(k))

print("czasy zadan:")
for i in zadania:
    print(i.czasy)

def Johnson(zadania):
    pi = np.zeros((n,1),dtype=int)
    l = 0
    k = n-1

    N = copy.copy(zadania)

    while N:
        numer_zadania = min(N,key=attrgetter("czasy"))
        numer_maszyny = numer_zadania.czasy.index(min(numer_zadania.czasy))
        if numer_zadania.czasy[0] < numer_zadania.czasy[1]:
            pi[l] = copy.copy(numer_zadania.numer)
            l += 1
        else:
            pi[k] = copy.copy(numer_zadania.numer)
            k -=1
        N.remove(numer_zadania)
    pi = pi+np.ones((n,1),dtype=int)
    print("pi:\n",pi)
    return pi

Johnson(zadania)