class SetIterator:
	""" Iterator class """
	def __init__(self, se):
		# Set object reference
		self._set = se
		# member variable to keep track of current index
		self._index = 0

	def __next__(self):
		""""Returns the next value from the set object"s list of examples """
		if self._index < len(self._set.ex) :
			result = self._set.ex[self._index]
			self._index +=1
			return result
		raise StopIteration

