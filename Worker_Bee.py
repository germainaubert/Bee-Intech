from Bee import bee 

class worker_bee(bee):

	# init une abeillee productrice
	def __init__(self,name = None, cost = 0, category = None, upgrade = [], prod = 0, bonus_fields = [], price = 0, required_level = 0):

		super().__init__(cost, name, category, upgrade, price ,required_level)
		self._prod = prod
		self._bonus_fields = bonus_fields