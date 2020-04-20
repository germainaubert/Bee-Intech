from Shop_Bee import shop_bee
from Hive import hive

class shop():

	# Créer le shop
	def __init__(self):

		# liste des abeilles dans le shop
		bees = []
		# liste des upgrades dans le shop
		upgrades = []

	# Methode d'achat d'un abeille 
	def buy_bee(self, hive, shop_bee):

		# Fonctionne uniquement si on a assez de miel pour acheter l'abeille sinon retourne False
		# Ajoute l'abeille a la ruche et soustrait le cout de l'abeille du total de miel
		if shop_bee.price() < hive.honey():
			hive.add_bee(shop_bee.bee())
			hive.honey_loose(shop_bee.price())
		else:
			return False