

class Data:
	def __init__(self,add=[]):
		assert all([isinstance(a,Addresses) for a in add])
		self.set = add

	def __repr__(self):
		if self.set == []:
			return 'Ɛ'
		return ''.join([str(a) for a in self.set])

