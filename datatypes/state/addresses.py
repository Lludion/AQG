

class Addresses(list):
	""" int lists """
	def __init__(self,li):
		assert all([isinstance(y,int) for y in li])
		super().__init__(li)

	def __repr__(self):
		return "A" + super().__repr__()
	
def is_address(x):
	return isinstance(x,int)

