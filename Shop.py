from Hive import hive
from Worker_Bee import worker_bee

class shop():

	# Créer le shop
	def __init__(self):

		# liste des abeilles dans le shop
		self._bees = [worker_bee('hervé2', 'Ah il est cher sa mère', 'worker', 'Le roi, jean jass et caballero', '140', 'bonus_fields', 1, 0)]
		# liste des upgrades dans le shop
		upgrades = []

	def bee(self,i):
		return self._bees[i]

	def bees(self):
		return self._bees
	# Methode d'achat d'un abeille 
	def buy_bee(self, hive, bee):

		# Fonctionne uniquement si on a assez de miel pour acheter l'abeille sinon retourne False
		# Ajoute l'abeille a la ruche et soustrait le cout de l'abeille du total de miel
		if bee.price() <= hive.honey():
			hive.add_bee(bee)
			hive.honey_loose(bee.price())
			print(hive._bees[0])
		else:
			return False