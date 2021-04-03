from obj.state import *

class Config:
	
	def __init__(self,d=None):
		self.d = defaultdict(complex) # defaultdict
		if d is not None:
			self.d[d] = 1

	def items(self):
		return self.d.items()
