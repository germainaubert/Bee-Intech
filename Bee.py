class bee():

	# init une abeille
	def __init__(self,name = None, cost = 0, category = None, upgrade = [], price = 0, required_level = 0):

		self._name = name
		self._cost = cost
		self._category = category
		self._upgrade = upgrade
		self._price = price
		self._required_level = required_level

	# retourne la categorie de l'abeille
	def category(self):
		return self._category

	def price(self):
		return self._price

	def name(self):
		return self._name