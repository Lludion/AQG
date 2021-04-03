from collections import defaultdict

def values(x):
	return x.values()

class State:
	def __init__(self,t,l=[0,0],d=[0,0],s=None):
		if l[0] == 0:
			li = lo = defaultdict(list) # returns empty list
		else:
			li,lo = l

		if d[0] == 0:
			di = do = defaultdict(list) # returns empty list
		else:
			di,do = d
		self.t = t
		self.di = di
		self.do = do # lists or defaultdicts addr -> list of data/addr
		self.li = li
		self.lo = lo
		self.skeleton = s

	def all(self):
		return list(self.t)+list(self.di)+list(self.do)+list(self.li)+list(self.lo)

	def items(self):
		return items(self.t)+items(self.di)+items(self.do)+items(self.li)+items(self.lo)

	def appearing(self):
		z =  values(self.t)+values(self.li)+values(self.lo)
		return [item for sublist in z for item in sublist]

	def check(self,s=None):
		if s is None:
			s = self.s
		elif self.s is None:
			self.s = s
		for x in self.all(): # checks all addresses are in the skeleton
			assert x in s.a
		for x in self.lo.values() + self.li.values():
			for y in x:
				assert y in s.a
		# check data length & origin dataset
		for x in self.do.values() + self.di.values():
			for y in x:
				assert x in s.d
			assert len(x) <= s.n
		# check for non repetitions !
		assert len(self.appearing()) == len(set(self.appearing))

	def __repr__(self):
		return "Config{" + str(self.items) + "}"

