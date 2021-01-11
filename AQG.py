from datatypes import *
from datatypes.state import *
from tools import *
from copy import copy

#from sys import setrecursionlimit
#setrecursionlimit(10**6)

A = Setc(Addresses([1,2,4]))
B = Setc(Addresses([7,8,9]))
D = Setc(['a','b'])
print(A)

# Adresses
astar = A.star()
print(astar,astar.__class__.__name__)
stored_as = Hilbert(astar)
print(stored_as)

# DATA
dkleene = D.kleene()
print(dkleene)
data_as = Hilbert(dkleene)
print(data_as)

#INPUT/OUTPUT
input_sp = cart(stored_as,data_as)
print(input_sp)

output_sp = cart(copy(stored_as),copy(data_as))
print(output_sp)

#TARGET
aquestion = A.question()
print(aquestion)
target_sp = Hilbert(aquestion)
print(target_sp)

#SECTORSPACE
sector_sp = cart(target_sp,input_sp,output_sp)
print(sector_sp)

#GATES
