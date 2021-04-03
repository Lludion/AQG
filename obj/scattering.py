
class Scattering:
	
	def __init__(self,f=None):
		
		if hasattr(comp,'__getitem__'):
			self.f = self.chekit
			self.ex = comp
			self.finite = True
		elif callable(f):
			self.ex = ex
			self.f = lambda x : self.checkit(x) or comp(x)
			self.finite = False
		else:
			self.f = f
