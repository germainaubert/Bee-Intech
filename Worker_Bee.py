from Bee import bee 

class worker_bee(bee):

	# init une abeillee productrice
	def __init__(self,name = None, cost = 0, category = None, upgrade = [], price = [None,0], required_level = 0, sprite = None, prod = 0, ressource = None, territory = None):

		super().__init__( name, cost, category, upgrade, price ,required_level, sprite)
		self._prod = prod
		self._ressource = ressource
		self._territory = territory

	def prod(self):
		return self._prod

	def ressource(self):
		return self._ressource

	def change_territory(self, name):
		self._territory = name

	def territory(self):
		return self._territory