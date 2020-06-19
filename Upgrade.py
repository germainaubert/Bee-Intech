
class upgrade():

	def __init__(self, name = None, lvl = 0, required_level = 0, price = [None,0], category = None, possession = False, placement = (0,0,0,0), description = None, sprite = None):

		self._name = name
		self._lvl = lvl
		self._required_level = required_level
		self._price = price
		self._category = category
		self._possession = possession
		self._placement = placement

	def possession(self):
		return self._possession

	def name(self):
		return self._name

	def required_level(self):
		return self._required_level

	def price(self):
		return self._price

	def purchase_upgrade(self):
		self._possession = True

