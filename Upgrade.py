
class upgrade():

	def __init__(self, name = None, lvl = 0, required_level = 0, price = [None,0], category = None, possession = False, placement = (0,0), description = None, sprite = None):

		self._name = name
		self._lvl = lvl
		self._required_level = required_level
		self._price = price
		self._category = category
		self._possession = possession
		self._placement = placement
		self._sprite = sprite
		self._description = description

	def required_level(self):
		return self._required_level

	def price(self):
		return self._price

	def purchase_upgrade(self):
		self._possession = True

	def sprite(self):
		return self._sprite

	def name(self):
		return self._name

	def lvl(self):
		return self._lvl

