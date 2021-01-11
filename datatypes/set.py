from tools import uniques,p3,SetIterator,unify,eps
from datatypes.other import Mot
from copy import deepcopy

class Setc:
	""" Set class """

	def __init__(self,comp=None,ex=None):
		if ex is None: ex = []
		if hasattr(comp,'__getitem__'):
			self.f = self.chekit
			self.ex = comp
			self.finite = True
		elif callable(comp):
			self.ex = ex
			self.f = lambda x : self.checkit(x) or comp(x)
			self.finite = False
		else:
			self.f = self.chekit
			self.ex = ex
			self.finite = True
			
	def chekit(self,x):
		return x in self.ex

	def __len__(self):
		if self.finite:
			return len(self.ex)
		else:
			return float("inf")

	def question(self):
		if self.finite:
			return Setc(self.ex + ['Ɛ'])
		return Target(lambda x : len(x) == 0 or (len(x) == 1 and self.f(x[0])),ex=self.ex + ['Ɛ'])

	def kleene(self):
		return Setc(lambda x : all([self.f(y) for y in x]),ex=self.ex+[Mot([a,b]) for a in self.ex for b in self.ex]+[p3])

	def star(self):
		if self.finite:
			withrep = Setc([Setc([i]) for i in self.ex])
			for i in self.ex:
				for nj in withrep:
					if i not in nj:
						withrep.append(nj.add(i))
			withrep.append(eps)
			return Stored(unify(withrep))

	def append(self,x):
		if self.finite:
			self.ex.append(x)
		else:
			p = self.ex.pop()
			self.ex.append(x)
			self.ex.append(p)#points

	def add(self,e):
		""" returns the union of this set and another element e """
		z = deepcopy(self)
		z.append(e)
		return z

	def union(self,s):
		""" returns the union of this set and another set s """
		z = deepcopy(self)
		for e in s:
			z.append(e)
		return z

	def __contains__(self,x):
		""" whether the set contains x"""
		return self.f(x)
	
	def __getitem__(self,i):
		if not self.finite:
			print("Iterate through infinite ... Not a good sight.")
			return self.f(i)
		else:
			return self.ex[i]

	def __repr__(self):
		if self.finite:
			try:
				return str(set(self.ex))
			except TypeError:
				return str(self.ex)
		else:
			return "∞→"+str(self.ex)
	
	def __iter__(self):
		''' Returns the Iterator object '''
		return SetIterator(self)

	def __add__(self,s):
		return self.union(s)
	
	def __copy__(self):
		return Setc().union(self)

from tools import uniques

class Stored(Setc):
	def __init__(self,comp=None,ex=None):
		super().__init__(comp=comp,ex=ex)
		#if isinstance(add,list):
		#	assert all([isinstance(a,Addresses) for a in add.ex])
		assert uniques(self.ex)

	def __repr__(self):
		if self.ex == []:
			return 'Ɛ'
		return ''.join([str(a) for a in self.ex])

class Target(Stored):
	def __init__(self,comp=None,ex=None):
		super().__init__(comp=comp,ex=ex)
		assert all(len(x) <= 1 for x in self.ex)

