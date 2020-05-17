
class territory():

	def __init__(self, name = None, lvl_require = 0 , number = 0, ressource = None, space = 0, defense = [] ):
		self._name = name
		self._lvl_require = lvl_require
		self._number = number
		self._ressource = ressource
		self._space = space
		self._defense = defense

	def ressource(self):
		return self._ressource

	def space(self):
		return self._space

	def defense(self):
		return self._defense