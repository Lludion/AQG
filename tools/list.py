from collections import Hashable

def uniques(li):
	""" checks whether all elements are unique in ~ O(n) if hashable """
	if not li:
		return True
	if isinstance(li[0], Hashable):
		seen = set({})
		for x in li:
			if x in seen: return False
			seen.add(x)
		return True
	return 

def unify(li):
	g = []
	for x in li:
		if all([not (all([(e in y) for e in x]) and all([(e in x) for e in y]) ) for y in g]):
			g.append(x)
	return g

