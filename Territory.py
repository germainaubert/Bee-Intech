
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
	
class displayed_territory(territory):

	def __init__(self, name = None, lvl_require = 0 , number = 0, ressource = None, space = 0, bees = [], possession = False, display_name = '', description= ''):
		super().__init__(name, lvl_require , number, ressource, space, bees, possession)
		self._display_name = display_name
		self._description = description
