def basify(bs):
	""" Transforms into a base """
	if isinstance(bs,int):
		return [str(i) for i in range(int)]
	else:
		return bs

def shbase(b):
	""" prints a base """
	if isinstance(b,(tuple,list)):
		if len(b) == 1:
			return shbase(b[0])

	if isinstance(b,tuple):
		s = ""
		for x in b:
			s += shbase(x) + "⊗"
		return s[:-1]
	else:
		s = "<"
		if isinstance(b,list):
			for i in b:
				s += i + ","
		else:
			s += str(b)
		return s + '>'

def basesfrom(*b):
	""" Creates the tensor product of several bases """
	base = b[0]
	for j in range(1,len(b)):
		print(base)
		base = (base,basify(b[j]))
	return base

