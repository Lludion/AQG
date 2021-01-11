from datatypes.state import *
from tools.base import *

class Hilbert:
	
	def __init__(self,*b):
		self.basis = basesfrom(*b)

	def __str__(self):
		return shbase(self.basis)

	def __copy__(self):
		return Hilbert(self.basis)

