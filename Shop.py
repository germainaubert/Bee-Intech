from Shop_Bee import shop_bee
from Hive import hive

class shop():

	def __init__(self):

		bees = []
		upgrades = []

	def buy_bee(self, hive, shop_bee):

		if shop_bee.price() > hive.honey():
			hive.add_bee(shop_bee.bee())
			hive.honey_loose(shop_bee.price())
		else:
			return False