from tools import *
from sector import *
from gate import *

class Skeleton:
	
	def __init__(self,a,g,s,d,n):
		#self.sec = kdd(Sector) #sectors
		self.a = a 
		self.sec = [Sector(i) for i in a] #addresses
		self.g = [Gate(k,s[k]) for k in g] #gates
		self.d = d
		self.n = n # useless, only used to create q = d ^<n

#	def __add_sector(self,a):
#		self.sec[a]
