from state import *

class Config:
	
	def __init__(self,d=None):
		self.d = defaultdict(complex) # defaultdict
		if d is not None:
			self.d = self.d.union({d})

	def items(self):
		return self.d.items()
