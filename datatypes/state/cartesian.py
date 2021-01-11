from datatypes.state.hilbert import *

def cartesian(*hilbertianstates):
	""" Cartesian product of h and g """
	return Hilbert(*[x.basis for x in hilbertianstates])

cart = carte = cartesian

