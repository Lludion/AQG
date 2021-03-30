from collections import defaultdict
from json import load

class kdd(defaultdict):
	def __missing__(self, key):
		if self.default_factory is None:
			raise KeyError(key)
		else:
			ret = self[key] = self.default_factory(key)
			return ret

	def unionjson(self,name):
		""" does the union with the dict created by the corresponding json """
		with open("_/json/"+name+".json", "r", encoding="utf-8-sig") as op:
			z = load(op)
			for k,v in z.items():
				self[k] = v
