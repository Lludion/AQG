from obj.skeleton import *
from obj.config import *

class AQC:

	def __init__(self,s,e):
		self.s = s #skeleton object
		self.e = e #a confing on s object ( defaultdict : state -> complex )

	def evolve(self):
		nconf = Config(complex)
		for state,alpha in self.e.items():
			newconfig = state.evolve()
			for ns,beta in newconfig.items():
				nconf[ns] += beta
		self.e = nconf

	def __repr__(self):
		return str("AQC\n") + str(self.s) + "\n" + str(self.e)
