
class shop_bee():

	def __init__(self, bee = None, price = 0, required_level = 0):
		self._bee = bee
		self._price = price
		self._required_level = required_level

	def price(self):
		return self._price

	def bee(self):
		return self._bee