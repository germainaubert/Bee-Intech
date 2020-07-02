from Bee import bee 

class fighter_bee(bee):

	# init une abeillee productrice
	def __init__(self, name = None, cost = 0, category = None, price = [None,0], required_level = 0, sprite = None, strength = 0):

		super().__init__( name, cost, category, price ,required_level, sprite)
		self._strength = strength

	def strength(self):
		return self._strength 