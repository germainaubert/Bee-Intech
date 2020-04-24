from Hive import hive
from Worker_Bee import worker_bee

class shop():

	# Créer le shop
	def __init__(self):

		# liste des abeilles dans le shop
		self._bees = [worker_bee('hervé2', 'Ah il est cher sa mère', 'worker', 'Le roi, jean jass et caballero', 10, 'bonus_fields', 15, 0, "./Images/bak.jpg"),
		worker_bee('hervé3', 'Ah il est cher sa mère', 'worker', 'Le roi, jean jass et caballero', 1560, 'bonus_fields', 10, 0, "./Images/merveille.jpg"),
		worker_bee('hervé4', 'Ah il est cher sa mère', 'worker', 'Le roi, jean jass et caballero', 69, 'bonus_fields', 1500, 0, "./Images/diobrando.jpg"),
		worker_bee('hervé5', 'Ah il est cher sa mère', 'worker', 'Le roi, jean jass et caballero', 420, 'bonus_fields', 105, 0, "./Images/leopepeche.jpg"),]
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
			print('Ò')
		else:
			print('zblax')
			return False