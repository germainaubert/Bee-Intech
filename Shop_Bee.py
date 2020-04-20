
class shop_bee():

	# Créer une des abeilles presente dans la boutique avec un prix et un niveau requis pour l'acheter
	def __init__(self, bee = None, price = 0, required_level = 0):
		self._bee = bee
		self._price = price
		self._required_level = required_level

	# retourne le prix
	def price(self):
		return self._price
		
	# retourne l'abeille
	def bee(self):
		return self._bee