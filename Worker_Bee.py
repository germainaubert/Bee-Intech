from Bee import bee 

class worker_bee(bee):

	# init une abeillee productrice
	def __init__(self,name = None, cost = 0, category = None, upgrade = [], price = [None,0], required_level = 0, sprite = None, prod = 0, ressource = None):

		super().__init__( name, cost, category, upgrade, price ,required_level, sprite)
		self._prod = prod
		self._ressource = ressource
