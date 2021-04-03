from tools import *
from obj.sector import *
from obj.gate import *

class Skeleton:
	
	def __init__(self,a,g,s,d,n):
		#self.sec = kdd(Sector) #sectors
		self.a = a 
		self.sec = [Sector(i) for i in a] #addresses
		self.g = [Gate(g[k],s[k]) for k in range(len(g))] #gates
		
		self.s = s # scatterings
		
		self.d = d
		self.n = n # useless, only used to create q = d ^<n

	#	def __add_sector(self,a):
	#	self.sec[a]

	def __repr__(self):
		return "Skeleton(A=" + str(self.sec) +"S=" + str(self.s) + "D=" + str(self.d) + ")"
