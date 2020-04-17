
class hive():

	def __init__(self):

		self.level = 0
		self.exp = 0
		self.honey = 10
		self.honey_prod = 15
		self.pollen = 0
		self.bees = []
		self.upgrades = []

	def honey_gain(self):
		self.honey += self.honey_prod

