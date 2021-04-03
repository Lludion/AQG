

class Sector:
	
	def __init__(self,a):
		self.adr = a
		self.t = []
		self.ai = [] # adr in
		self.ao = [] # adr out
		self.xi = [] # data in
		self.xo = [] # data out
	
	def fill(self,t,ai,ao,di,do):
		self.t = t
		self.ai = ai # adr in
		self.ao = ao # adr out
		self.xi = xi # data in
		self.xo = xo # data out

	def __repr__(self):
		return str(self.adr)
