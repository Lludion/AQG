
class Mot:
	def __init__(self,ex):
		self.ex = ex
	
	def append(self,e):
		self.ex.append(e)

	def __repr__(self):
		if self.ex == []:
			return 'Ɛ'
		return ''.join([str(a) for a in self.ex])

