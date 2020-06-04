
class territory():

	def __init__(self, name = None, lvl_require = 0 , number = 0, ressource = None, space = 0, bees = [], possession = False ):
		self._name = name
		self._lvl_require = lvl_require
		self._number = number
		self._ressource = ressource
		self._space = space
		self._bees = bees
		self._possession = possession

	def ressource(self):
		return self._ressource

	def space(self):
		return self._space

	def bees(self):
		return self._bees

	def name(self):
		return self._name

	def possession(self):
		return self._possession